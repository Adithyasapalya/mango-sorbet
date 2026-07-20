import yfinance as yf
import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression

# -----------------------------------
# FETCH STOCK DATA
# -----------------------------------
def fetch_stock_data(
    stock,
    period="1y"
):

    ticker = yf.Ticker(stock)

    df = ticker.history(
        period=period
    )

    return df

# -----------------------------------
# RSI
# -----------------------------------
def calculate_rsi(df):

    delta = df["Close"].diff()

    gain = np.where(
        delta > 0,
        delta,
        0
    )

    loss = np.where(
        delta < 0,
        -delta,
        0
    )

    gain_series = pd.Series(
        gain
    ).rolling(14).mean()

    loss_series = pd.Series(
        loss
    ).rolling(14).mean()

    rs = gain_series / loss_series

    rsi = 100 - (
        100 / (1 + rs)
    )

    return rsi

# -----------------------------------
# MARKET TREND
# -----------------------------------
def market_trend(df):

    moving_avg = df["Close"].rolling(
        20
    ).mean()

    latest_price = df["Close"].iloc[-1]

    latest_ma = moving_avg.iloc[-1]

    if latest_price > latest_ma:

        return "Bullish"

    return "Bearish"

# -----------------------------------
# PREDICTION MODEL
# -----------------------------------
def predict_stock(df):

    prediction_df = df.reset_index()

    prediction_df["Day"] = np.arange(
        len(prediction_df)
    )

    X = prediction_df[["Day"]]

    y = prediction_df["Close"]

    model = LinearRegression()

    model.fit(X, y)

    future_days = np.array(
        range(
            len(prediction_df),
            len(prediction_df) + 30
        )
    ).reshape(-1, 1)

    predictions = model.predict(
        future_days
    )

    return predictions

# -----------------------------------
# TRADING SIMULATION
# -----------------------------------
def simulate_trade(
    current_price,
    future_price,
    capital=10000
):

    shares = capital / current_price

    future_value = shares * future_price

    profit = future_value - capital

    if profit > 0:

        action = "BUY"

    else:

        action = "SELL"

    return {
        "action": action,
        "profit": round(profit, 2),
        "future_value": round(
            future_value,
            2
        )
    }