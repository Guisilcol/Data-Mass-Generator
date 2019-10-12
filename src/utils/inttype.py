# Defines constraints on int types
# reference https://dev.mysql.com/doc/refman/8.0/en/integer-types.html


class IntType:
    def __init__(self, min, max, unsigned_min, unsigned_max, name):
        self.is_unsigned = False
        self._min = min
        self._max = max
        self._unmax = unsigned_max
        self._unmin = unsigned_min
        self.name = name

    def max(self):
        return self._unmax if self.is_unsigned else self._max

    def min(self):
        return self._unmin if self.is_unsigned else self._min

    @property
    def available_numbers(self):
        return abs(self.min()) + self.max() + 1  # 1 since zero is included

    def copy(self):
        from copy import copy
        return copy(self)

    def is_out_of_bounds(self, number):
        return number < self.min() or number > self.max()


TINYINT = IntType(-128, 127, 0, 255, 'TINYINT')
SMALLINT = IntType(-32768, 32767, 0, 65535, 'SMALLINT')
MEDIUMINT = IntType(-8388608, 8388607, 0, 16777215, 'MEDIUMINT')
INT = IntType(-2147483648, 2147483647, 0, 4294967295, 'INT')
BIGINT = IntType(-2 ** 63, 2 ** 63 - 1, 0, 2 ** 64 - 1, 'BIGINT')
