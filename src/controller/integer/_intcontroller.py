from generator.intgen import IntGen
from controller._controlbase import ControlBase
from utils.inttype import IntType


class IntController(ControlBase):
    def __init__(self, int_type: IntType, rows, args):
        super().__init__()
        self._int_type = int_type
        self.how_many = rows
        self.args = args
        self.is_primary = False
        self.auto_increment = False
        self.min_val = None
        self.max_val = None
        self._parse_args()

    def _has_enough_numbers(self):
        """ Stop the execution if the range of available numbers is less than how many rows is needed """
        ava_nums = self._int_type.available_numbers
        if ava_nums < self.how_many:
            raise Exception(
                f"Error: {self._int_type.name} range ({ava_nums}) is less than the selected number of rows ({self.how_many})")

    def _parse_args(self):
        if '-u' in self.args:
            self._int_type.is_unsigned = True
            del self.args[self.args.index('-u')]
        if '-a' in self.args:
            self.auto_increment = True
            self._has_enough_numbers()
            self.can_generate = False
            del self.args[self.args.index('-a')]
        if '-p' in self.args:
            self.is_primary = True
            self._has_enough_numbers()
            del self.args[self.args.index('-p')]

        for current_arg in self.args:
            import re
            cmd = current_arg[:2]
            cmd_args = current_arg[2:]

            if '-r' == cmd:
                if not re.match(r"-?\d+:-?\d+", cmd_args):
                    raise Exception(f"Error: bad formatted parameters '{cmd_args}' from {cmd} argument")

                num1, num2 = cmd_args.split(':')
                num1, num2 = int(num1), int(num2)
                #  This should be executed after -u since -u will change the range
                if self._int_type.is_out_of_bounds(num1):
                    raise Exception(f"Error: the first parameter from {cmd}, '{num1} is out of the bounds from '{self._int_type.name}'")
                elif self._int_type.is_out_of_bounds(num2):
                    raise Exception(f"Error: the first parameter from {cmd}, '{num2} is out of the bounds from '{self._int_type.name}'")

                self.min_val = num1
                self.max_val = num2
                del self.args[self.args.index(current_arg)]

        if len(self.args) > 0:
            raise Exception(f"Error: invalid argument {self.args[0]}")

        self.list_is_unique = self.is_primary

    def _gen_random(self):
        while len(self.rows) < self.how_many:
            min = self.min_val or self._int_type.min()
            max = self.max_val or self._int_type.max()
            val = IntGen.generate(min, max)
            self.rows.add(val)

    @property
    def type_name(self):  # TODO: check if this is the correct form of write unsigned types?
        tn = self._int_type.name
        tn += ' UNSIGNED' if self._int_type.is_unsigned else ''
        tn += ' PRIMARY KEY' if self.is_primary else ''
        tn += ' AUTO_INCREMENT' if self.auto_increment else ''
        return tn

    def gen(self):
        """ Generates the data """
        self._gen_random()
