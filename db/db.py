import sqlite3 
import platform 

if platform.system()=='Linux':
    BASE_PATH = '/home/michael/Documents/Coding/account-tracker/db/'
elif platform.system()=='Windows':
    BASE_PATH = 'C:\\Users\\mladouceur\\Python\\account-tracker\\db\\'

DATABASE_FILE_PATH = f'{BASE_PATH}securities.db'

class DB:
    def __init__(self):
        self.db = DATABASE_FILE_PATH
        self.conn = sqlite3.connect(self.db)
        self.c = self.conn.cursor()