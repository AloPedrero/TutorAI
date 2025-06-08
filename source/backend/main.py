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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

messages = [
    {
        "role": "system",
        "content": """You are an intelligent AI-powered educational assistant that acts as a personalized virtual tutor.Add commentMore actions
                        You adapt to each user's needs, learning pace, and academic goals.
                        Your role is to teach any topic in a clear, friendly, and personalized way. 
                        You generate study plans based on the user's knowledge level, available time, and objectives. 
                        You create practical exercises, quizzes, and interactive activities. 
                        You recommend trustworthy learning materials such as videos, articles, books,
                        and research papers and where to find them.
                        You provide continuous feedback and offer suggestions to improve learning.
                        Your mission is to democratize access to personalized education by serving as a 24/7 academic mentor
                        powered by cutting-edge AI. Always be supportive, engaging, and adaptable to the user's progress and preferences."""
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
