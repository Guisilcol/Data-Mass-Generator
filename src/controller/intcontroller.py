from integer._intgen import IntGen


# TODO: add flag to prevent how_many of being greater than max amount of numbers of smallint, may use abs(min) - max to get the range of total numbers availiables
# of course, the flag will only work if is_primary is true since in the situation is not possible to all entrys be unique

# TODO: treat auto increment

class IntController:
    is_primary: bool

    def __init__(self, int_type, is_primary=False, rows=1):
        self._int_type = int_type
        self.how_many = rows
        self.is_primary = is_primary
        self.fields = []

    def gen(self):
        i = 0
        while i < self.how_many:
            val = IntGen.generate(self._int_type.min(), self._int_type.max())
            if not self.is_primary or (self.is_primary and not val in self.fields):
                self.fields.append(val)
                i += 1
        # TODO: must return something else in the future
        return self.fields
