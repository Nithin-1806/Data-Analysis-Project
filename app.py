import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit App Title
st.title("📈 Real-Time Stock Market Analysis")

# List of Popular Stock Symbols
stock_symbols = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Google": "GOOGL",
    "Amazon": "AMZN",
    "Tesla": "TSLA",
    "NVIDIA": "NVDA",
    "Meta (Facebook)": "META",
    "Netflix": "NFLX",
    "IBM": "IBM",
    "Intel": "INTC",
}

# Sidebar: Stock Selection Dropdown
st.sidebar.header("🔍 Select a Stock")
selected_stock = st.sidebar.selectbox("Choose a stock", list(stock_symbols.keys()))

# Fetch Real-Time Data
symbol = stock_symbols[selected_stock]
stock = yf.Ticker(symbol)

# Get Stock Information
stock_info = stock.info
st.write(f"### {selected_stock} ({symbol}) Stock Overview")

# Display Latest Stock Price
current_price = stock_info.get("currentPrice", "N/A")
st.metric(label="📌 Current Price", value=f"${current_price}")

# Fetch Historical Data
st.write("### 📊 Stock Price Trend (Last 6 Months)")
hist_data = stock.history(period="6mo")

# Plot Closing Prices
fig, ax = plt.subplots()
ax.plot(hist_data.index, hist_data["Close"], color="blue", marker="o", linestyle="-", linewidth=2)
ax.set_xlabel("Date")
ax.set_ylabel("Closing Price")
ax.set_title(f"Stock Price Trend for {selected_stock}")
plt.xticks(rotation=45)
st.pyplot(fig)

# Additional Stock Information
st.write("### ℹ️ Stock Details")
st.write(f"**Market Cap:** {stock_info.get('marketCap', 'N/A')}")
st.write(f"**52-Week High:** ${stock_info.get('fiftyTwoWeekHigh', 'N/A')}")
st.write(f"**52-Week Low:** ${stock_info.get('fiftyTwoWeekLow', 'N/A')}")
st.write(f"**Sector:** {stock_info.get('sector', 'N/A')}")
st.write(f"**Industry:** {stock_info.get('industry', 'N/A')}")
st.write(f"**Company Website:** [{stock_info.get('website', 'N/A')}]({stock_info.get('website', '#')})")

# Footer
st.markdown("---")
st.markdown("📌 **Disclaimer:** Data fetched in real-time from Yahoo Finance. Not for financial decision-making.")
