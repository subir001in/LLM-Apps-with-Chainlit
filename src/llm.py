from openai import OpenAI
from src.prompt import system_instruction

client = OpenAI()

messages = [
    {"role":"system","content":system_instruction}
]

def ask_bot(messages, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
    model=model,
    messages= messages
    #,tempurature=tempurature
    )
    return response['choices'][0]['message']['content']