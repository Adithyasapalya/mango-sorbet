from llm.ollama_client import generate_response


def calculate_recommendation(df):

    latest_price = df["Close"].iloc[-1]

    moving_avg = df["Close"].rolling(window=5).mean().iloc[-1]

    if latest_price > moving_avg:
        recommendation = "BUY"

    elif latest_price < moving_avg:
        recommendation = "SELL"

    else:
        recommendation = "HOLD"

    return recommendation, latest_price, moving_avg


def generate_ai_insight(
    stock,
    recommendation,
    latest_price,
    moving_avg,
    sentiment
):

    prompt = f"""
You are a professional stock market analyst.

Stock: {stock}

Current Price: {latest_price}

Moving Average: {moving_avg}

Market Sentiment: {sentiment}

Recommendation: {recommendation}

Explain:
- current trend
- possible future movement
- market sentiment
- investment risk
- recommendation reasoning

Keep response simple and professional.
"""

    return generate_response(prompt)