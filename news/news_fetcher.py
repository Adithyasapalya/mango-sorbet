from newsapi import NewsApiClient

# Replace with your NewsAPI key
NEWS_API_KEY = "pub_7fe04441f269432f8228956b4e03eaba"

newsapi = NewsApiClient(api_key=NEWS_API_KEY)


def fetch_stock_news(stock):

    try:

        articles = newsapi.get_everything(
            q=stock,
            language="en",
            sort_by="publishedAt",
            page_size=5
        )

        return articles["articles"]

    except Exception as e:

        print("News API Error:", e)

        return []