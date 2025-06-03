from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

app = FastAPI()

# Permitir acceso desde tu frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringir esto a ["http://localhost:5500"] por seguridad
    allow_methods=["*"],
    allow_headers=["*"],
)

# Para manejar los mensajes
class Message(BaseModel):
    message: str

messages = [
    {
        "role": "system",
        "content": """You are an intelligent AI-powered educational assistant..."""
    }
]

@app.post("/chat")
async def chat_endpoint(message: Message):
    messages.append({"role": "user", "content": message.message})
    
    response = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=messages
    )

    reply = response.choices[0].message.content.strip()
    messages.append({"role": "assistant", "content": reply})
    
    return {"response": reply}
