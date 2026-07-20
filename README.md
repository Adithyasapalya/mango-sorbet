# ChronosAI – AI Multi-Agent Financial Intelligence Platform

> An AI-powered Multi-Agent Financial Intelligence Platform that combines real-time stock market data, technical analysis, machine learning, financial news, sentiment analysis, autonomous trading simulation, and local Large Language Models (LLMs) to generate intelligent investment recommendations and market insights.

---

## Overview

ChronosAI is an intelligent financial analytics platform designed to help users analyze the stock market through AI-driven insights and autonomous agents.

The platform combines information from:

- Real-time Stock Market Data
- Financial News
- Technical Indicators
- Machine Learning Predictions
- Local Large Language Models (Ollama + Llama 3)

The system downloads historical stock data, analyzes market trends, predicts future prices, evaluates market sentiment from financial news, generates Buy/Hold/Sell recommendations, simulates trading decisions, and provides AI-generated investment insights.

---

## Features

- Real-time Stock Market Analysis
- Top US Stock Tracking
- Interactive Candlestick Charts
- Historical Market Analysis
- RSI Indicator
- Moving Average Analysis
- Bull/Bear Market Detection
- Machine Learning Price Prediction
- Financial News Aggregation
- News Sentiment Analysis
- Multi-Currency Stock Price Conversion
- AI Buy / Hold / Sell Recommendation Engine
- Autonomous Trading Simulation
- AI-generated Financial Insights using Ollama (Llama 3)
- Multi-Agent Financial Workflow
- Interactive Streamlit Dashboard
- Dark / Light Theme Support

---

## Project Workflow

```text
                 User

                  │
                  ▼

          Select Stock

                  │
                  ▼

        Download Market Data

                  │
      ┌───────────┴────────────┐
      ▼                        ▼

Technical Indicators      Financial News

      │                        │
      ▼                        ▼

 RSI & Moving Avg      Sentiment Analysis

      │                        │
      └───────────┬────────────┘
                  ▼

      Machine Learning Prediction

                  │
                  ▼

     Autonomous Trading Simulation

                  │
                  ▼

     Hermes Financial AI Agent

          (Ollama + Llama 3)

                  │
                  ▼

    AI Investment Recommendation

                  │
                  ▼

      Interactive Dashboard
```

---

## Project Structure

```text
ChronosAI/

│
├── app.py
├── orchestrator.py
├── requirements.txt
├── README.md
│
├── agents/
│   ├── hermes_financial_agent.py
│   ├── stock_agent.py
│   ├── news_agent.py
│   ├── prediction_agent.py
│   └── trading_agent.py
│
├── analysis/
│   ├── predictor.py
│   ├── recommender.py
│   └── sentiment.py
│
├── news/
│   └── news_fetcher.py
│
├── tools/
│   └── financial_tools.py
│
├── assets/
│
└── screenshots/
```

---

## Technologies Used

- Python 3.11+
- Streamlit
- Pandas
- NumPy
- Plotly
- Scikit-learn
- yfinance
- NewsAPI
- TextBlob
- Forex-Python
- Ollama
- Llama 3
- Requests

---

## Installation

### Prerequisites

- Python 3.11+
- pip
- Ollama

Clone the repository

```bash
git clone https://github.com/<your-username>/ChronosAI.git

cd ChronosAI
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Install Ollama and pull the Llama 3 model.

```bash
ollama pull llama3
```

Create a `.env` file.

```env
NEWS_API_KEY=your_newsapi_key
```

---

## Running the Application

Start Ollama

```bash
ollama run llama3
```

Launch the Streamlit dashboard

```bash
streamlit run app.py
```

---

## Dashboard

The application provides:

- Interactive candlestick charts
- Historical stock analysis
- Technical indicators
- RSI visualization
- Machine learning price prediction
- Bull/Bear market detection
- Financial news aggregation
- News sentiment analysis
- Currency conversion
- Buy / Hold / Sell recommendation engine
- Autonomous trading simulation
- AI-generated financial reasoning

---

## Processing Pipeline

### 1. Data Collection

- Fetch historical stock data
- Retrieve OHLC prices
- Download company information

---

### 2. Technical Analysis

Calculates:

- RSI
- Moving Average
- Trend Analysis
- Bull/Bear Detection

---

### 3. Machine Learning

Generates:

- Future Price Prediction
- Trend Forecast
- Market Projection

---

### 4. News Intelligence

- Fetch latest financial news
- Analyze article sentiment
- Generate overall market sentiment

---

### 5. AI Financial Agent

The Hermes Financial Agent combines:

- Market Trends
- Technical Indicators
- News Sentiment
- Price Prediction
- Trading Simulation

to generate:

- Financial Summary
- Investment Insights
- Buy / Hold / Sell Recommendation
- Risk Assessment

---

## Outputs

```text
Interactive Dashboard

Candlestick Charts

Technical Indicators

RSI Graph

Price Prediction

Latest Financial News

Sentiment Analysis

Trading Simulation

AI Financial Insights
```

---

## Future Improvements

- Portfolio Management
- Portfolio Optimization
- Reinforcement Learning Trading Agent
- Risk Management Engine
- Cryptocurrency Support
- ETF Analysis
- Options Analytics
- Economic Indicators
- Earnings Calendar
- Voice Assistant
- Docker Support
- Kubernetes Deployment
- Cloud Deployment
- Multi-LLM Support

---

## Contributing

Contributions are welcome.

Feel free to fork the repository, create a feature branch, and submit a pull request.

---

## License

This project is licensed under the MIT License.

---

## Author

**Adithya Ashok Sapalya**