import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_super_trend(data, period=7, multiplier=3):
    df = data.copy()
    
    # Calculate True Range (TR)
    df['HL'] = df['High'] - df['Low']
    df['HC'] = abs(df['High'] - df['Close'].shift())
    df['LC'] = abs(df['Low'] - df['Close'].shift())
    df['TR'] = np.maximum.reduce([df['HL'], df['HC'], df['LC']])
    
    # Calculate Average True Range (ATR)
    df['ATR'] = df['TR'].rolling(window=period).mean()
    
    # Initial SuperTrend values
    df['SuperTrend'] = 0.0
    
    # Calculate SuperTrend for uptrend
    df['UpperBand'] = df['High'] - multiplier * df['ATR']
    df.loc[df['Adj Close'] > df['UpperBand'], 'SuperTrend'] = df['UpperBand']
    
    # Calculate SuperTrend for downtrend
    df['LowerBand'] = df['Low'] + multiplier * df['ATR']
    df.loc[df['Adj Close'] < df['LowerBand'], 'SuperTrend'] = df['LowerBand']
    
    return df

# Download historical data using yfinance
symbol = 'AAPL'
start_date = '2022-01-01'
end_date = '2023-01-01'
data = yf.download(symbol, start=start_date, end=end_date)

print(data.keys())
# Calculate SuperTrend values
super_trend_data = calculate_super_trend(data)

super_trend_data.to_csv("super_trend_cal.csv",  index = False)
# Plotting
plt.figure(figsize=(10, 5))
plt.plot(super_trend_data['Adj Close'], label='Close Price', linewidth=1)
plt.plot(super_trend_data['SuperTrend'], label='SuperTrend', color='orange', linewidth=2)
plt.plot(super_trend_data['UpperBand'], label='UpperBand', linestyle='--', color='red', alpha=0.5)
plt.plot(super_trend_data['LowerBand'], label='LowerBand', linestyle='--', color='green', alpha=0.5)

plt.title(f'{symbol} SuperTrend Indicator')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()
