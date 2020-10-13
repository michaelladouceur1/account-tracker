from utils.utils import Utils

class Router:
    def __init__(self):
        self.utils = Utils()

    def dropdown_symbols(self):
        dd_symbols = []
        symbols = self.utils.read_csv('nasdaq')
        symbols = symbols.append(self.utils.read_csv('nyse'))
        print(symbols)
        for i in symbols['Symbol'].sort_values():
            dd_symbols.append({'label': i, 'value': i})
        return dd_symbols
