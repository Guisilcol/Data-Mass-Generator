from src.abstract.database import Database
from src.config import DATABASE_PATH


class Name(Database):

    def name(self) -> str:
        sql = "SELECT name FROM name ORDER BY RANDOM() LIMIT 1;"
        data = self.getData(sql, DATABASE_PATH)
        return data[0][0]

    def surname(self) -> str:
        sql = "SELECT surname FROM surname ORDER BY RANDOM() LIMIT 1;"
        data = self.getData(sql, DATABASE_PATH)
        return data[0][0]

    def name_surname(self) -> str:
        name = self.name()
        surname = self.surname()
        return "{} {}".format(name, surname)