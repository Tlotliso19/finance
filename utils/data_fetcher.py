import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def get_historical_data(symbol, period='1y'):
    """Fetch historical data from Yahoo Finance"""
    try:
        ticker = yf.Ticker(symbol)
        df = ticker.history(period=period)
        return df
    except Exception as e:
        return None

def get_stock_info(symbol):
    """Get basic stock information"""
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        return {
            'name': info.get('longName', symbol),
            'sector': info.get('sector', 'N/A'),
            'price': info.get('currentPrice', 0),
            'currency': info.get('currency', 'USD'),
            'market_cap': info.get('marketCap', 0)
        }
    except:
        return None

def get_market_index(index_symbol='^GSPC'):
    """Get market index data (S&P 500 by default)"""
    return get_historical_data(index_symbol)
