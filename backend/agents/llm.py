import os
from groq import Groq
from dotenv import load_dotenv
from backend.state import AgentState

load_dotenv()

api_key = os.getenv("GROQ_API_KEY") or "gsk_t1hGi6uUiENLsfFzxJLQWGdyb3FYlBsWwjzauQ0RSSB7f4MYy"

client = Groq(api_key=api_key)

def llm_agent(state: AgentState) -> dict:

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system",
             "content": "You are a safe AI assistant."},
            {"role": "user", "content": state["query"]}
        ]
    )

    return {
        "response": response.choices[0].message.content,
        "status": "DONE"
    }