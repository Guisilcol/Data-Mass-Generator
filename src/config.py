import os

# Create the database path dynamically according to operating system
DATABASE_PATH = os.path.normcase(__file__.rsplit("src")[0] + 'db/database.db')
    
