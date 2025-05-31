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

# Initialize message history
messages = []

print("🧠 Start chatting with the model (type 'exit' to quit):\n")

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

    print("\n🤖 Assistant:", assistant_reply, "\n")