from utils.utils import Utils

class Router:
    def __init__(self):
        self.utils = Utils()
        self.symbols = self._get_symbols_data()
        self.download_symbols_dropdown()
        self.download_sector_dropdown()

    def _get_symbols_data(self):
        symbols = self.utils.read_csv('nasdaq')
        symbols = symbols.append(self.utils.read_csv('nyse'))
        return symbols

    def download_symbols_dropdown(self):
        dd_symbols = []
        for i,row in self.symbols.sort_values(by=['Symbol']).iterrows():
            dd_symbols.append({'label': f'{row["Symbol"]} ({row["Name"]})', 'value': row['Symbol']})
        self.download_symbols = dd_symbols
    
    def update_download_symbols_dropdown(self,value):
        dd_symbols = []
        if value is not None:
            filter_symbols = self.symbols[self.symbols['Sector'] == value]
            for i,row in filter_symbols.sort_values(by=['Symbol']).iterrows():
                dd_symbols.append({'label': f'{row["Symbol"]} ({row["Name"]})', 'value': row['Symbol']})
            return dd_symbols
        else:
            return self.download_symbols

    def download_sector_dropdown(self):
        dd_symbols = []
        for i in set(self.symbols['Sector'].sort_values()):
            print(type(i))
            dd_symbols.append({'label': i, 'value': i})
        self.download_sectors = dd_symbols

