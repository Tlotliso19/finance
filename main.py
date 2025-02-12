import streamlit as st
from components.sidebar import render_sidebar
from components.dashboard import render_dashboard
import utils.data_fetcher as data_fetcher
from utils.database import init_db, get_db, Portfolio, Asset
from sqlalchemy.orm import Session
import contextlib

st.set_page_config(
    page_title="Financial Risk Analysis Platform",
    page_icon="📈",
    layout="wide"
)

# Initialize database
init_db()

def get_or_create_portfolio(db: Session) -> Portfolio:
    """Get the default portfolio or create if it doesn't exist"""
    portfolio = db.query(Portfolio).first()
    if not portfolio:
        portfolio = Portfolio(name="My Portfolio")
        db.add(portfolio)
        db.commit()
        db.refresh(portfolio)
    return portfolio

def main():
    # Get database session
    with contextlib.contextmanager(get_db)() as db:
        # Get or create default portfolio
        portfolio = get_or_create_portfolio(db)

        # Page title and description
        st.title("Financial Risk Analysis Platform")

        # Render sidebar and get user inputs
        selected_view, portfolio_updates = render_sidebar(db, portfolio)

        # Convert portfolio to dict format for dashboard
        portfolio_dict = {
            asset.symbol: {
                'value': asset.value,
                'info': {
                    'name': asset.name,
                    'sector': asset.sector,
                    'currency': asset.currency
                }
            }
            for asset in portfolio.assets
        }

        # Render main dashboard
        render_dashboard(selected_view, portfolio_dict)

if __name__ == "__main__":
    main()