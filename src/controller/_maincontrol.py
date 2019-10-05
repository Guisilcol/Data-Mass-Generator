from pydoc import locate


class MainControl:
    def __init__(self, file):
        self.db_name = ''
        self.rows_count = 0
        self.controllers = []
        self.file = file

    def init(self, params):
        self.db_name = params.get('$db', False)
        self.rows_count = params.get('$rows', False)

        if not self.db_name:
            raise Exception('Error: database ($db) name must be specified')

        if not self.rows_count:
            raise Exception('Error: rows count ($rows) must be specified')

        for field_name, field_value in params.items():  # generates the values filed-by-field first
            if field_name.startswith('$'):
                continue

            local_param = field_value.strip().split(' ')
            namespace = local_param[0]
            args = local_param[1:]

            ctrl = self.call_controller(namespace, self.rows_count, args)
            self.controllers.append(ctrl)

        self.generate()
        self.create_table(params)
        self.create_insert(params)

    def generate(self):
        for ctrl in self.controllers:
            if ctrl.can_generate:
                ctrl.gen()
                ctrl.serialize()

    def create_table(self, params):
        """ Create the table creation sql script (CREATE TABLE...) """
        script = f"CREATE TABLE {self.db_name}\n("
        field_names = [i for i in params.keys() if not i.startswith('$')]

        for i, item in enumerate(field_names):
            row_data = self.controllers[i].type_name  # ctrls are expected to be in the same order as dict keys
            script += f"\t{item} {row_data}"

            if i != len(field_names) - 1:
                script += ','

            script += "\n"

        script += f")\n"
        self.append(script)

    def create_insert(self, params):
        """ Add the data to the script (INSERT INTO...) """
        script = ''
        field_names = [i for i in params.keys() if not i.startswith('$')]

        # Create the insert header
        script += f"INSERT INTO {self.db_name} ("
        for i, item in enumerate(field_names):
            if not self.controllers[i].can_generate:
                continue
            script += item

            if i != len(field_names) - 1:
                script += ', '

        script += ') VALUES'
        self.append(script)
        script = ''

        # Add data
        i = 0
        while i < self.rows_count:
            script += f"\t("
            for idx, ctrl in enumerate(self.controllers):
                if not ctrl.can_generate:
                    continue
                script += ctrl.dump_line()

                if idx != len(self.controllers) - 1:
                    script += ', '

            script += ')'
            self.append(script)
            script = ''
            i += 1

    def append(self, text):
        self.file.write(f"{text}\n")

    @classmethod
    def call_controller(cls, namespace: str, row_count: int, args: list):
        """ The correct controller will be instanced dynamically using reflection within this method.

        The controllers must be inside of the controller folder followed by the folder of it's type
        and the file must have a generate method that will make an instance of the controller class.

            structure: controller_folder.type_folder.file.generate()
        """
        instance = locate(f"controller.{namespace}.generate")
        if instance is None:
            raise Exception(f"Error: namespace {namespace} not found")

        return instance(row_count, args)
