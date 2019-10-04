# Base class from generators, it saves the chunks of data into files
from tempfile import NamedTemporaryFile
from abc import ABCMeta, abstractmethod


class ControlBase(metaclass=ABCMeta):
    def __init__(self):
        super().__init__()
        self.rows = []
        self._temp_file = NamedTemporaryFile('w+', delete=False)

    def __del__(self):
        import os
        if not self._temp_file.closed:
            self._temp_file.close()
        os.unlink(self._temp_file.name)

    @property
    @abstractmethod
    def type_name(self):
        """ Must return the type name as is in SQL """
        pass

    @abstractmethod
    def gen(self):
        """ Must return generate the random values """
        pass

    @property
    def file_name(self):
        from os.path import exists
        if not exists(self._temp_file.name):
            raise Exception('Error: tempfile not found')

        return self._temp_file.name

    def serialize(self):
        """ Save the itens in a temporary file, one per line.
        The file will be removed when the instance of this class be collected by the gasbage collector
        """
        if not self._temp_file.closed:
            self._temp_file.writelines([f"{str(item)}\n" for item in self.rows])
            self._temp_file.close()
