import streamlit as st
from utils.portfolio_analyzer import analyze_portfolio
from components.charts import plot_portfolio_composition, plot_historical_performance

def render_dashboard(selected_view, portfolio):
    """Render main dashboard content"""
    if not portfolio:
        st.info("Please add assets to your portfolio using the sidebar.")
        return
    
    # Get portfolio analysis
    analysis = analyze_portfolio(portfolio)
    
    if selected_view == "Dashboard":
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Portfolio Value", f"${analysis['total_value']:,.2f}")
        with col2:
            st.metric("Portfolio Beta", f"{analysis['beta']:.2f}")
        with col3:
            st.metric("Annual Volatility", f"{analysis['volatility']*100:.1f}%")
        
        # Portfolio composition chart
        st.subheader("Portfolio Composition")
        plot_portfolio_composition(portfolio)
        
        # Historical performance
        st.subheader("Historical Performance")
        plot_historical_performance(portfolio)
        
    elif selected_view == "Risk Analysis":
        st.subheader("Risk Metrics")
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Sharpe Ratio", f"{analysis['sharpe']:.2f}")
            st.metric("Value at Risk (95%)", f"{analysis['var_95']*100:.1f}%")
        
        with col2:
            st.metric("Expected Annual Return", f"{analysis['returns']*100:.1f}%")
            risk_level = "High" if analysis['volatility'] > 0.25 else "Medium" if analysis['volatility'] > 0.15 else "Low"
            st.metric("Risk Level", risk_level)
            
    elif selected_view == "Recommendations":
        st.subheader("Investment Recommendations")
        
        risk_level = "High" if analysis['volatility'] > 0.25 else "Medium" if analysis['volatility'] > 0.15 else "Low"
        
        recommendations = {
            "High": "Consider reducing exposure to volatile assets and adding more stable, defensive stocks.",
            "Medium": "Your portfolio has a balanced risk profile. Consider maintaining current allocation.",
            "Low": "You might want to consider adding some growth assets to potentially increase returns."
        }
        
        st.write(recommendations[risk_level])
