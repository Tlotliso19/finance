import numpy as np
from scipy import stats

def calculate_volatility(returns, annualize=True):
    """Calculate volatility of returns"""
    if len(returns) == 0:
        return 0
    vol = np.std(returns)
    if annualize:
        vol = vol * np.sqrt(252)  # Annualize daily volatility
    return vol

def calculate_beta(stock_returns, market_returns):
    """Calculate beta relative to market"""
    if len(stock_returns) == 0 or len(market_returns) == 0:
        return 0

    # Ensure arrays are of the same length
    min_length = min(len(stock_returns), len(market_returns))
    stock_returns = stock_returns[-min_length:]
    market_returns = market_returns[-min_length:]

    if min_length == 0:
        return 0

    try:
        covariance = np.cov(stock_returns, market_returns)[0][1]
        market_variance = np.var(market_returns)
        return covariance / market_variance if market_variance != 0 else 0
    except:
        return 0

def calculate_sharpe_ratio(returns, risk_free_rate=0.02):
    """Calculate Sharpe ratio"""
    if len(returns) == 0:
        return 0
    try:
        excess_returns = returns.mean() * 252 - risk_free_rate
        volatility = calculate_volatility(returns)
        return excess_returns / volatility if volatility != 0 else 0
    except:
        return 0

def calculate_var(returns, confidence_level=0.95):
    """Calculate Value at Risk"""
    if len(returns) == 0:
        return 0
    try:
        return np.percentile(returns, (1 - confidence_level) * 100)
    except:
        return 0

def get_risk_rating(volatility):
    """Convert volatility to risk rating"""
    if volatility < 0.15:
        return "Low"
    elif volatility < 0.25:
        return "Medium"
    else:
        return "High"