import sqlite3
import os
from datetime import datetime

# Helper functions
def remove_file(filename):
    if os.path.exists(filename):
        os.remove(filename) 

def get_data(data: str) -> str:
    if data.strip() == '' or data.strip().isnumeric():
        return None
    return data.strip()

def create_file(filename):
    with open(filename, 'w') as f:
        f.close()
        
def append_data(filename, data):
    with open(filename, 'a+') as f:
        f.write(data)
        f.close()

def read_data(filename):
    data = ''
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data += line
        f.close()
    return data

class EntryNotFoundError(Exception):
    def __init__(self, error_msg):
        self.error_msg = error_msg
        
    def __str__(self):
        return self.error_msg

class Journal:
    def __init__(self, db_file):
        self.__conn     = sqlite3.connect(db_file)
        self.__cursor   = self.__conn.cursor()
        self.__data     = None
        self.__filename = 'journal.txt'
        create_file(self.__filename)
        self.__cursor.execute("CREATE TABLE IF NOT EXISTS my_table(data VARCHAR(50), date DATE)")
        
    @property
    def today(self):
        data_compose = ''
        datas = self.__cursor.execute("SELECT * FROM my_table").fetchall()
        for temp in datas:
            data_compose += temp[0] + '\n'
        
        if not os.path.exists(self.__filename):
            raise FileNotFoundError('No diary entry')
        
        append_data(self.__filename, data_compose)
        self.__data = get_data(read_data(self.__filename))
        return self.__data
    
    @today.setter
    def today(self, entry):
        self.__cursor.execute(f"INSERT INTO my_table VALUES('{entry}', '{datetime.now()}')")
        self.__conn.commit()
        
    @today.deleter
    def today(self):
        if not os.path.exists(self.__filename):
            raise FileNotFoundError('No diary entry')
        remove_file(self.__filename)
            
if __name__ == '__main__':
    j = Journal('journal.sqlite3')
    j.today = 'Visited Harbin City'
    j.today = 'Visited Hangzhou City'
    print(j.today)
    # del j.today
    # print(j.today)