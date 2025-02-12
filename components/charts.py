import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from utils.data_fetcher import get_historical_data

def plot_portfolio_composition(portfolio):
    """Plot portfolio composition pie chart"""
    labels = list(portfolio.keys())
    values = [asset['value'] for asset in portfolio.values()]
    
    fig = px.pie(
        values=values,
        names=labels,
        title="Portfolio Allocation"
    )
    st.plotly_chart(fig, use_container_width=True)

def plot_historical_performance(portfolio):
    """Plot historical performance of portfolio"""
    # Get historical data
    historical_data = {}
    total_value = sum(asset['value'] for asset in portfolio.values())
    
    for symbol, asset in portfolio.items():
        weight = asset['value'] / total_value
        df = get_historical_data(symbol)
        if df is not None:
            historical_data[symbol] = df['Close'] * weight

    if not historical_data:
        st.error("Could not fetch historical data")
        return
    
    # Create cumulative performance chart
    fig = go.Figure()
    
    for symbol in historical_data:
        fig.add_trace(
            go.Scatter(
                x=historical_data[symbol].index,
                y=historical_data[symbol].values,
                name=symbol,
                mode='lines'
            )
        )
    
    fig.update_layout(
        title="Historical Performance",
        xaxis_title="Date",
        yaxis_title="Value ($)",
        hovermode='x unified'
    )
    
    st.plotly_chart(fig, use_container_width=True)
