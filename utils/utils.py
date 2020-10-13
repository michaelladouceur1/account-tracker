import datetime
import pandas as pd
import platform 

if platform.system()=='Linux':
    BASE_PATH = '/home/michael/Documents/Coding/account-tracker/utils/assets/'
elif platform.system()=='Windows':
    BASE_PATH = 'C:\\Users\\mladouceur\\Python\\account-tracker\\utils\\assets\\'

class Utils:
    def _current_date_time(self, format):
        time = dt.datetime.now()
        if format == 'datetime':
            return f'{time.year}-{time.month}-{time.day} {time.hour}:{time.minute}'
        elif format == 'date':
            return f'{time.year}-{time.month}-{time.day}'

    def read_csv(self, csv):
        df = pd.read_csv(f'{BASE_PATH}{csv}.csv')
        return df
