import os
from openai import OpenAI

# Define the conversation messages
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Explain what AI is in simple terms."}
]

client = OpenAI(
    api_key=os.environ.get("API_KEY"),  # This is the default and can be omitted
)

# Make the API request to GPT-4
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-4o",
)

# Print the response content
print(chat_completion)