# necrochopics/config.py

API_KEY = "groq_api"
MODEL = "llama3-8b-8192"
ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"
TEMPERATURE = 0.7
MAX_RETRY = 3
MAX_HISTORY = 4

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        " fill anything prompt you want."
    )
}
