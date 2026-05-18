import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_response(prompt, model="llama3"):

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]

    except Exception as e:
        return f"LLM Error: {str(e)}"