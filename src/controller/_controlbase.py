# Base class from generators, it saves the chunks of data into files
import tempfile


class ControlBase:
	def __init__(self):
		self.rows = []
		self._temp_file = tempfile.TemporaryFile(delete=False)

	def serialize(self):
		for item in self.rows:
				self._temp_file .write(bytes(item))

