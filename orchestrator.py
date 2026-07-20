from agents.hermes_financial_agent import (
    ask_financial_agent
)

from tools.financial_tools import (
    fetch_stock_data,
    predict_stock,
    market_trend,
    simulate_trade
)

from news.news_fetcher import (
    fetch_stock_news
)

from analysis.sentiment import (
    analyze_sentiment
)

# -----------------------------------
# MAIN ORCHESTRATOR
# -----------------------------------
class ChronosOrchestrator:

    def __init__(self):

        print(
            "ChronosAI Initialized"
        )

    # --------------------------------
    # COMPLETE PIPELINE
    # --------------------------------
    def run_analysis(
        self,
        stock,
        period="1y"
    ):

        # FETCH DATA
        df = fetch_stock_data(
            stock,
            period
        )

        # MARKET TREND
        trend = market_trend(df)

        # PREDICTIONS
        predictions = predict_stock(df)

        # TRADE SIMULATION
        trade = simulate_trade(
            df["Close"].iloc[-1],
            predictions[-1]
        )

        # NEWS
        articles = fetch_stock_news(
            stock
        )

        news_results = []

        for article in articles:

            title = article["title"]

            sentiment = analyze_sentiment(
                title
            )

            news_results.append({
                "title": title,
                "sentiment": sentiment
            })

        # HERMES AI
        ai_response = ask_financial_agent(
            f"""
            Analyze {stock}.
            Current trend: {trend}
            Trading simulation: {trade}
            Give investment advice.
            """
        )

        return {

            "df": df,

            "trend": trend,

            "predictions":
            predictions,

            "trade": trade,

            "news":
            news_results,

            "ai_response":
            ai_response
        }