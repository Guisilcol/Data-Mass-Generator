import os

# Has dynamically created database path according to operating system
DATABASE_PATH = os.path.normcase(__file__.rsplit("src")[0] + 'db/database.db')
    