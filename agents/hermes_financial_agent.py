import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

SYSTEM_PROMPT = """
You are ChronosAI.

You are an autonomous financial analyst AI.

Your responsibilities:
- analyze stocks
- analyze market trends
- analyze predictions
- analyze risk
- provide investment recommendations
- explain reasoning clearly

You must provide:
- concise analysis
- financial insights
- buy/sell/hold recommendation
- risk awareness
"""

def ask_financial_agent(prompt):

    final_prompt = f"""
    {SYSTEM_PROMPT}

    USER REQUEST:
    {prompt}
    """

    try:

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3",
                "prompt": final_prompt,
                "stream": False
            }
        )

        result = response.json()

        return result["response"]

    except Exception as e:

        return f"AI Agent Error: {str(e)}"