# Financial Risk Analysis Platform

A comprehensive financial risk analysis platform built with Streamlit, providing advanced portfolio management, real-time stock analysis, and interactive risk assessment tools.

## Features

- Portfolio Management Dashboard
- Real-time Stock Market Data Analysis
- Risk Assessment Tools
- Interactive Data Visualization
- Historical Performance Tracking
- Investment Recommendations

## Tech Stack

- Python 3.11
- Streamlit
- SQLAlchemy (PostgreSQL)
- YFinance for market data
- Plotly for visualizations
- Scipy for statistical analysis

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
- Create a `.env` file with your database configuration
- Required variables: `DATABASE_URL`

3. Run the application:
```bash
streamlit run main.py
```

## Project Structure

- `main.py` - Application entry point
- `components/` - UI components and visualizations
- `utils/` - Helper functions and data processing
- `.streamlit/` - Streamlit configuration

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
