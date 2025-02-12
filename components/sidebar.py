import streamlit as st
from utils.data_fetcher import get_stock_info
from utils.database import Asset
from sqlalchemy.orm import Session

def render_sidebar(db: Session, portfolio):
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
                # Create new asset in database
                new_asset = Asset(
                    portfolio_id=portfolio.id,
                    symbol=new_symbol,
                    value=value,
                    name=info['name'],
                    sector=info.get('sector', 'N/A'),
                    currency=info['currency']
                )
                db.add(new_asset)
                db.commit()
                portfolio_updates[new_symbol] = {
                    'value': value,
                    'info': info
                }

    # Display current portfolio
    st.sidebar.subheader("Current Holdings")
    for asset in portfolio.assets:
        st.sidebar.text(f"{asset.symbol}: ${asset.value:,.2f}")

    return selected_view, portfolio_updates