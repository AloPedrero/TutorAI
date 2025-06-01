from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Initialize client
client = OpenAI(
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

# System prompt to set context
messages = [
    {
        "role": "system",
        "content": """You are an intelligent AI-powered educational assistant that acts as a personalized virtual tutor.
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

print("🧠 Start chatting with your AI tutor (type 'exit' to quit):\n")

while True:
    user_input = input("📝 You: ")
    
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Exiting the chat. Bye!")
        break

    # Append user message
    messages.append({"role": "user", "content": user_input})

    # Get model response
    response = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=messages
    )

    assistant_reply = response.choices[0].message.content.strip()

    # Append assistant response to history
    messages.append({"role": "assistant", "content": assistant_reply})

    print("\n🤖 Tutor:", assistant_reply, "\n")
