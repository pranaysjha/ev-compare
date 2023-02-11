import yfinance as yf

class EVCompare:
    
    def __init__(self, symbol: str):
        self._ticker = yf.Ticker(symbol)

        self._balance_sheet = self._ticker.balance_sheet
        self._debt = self._balance_sheet.loc['Total Debt']
        self._cash = self._balance_sheet.loc['Cash And Cash Equivalents']

        self._income_stmt = self._ticker.income_stmt
        self._shares = self._income_stmt.loc['Diluted Average Shares']

        self._close = self._ticker.history(period='5y')
        