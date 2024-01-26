import chainlit as cl
from src.llm import ask_bot,messages

@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    #response= ask_bot(messages,model="gpt-3.5-turbo",tempurature=0)
    response= ask_bot(messages,model="gpt-3.5-turbo")
    messages.append({"role":"user", "content":message.content})
    message.append({"role":"assistant", "content":response})

    # Send a response back to the user
    await cl.Message(
        #content=f"Received: {message.content}",
        content=response
    ).send()

