import openai
from api_key import chat_gpt_api_key

openai.api_key = chat_gpt_api_key

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": ""},
        {"role": "assistant", "content": ""},
        {"role": "user", "content": ""},
    ]
)

print(response)
