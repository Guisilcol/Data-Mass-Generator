import sqlite3


class Database():

    # Returns a list containing the informed query data.
    def get_data(self, sql: str, database_path: str) -> list:
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        result_set = cursor.execute(sql).fetchall()
        cursor.close()
        connection.close()

        return result_set
