# Defines constraints on int types
# reference https://dev.mysql.com/doc/refman/8.0/en/integer-types.html

class IntType:
     def __init__(self, min, max, unsigned_min, unsigned_max):
          self.is_unsigned = False
          self._min = min
          self._max = max
          self._unmax = unsigned_max
          self._unmin = unsigned_min
     
     def max(self):
          return self._unmax if self.is_unsigned else self._max
     
     def min(self):
          return self._unmin if self.is_unsigned else self._min 

     def is_out_of_bounds(self, number):
          return number < self.min() or number > self.max()
     

TINYINT = IntType(-128, 127, 0, 255)
SMALLINT = IntType(-32768, 32767, 0, 65535)
MEDIUMINT = IntType(-8388608, 8388607, 0, 16777215)
INT = IntType(-2147483648, 2147483647, 0, 4294967295)
BIGINT = IntType(-2**63, 2**63-1, 0, 2**64-1) # not sure if the calc is precise

