# Base class from generators, it saves the chunks of data into files
from tempfile import NamedTemporaryFile
from abc import ABCMeta, abstractmethod


class ControlBase(metaclass=ABCMeta):
    def __init__(self):
        super().__init__()
        self.rows = []
        self.can_generate = True
        self._temp_file = NamedTemporaryFile('r+', delete=False)

    def __del__(self):
        import os
        if not self._temp_file.closed:
            self._temp_file.close()
        os.unlink(self._temp_file.name)

    @property
    @abstractmethod
    def type_name(self):
        """ Must return the type name as is in SQL (e.g: VARCHAR(30) NOT NOLL...) """
        pass

    @abstractmethod
    def gen(self):
        """ Must generate the random data. If can_generate is set true then gen must do nothing. """
        pass

    def dump_line(self):
        """ Get one item from the temporary file. If serialize() has not called before then the file will be empty """
        return self._temp_file.readline().rstrip()

    def serialize(self):
        """ Save the data in a temporary file, one per line.
        The file will be removed when the instance of this class get collected by the garbage collector
        """
        self._temp_file.writelines([f"{str(item)}\n" for item in self.rows])
        self._temp_file.flush()
        self._temp_file.seek(0)  # reset position for when dump_line be called
