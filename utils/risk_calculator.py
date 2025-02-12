import numpy as np
from scipy import stats

def calculate_volatility(returns, annualize=True):
    """Calculate volatility of returns"""
    vol = np.std(returns)
    if annualize:
        vol = vol * np.sqrt(252)  # Annualize daily volatility
    return vol

def calculate_beta(stock_returns, market_returns):
    """Calculate beta relative to market"""
    covariance = np.cov(stock_returns, market_returns)[0][1]
    market_variance = np.var(market_returns)
    return covariance / market_variance

def calculate_sharpe_ratio(returns, risk_free_rate=0.02):
    """Calculate Sharpe ratio"""
    excess_returns = returns.mean() * 252 - risk_free_rate
    volatility = calculate_volatility(returns)
    return excess_returns / volatility

def calculate_var(returns, confidence_level=0.95):
    """Calculate Value at Risk"""
    return np.percentile(returns, (1 - confidence_level) * 100)

def get_risk_rating(volatility):
    """Convert volatility to risk rating"""
    if volatility < 0.15:
        return "Low"
    elif volatility < 0.25:
        return "Medium"
    else:
        return "High"
