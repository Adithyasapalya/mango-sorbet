import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go

from forex_python.converter import (
    CurrencyRates,
    RatesNotAvailableError
)

from orchestrator import (
    ChronosOrchestrator
)

from tools.financial_tools import (
    calculate_rsi
)

from analysis.recommender import (
    calculate_recommendation
)

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------
st.set_page_config(
    page_title="ChronosAI Financial Intelligence",
    layout="wide"
)

# ------------------------------------------------
# STOCK DICTIONARY
# ------------------------------------------------
stocks = {

    "Apple (AAPL)": "AAPL",
    "Microsoft (MSFT)": "MSFT",
    "Google (GOOGL)": "GOOGL",
    "Amazon (AMZN)": "AMZN",
    "Nvidia (NVDA)": "NVDA",
    "Meta (META)": "META",
    "Tesla (TSLA)": "TSLA",
    "Netflix (NFLX)": "NFLX",
    "AMD (AMD)": "AMD",
    "JPMorgan Chase (JPM)": "JPM",

    "Visa (V)": "V",
    "Mastercard (MA)": "MA",
    "Intel (INTC)": "INTC",
    "Oracle (ORCL)": "ORCL",
    "Coca-Cola (KO)": "KO",

    "PepsiCo (PEP)": "PEP",
    "Disney (DIS)": "DIS",
    "Nike (NKE)": "NKE",
    "Adobe (ADBE)": "ADBE",
    "Salesforce (CRM)": "CRM",

    "Monster Beverage (MNST)": "MNST",
    "Celsius Holdings (CELH)": "CELH"
}

# ------------------------------------------------
# CUSTOM STYLE
# ------------------------------------------------
st.markdown(
    """
    <style>

    .top-bar {
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------------------------------
# HEADER
# ------------------------------------------------
st.title(
    "ChronosAI Financial Intelligence Dashboard"
)

st.markdown("---")

# ------------------------------------------------
# INITIALIZE ORCHESTRATOR
# ------------------------------------------------
orchestrator = ChronosOrchestrator()

# ------------------------------------------------
# TOP CONTROLS
# ------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:

    selected_stock_name = st.selectbox(
        "Select Stock",
        list(stocks.keys())
    )

with col2:

    period_label = st.selectbox(
        "Select Period",
        [
            "1 Month",
            "3 Months",
            "6 Months",
            "1 Year",
            "2 Years",
            "5 Years",
            "Max"
        ]
    )

period_mapping = {

    "1 Month": "1mo",
    "3 Months": "3mo",
    "6 Months": "6mo",
    "1 Year": "1y",
    "2 Years": "2y",
    "5 Years": "5y",
    "Max": "max"
}

period = period_mapping.get(
    period_label,
    "1mo"
)

with col3:

    currency_options = {

        "USD - United States Dollar": "USD",
        "EUR - Euro": "EUR",
        "GBP - British Pound Sterling": "GBP",
        "INR - Indian Rupee": "INR",
        "JPY - Japanese Yen": "JPY",
        "AUD - Australian Dollar": "AUD",
        "CAD - Canadian Dollar": "CAD",
        "CHF - Swiss Franc": "CHF",
        "CNY - Chinese Yuan": "CNY",
        "SGD - Singapore Dollar": "SGD",
        "NZD - New Zealand Dollar": "NZD",
        "TRY - Turkish Lira": "TRY",
        "ZAR - South African Rand": "ZAR",
        "HKD - Hong Kong Dollar": "HKD",
        "BRL - Brazilian Real": "BRL",
        "RUB - Russian Ruble": "RUB",
        "SEK - Swedish Krona": "SEK",
        "NOK - Norwegian Krone": "NOK",
        "MXN - Mexican Peso": "MXN",
        "KRW - South Korean Won": "KRW"
    }

    selected_currency_label = st.selectbox(
        "Currency",
        list(currency_options.keys())
    )

    currency = currency_options[
        selected_currency_label
    ]

with col4:

    if "theme_toggle" not in st.session_state:

        st.session_state.theme_toggle = True

    subcol1, subcol2 = st.columns(
        [0.1, 0.9]
    )

    with subcol1:

        theme_toggle = st.checkbox(
            "",
            value=st.session_state.theme_toggle,
            key="theme_toggle"
        )

    theme_label = (
        "Dark Mode"
        if theme_toggle
        else "Light Mode"
    )

    theme_text_color = (
        "#FFFFFF"
        if theme_toggle
        else "#000000"
    )

    with subcol2:

        st.markdown(
            f"""
            <div style='
            display:inline-block;
            color:{theme_text_color};
            margin-top:10px;
            margin-left:-12px;
            font-weight:normal;
            '>
            {theme_label}
            </div>
            """,
            unsafe_allow_html=True
        )

# ------------------------------------------------
# THEME
# ------------------------------------------------
if theme_toggle:

    background = "#0E1117"
    text_color = "white"
    card_color = "#161B22"

else:

    background = "#FFFFFF"
    text_color = "#000000"
    card_color = "#F3F3F3"

# ------------------------------------------------
# APPLY THEME
# ------------------------------------------------
st.markdown(
    f"""
    <style>

    .stApp {{
        background-color: {background};
        color: {text_color};
    }}

    div[data-baseweb="select"] > div {{
        background-color: {card_color};
        color: {text_color};
    }}

    .stSelectbox label {{
        color: {text_color} !important;
        font-weight: bold;
    }}

    .stMarkdown {{
        color: {text_color};
    }}

    .stText {{
        color: {text_color};
    }}

    .stRadio label,
    .stCheckbox label,
    div[data-baseweb="checkbox"] label {{
        color: {text_color} !important;
        font-weight: normal;
    }}

    .stToggle label,
    div[data-baseweb="toggle"] label,
    div[data-baseweb="toggle"] span,
    .stToggle {{
        color: {text_color} !important;
        font-weight: bold;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------------------------------
# STOCK SELECTION
# ------------------------------------------------
selected_stock = stocks[
    selected_stock_name
]

# ------------------------------------------------
# ORCHESTRATED ANALYSIS
# ------------------------------------------------
results = orchestrator.run_analysis(
    selected_stock,
    period
)

df = results["df"]

predictions = results["predictions"]

market_trend_result = results["trend"]

trade = results["trade"]

news = results["news"]

ai_response = results["ai_response"]

if df.empty or "Close" not in df.columns:

    st.error(
        "Unable to fetch stock data"
    )

    st.stop()

# ------------------------------------------------
# PRICE METRICS
# ------------------------------------------------
latest_price = df["Close"].iloc[-1]

previous_price = df["Close"].iloc[-2]

change = latest_price - previous_price

percent_change = (
    (change / previous_price) * 100
    if previous_price != 0
    else 0
)

# ------------------------------------------------
# CURRENCY CONVERSION
# ------------------------------------------------
c = CurrencyRates()

converted_price = None

converted_price_label = "N/A"

try:

    converted_price = c.convert(
        "USD",
        currency,
        latest_price
    )

    converted_price_label = (
        f"{converted_price:.2f}"
    )

except RatesNotAvailableError:

    converted_price_label = (
        f"Rate unavailable for {currency}"
    )

except Exception:

    converted_price_label = (
        "Conversion error"
    )

# ------------------------------------------------
# DISPLAY METRICS
# ------------------------------------------------
metric1, metric2, metric3, metric4 = st.columns(4)

metric1.metric(
    "Current Price",
    f"${latest_price:.2f}"
)

metric2.metric(
    f"Price in {selected_currency_label}",
    converted_price_label
)

metric3.metric(
    "Daily Change",
    f"{change:.2f}"
)

metric4.metric(
    "Percent Change",
    f"{percent_change:.2f}%"
)

st.markdown("---")

# ------------------------------------------------
# CANDLESTICK CHART
# ------------------------------------------------
candlestick = go.Figure()

candlestick.add_trace(
    go.Candlestick(
        x=df.index,
        open=df["Open"],
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
        name="Market"
    )
)

candlestick.update_layout(
    title=f"{selected_stock_name} Market Chart",
    height=600
)

st.plotly_chart(
    candlestick,
    use_container_width=True
)

# ------------------------------------------------
# MOVING AVERAGE
# ------------------------------------------------
df["MA5"] = df["Close"].rolling(5).mean()

ma_chart = go.Figure()

ma_chart.add_trace(
    go.Scatter(
        x=df.index,
        y=df["Close"],
        mode="lines",
        name="Close Price"
    )
)

ma_chart.add_trace(
    go.Scatter(
        x=df.index,
        y=df["MA5"],
        mode="lines",
        name="Moving Average"
    )
)

ma_chart.update_layout(
    title="Moving Average Analysis",
    height=500
)

st.plotly_chart(
    ma_chart,
    use_container_width=True
)

# ------------------------------------------------
# RSI
# ------------------------------------------------
rsi = calculate_rsi(df)

df["RSI"] = rsi.values

rsi_chart = go.Figure()

rsi_chart.add_trace(
    go.Scatter(
        x=df.index,
        y=df["RSI"],
        mode="lines",
        name="RSI"
    )
)

rsi_chart.update_layout(
    title="RSI Indicator",
    height=400
)

st.plotly_chart(
    rsi_chart,
    use_container_width=True
)

# ------------------------------------------------
# MARKET TREND
# ------------------------------------------------
if market_trend_result == "Bullish":

    st.success(
        "Bullish Market Detected"
    )

else:

    st.error(
        "Bearish Market Detected"
    )

# ------------------------------------------------
# BUY / SELL RECOMMENDATION
# ------------------------------------------------
recommendation, latest_price, moving_avg = (
    calculate_recommendation(df)
)

st.subheader(
    "AI Recommendation Engine"
)

if recommendation == "BUY":

    st.success(
        f"Recommendation: {recommendation}"
    )

elif recommendation == "SELL":

    st.error(
        f"Recommendation: {recommendation}"
    )

else:

    st.warning(
        f"Recommendation: {recommendation}"
    )

st.write(
    f"Current Price: {latest_price:.2f}"
)

st.write(
    f"Moving Average: {moving_avg:.2f}"
)

# ------------------------------------------------
# AI PREDICTION
# ------------------------------------------------
prediction_chart = go.Figure()

prediction_chart.add_trace(
    go.Scatter(
        x=df.index,
        y=df["Close"],
        mode="lines",
        name="Historical"
    )
)

future_x = list(
    range(
        len(df),
        len(df) + len(predictions)
    )
)

prediction_chart.add_trace(
    go.Scatter(
        x=future_x,
        y=predictions,
        mode="lines",
        name="AI Prediction"
    )
)

prediction_chart.update_layout(
    title="30 Day AI Prediction",
    height=500
)

st.plotly_chart(
    prediction_chart,
    use_container_width=True
)

# ------------------------------------------------
# NEWS & SENTIMENT
# ------------------------------------------------
st.subheader(
    "Latest Market News"
)

sentiments = []

for item in news:

    title = item["title"]

    sentiment = item["sentiment"]

    url = item.get("url")

    sentiments.append(sentiment)

    if url:

        st.markdown(
            f"### <a href='{url}' target='_blank'>{title}</a>",
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"### {title}"
        )

    st.write(
        f"Sentiment: {sentiment}"
    )

    st.markdown("---")

# ------------------------------------------------
# AI RESPONSE
# ------------------------------------------------
st.subheader(
    "ChronosAI Autonomous Analysis"
)

st.write(ai_response)

# ------------------------------------------------
# TRADING SIMULATION
# ------------------------------------------------
st.subheader(
    "Autonomous Trading Simulation"
)

st.write(trade)

# ------------------------------------------------
# RAW DATA
# ------------------------------------------------
with st.expander(
    "View Raw Market Data"
):

    st.dataframe(df)

# ------------------------------------------------
# FOOTER
# ------------------------------------------------
st.markdown("---")

st.caption(
    "Powered By MiroFish and Hermes Agent"
)