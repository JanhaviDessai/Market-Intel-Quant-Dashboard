# Algorithmic Market Intelligence Dashboard

A real-time financial data engine built to perform technical analysis and time-series visualization on global equities and digital assets.

##  Key Features
- **Live Data Integration:** Leverages the `yfinance` API to fetch real-time market data for any ticker (Stocks, Crypto, Currencies).
- **Algorithmic Indicators:** Automatically calculates and plots **20-day and 50-day Simple Moving Averages (SMA)** to detect bullish/bearish trends.
- **Interactive Visualization:** Uses **Plotly Graph Objects** for high-fidelity, zoomable time-series charts.
- **Dynamic Metrics:** Real-time calculation of price delta and volatility metrics.

##  Data Science Logic
The dashboard utilizes **Rolling Window Functions** in Pandas to compute technical indicators:
- **SMA-20:** Captures short-term momentum.
- **SMA-50:** Identifies long-term structural trends.

##  Tech Stack
- **Language:** Python 3.x
- **Libraries:** Streamlit (UI), Pandas (Data Manipulation), YFinance (API), Plotly (Charts)
- **Deployment:** Architected for cloud hosting on Streamlit Cloud/Azure App Service.

##  How to Run
1. Clone the repo: `git clone https://github.com/USERNAME/Market-Intel-Quant-Dashboard.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Launch app: `streamlit run finance_app.py`
