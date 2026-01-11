import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

#  Page Config
st.set_page_config(page_title="Market Intel", layout="wide")

st.title(" Algorithmic Market Intelligence")
st.markdown("---")


st.sidebar.header("Target Asset")
ticker = st.sidebar.text_input("Enter Ticker Symbol (e.g., MSFT, AAPL, BTC-USD)", "MSFT")
period = st.sidebar.selectbox("Time Horizon", ["1mo", "6mo", "1y", "5y"])


with st.spinner('Fetching market data...'):
    data = yf.download(ticker, period=period)

if not data.empty:
    
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    #  Financial Logic: Moving Averages (MA)
    data['MA20'] = data['Close'].rolling(window=20).mean()
    data['MA50'] = data['Close'].rolling(window=50).mean()

    #  Key Metrics Calculation
    current_price = float(data['Close'].iloc[-1])
    previous_price = float(data['Close'].iloc[-2])
    change = current_price - previous_price
    
    col1, col2, col3 = st.columns(3)
    

    col1.metric("Live Price", f"${current_price:,.2f}", f"{change:,.2f}")
    

    ma20_val = data['MA20'].iloc[-1]
    ma50_val = data['MA50'].iloc[-1]
    
    col2.metric("20-Day Avg", f"${ma20_val:,.2f}" if not pd.isna(ma20_val) else "N/A")
    col3.metric("50-Day Avg", f"${ma50_val:,.2f}" if not pd.isna(ma50_val) else "N/A")


    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], name="Price", line=dict(color='royalblue', width=2)))
    fig.add_trace(go.Scatter(x=data.index, y=data['MA20'], name="20d MA", line=dict(dash='dash', color='orange')))
    fig.add_trace(go.Scatter(x=data.index, y=data['MA50'], name="50d MA", line=dict(dash='dot', color='red')))
    
    fig.update_layout(
        title=f"{ticker} Technical Analysis",
        template="plotly_dark",
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
    )
    st.plotly_chart(fig, use_container_width=True)


    with st.expander("View Historical Raw Data"):
        st.dataframe(data.tail(10), use_container_width=True)
else:
    st.error(f"Ticker '{ticker}' not found or no data available for the selected period.")

st.markdown("---")
st.caption("Data provided by yfinance API")