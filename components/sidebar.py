import streamlit as st
from utils.data_fetcher import get_stock_info

def render_sidebar():
    """Render sidebar with portfolio management options"""
    st.sidebar.title("Portfolio Management")
    
    # View selection
    selected_view = st.sidebar.selectbox(
        "Select View",
        ["Dashboard", "Risk Analysis", "Recommendations"]
    )
    
    # Portfolio management
    st.sidebar.subheader("Portfolio Composition")
    
    # Add new asset
    new_symbol = st.sidebar.text_input("Add Asset (Symbol)").upper()
    portfolio_updates = {}
    
    if new_symbol:
        info = get_stock_info(new_symbol)
        if info:
            value = st.sidebar.number_input(
                f"Investment value in {info['currency']}",
                min_value=0.0
            )
            if st.sidebar.button("Add to Portfolio"):
                portfolio_updates[new_symbol] = {
                    'value': value,
                    'info': info
                }
    
    # Display current portfolio
    if st.session_state.get('portfolio'):
        st.sidebar.subheader("Current Holdings")
        for symbol, data in st.session_state.portfolio.items():
            st.sidebar.text(f"{symbol}: ${data['value']:,.2f}")
    
    return selected_view, portfolio_updates
