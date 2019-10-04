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
            del self.args[self.args.index('-a')]
        if '-p' in self.args:
            self.is_primary = True
            self._has_enough_numbers()
            del self.args[self.args.index('-p')]

        if len(self.args) > 0:
            raise Exception("Error: invalid argument {0}".format(self.args[0]))

    def _gen_random(self):
        i = 0
        while i < self.how_many:
            val = IntGen.generate(self._int_type.min(), self._int_type.max())
            if not self.is_primary or (self.is_primary and not val in self.rows):
                self.rows.append(val)
                i += 1

    @property
    def type_name(self):  # TODO: check if this is the correct form of write unsined types?
        tn = self._int_type.name
        tn += ' UNSIGNED' if self._int_type.is_unsigned else ''
        tn += ' PRIMARY KEY' if self.is_primary else ''
        tn += ' AUTO_INCREMENT' if self.auto_increment else ''
        return tn

    def gen(self):
        """ Returns a string containing the file path where the values are stored """
        if self.auto_increment:
            return  # does nothing since in this case no number need to be generated

        self._gen_random()
        self.serialize()
