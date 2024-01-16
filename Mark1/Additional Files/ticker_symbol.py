# import yfinance as yf

# def get_nse_symbols():
#     symbols = []

#     # Fetching data for NSE stocks by specifying the exchange as "NS"
#     nse_stocks = yf.Tickers("NSE")
    
#     for stock in nse_stocks.tickers:
#         print(stock)
#         symbols.append(stock)

#     return symbols

# def save_symbols_to_file(symbols, filename):
#     with open(filename, 'w') as file:
#         for symbol in symbols:
#             file.write(symbol + '\n')

# if __name__ == "__main__":
#     symbols = get_nse_symbols()
#     print("List of NSE Stock Ticker Symbols:")
#     print(symbols)
    
#     file_name = "NSE_symbols_yfinance.txt"
#     save_symbols_to_file(symbols, file_name)
#     print(f"Symbols saved to '{file_name}' file.")

import yfinance as yf

# Get the list of all NSE stocks
nse_tickers = yf.Tickers('INR=X')

# Print the list of ticker symbols
print(nse_tickers.tickers['INR=X'])