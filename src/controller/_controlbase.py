# Base class from generators, it saves the chunks of data into files
from tempfile import TemporaryFile


class ControlBase:
	def __init__(self):
		self.rows = []
		self._temp_file = TemporaryFile('w+', delete=False)

	def __del__(self):
		import os
		if not self._temp_file.closed:
			self._temp_file.close()
		os.unlink(self._temp_file.name)

	def serialize(self):
		if self._temp_file.closed:
			return
		self._temp_file.writelines([f"{str(item)}\n" for item in self.rows])
		self._temp_file.close()


