from pydoc import locate


class MainControl:
    def __init__(self):
        self.db_name = ''
        self.rows_count = 0
        self.controllers = []
        self.script = ''

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
            ctrl.gen()  # maybe move it to somewhere else
            self.controllers.append(ctrl)

        self.create_table(params)
        self.create_insert(params)

    def create_table(self, params):
        """Create the table creation script"""
        self.script = f"CREATE TABLE {self.db_name}\n("
        field_names = [i for i in params.keys() if not i.startswith('$')]

        for i, item in enumerate(field_names):
            row_data = self.controllers[i].type_name
            self.script += f"\t{item} {row_data}"

            if i != len(field_names) - 1:
                self.script += ","

            self.script += "\n"

        self.script += f")\n"
        # save it into a file since the next method will load a mass of data

    def create_insert(self, params):
        """Create the values insertion script"""
        pass

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
