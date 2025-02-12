import streamlit as st
from components.sidebar import render_sidebar
from components.dashboard import render_dashboard
import utils.data_fetcher as data_fetcher

st.set_page_config(
    page_title="Financial Risk Analysis Platform",
    page_icon="📈",
    layout="wide"
)

def main():
    # Initialize session state
    if 'portfolio' not in st.session_state:
        st.session_state.portfolio = {}
    
    # Page title and description
    st.title("Financial Risk Analysis Platform")
    
    # Render sidebar and get user inputs
    selected_view, portfolio_updates = render_sidebar()
    
    # Update portfolio if changes made
    if portfolio_updates:
        st.session_state.portfolio.update(portfolio_updates)
    
    # Render main dashboard
    render_dashboard(selected_view, st.session_state.portfolio)

if __name__ == "__main__":
    main()
