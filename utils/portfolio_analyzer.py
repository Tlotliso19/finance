import pandas as pd
import numpy as np
from utils.risk_calculator import *
from utils.data_fetcher import get_historical_data, get_market_index

def analyze_portfolio(portfolio):
    """Analyze portfolio and calculate risk metrics"""
    if not portfolio:
        return {
            'total_value': 0,
            'volatility': 0,
            'beta': 0,
            'sharpe': 0,
            'var_95': 0,
            'returns': 0
        }

    # Get historical data for all assets
    historical_data = {}
    weights = {}
    total_value = sum(asset['value'] for asset in portfolio.values())

    # If total value is 0, return default metrics
    if total_value == 0:
        return {
            'total_value': 0,
            'volatility': 0,
            'beta': 0,
            'sharpe': 0,
            'var_95': 0,
            'returns': 0
        }

    for symbol, asset in portfolio.items():
        historical_data[symbol] = get_historical_data(symbol)
        weights[symbol] = asset['value'] / total_value

    # Calculate portfolio returns
    if not historical_data:
        return {
            'total_value': total_value,
            'volatility': 0,
            'beta': 0,
            'sharpe': 0,
            'var_95': 0,
            'returns': 0
        }

    first_symbol = list(portfolio.keys())[0]
    portfolio_returns = pd.Series(0, index=historical_data[first_symbol].index)

    for symbol in portfolio:
        if historical_data[symbol] is not None:
            returns = historical_data[symbol]['Close'].pct_change()
            portfolio_returns += returns * weights[symbol]

    # Get market data
    market_data = get_market_index()
    market_returns = market_data['Close'].pct_change() if market_data is not None else pd.Series(0, index=portfolio_returns.index)

    # Calculate risk metrics
    clean_returns = portfolio_returns.dropna()
    analysis = {
        'total_value': total_value,
        'volatility': calculate_volatility(clean_returns),
        'beta': calculate_beta(clean_returns, market_returns.dropna()),
        'sharpe': calculate_sharpe_ratio(clean_returns),
        'var_95': calculate_var(clean_returns),
        'returns': clean_returns.mean() * 252  # Annualized returns
    }

    return analysis