import pandas as pd
import numpy as np
from utils.risk_calculator import *
from utils.data_fetcher import get_historical_data, get_market_index

def analyze_portfolio(portfolio):
    """Analyze portfolio and calculate risk metrics"""
    if not portfolio:
        return None
    
    # Get historical data for all assets
    historical_data = {}
    weights = {}
    total_value = sum(asset['value'] for asset in portfolio.values())
    
    for symbol, asset in portfolio.items():
        historical_data[symbol] = get_historical_data(symbol)
        weights[symbol] = asset['value'] / total_value
    
    # Calculate portfolio returns
    portfolio_returns = pd.Series(0, index=historical_data[list(portfolio.keys())[0]].index)
    for symbol in portfolio:
        returns = historical_data[symbol]['Close'].pct_change()
        portfolio_returns += returns * weights[symbol]
    
    # Get market data
    market_data = get_market_index()
    market_returns = market_data['Close'].pct_change()
    
    # Calculate risk metrics
    analysis = {
        'total_value': total_value,
        'volatility': calculate_volatility(portfolio_returns.dropna()),
        'beta': calculate_beta(portfolio_returns.dropna(), market_returns.dropna()),
        'sharpe': calculate_sharpe_ratio(portfolio_returns.dropna()),
        'var_95': calculate_var(portfolio_returns.dropna()),
        'returns': portfolio_returns.mean() * 252  # Annualized returns
    }
    
    return analysis
