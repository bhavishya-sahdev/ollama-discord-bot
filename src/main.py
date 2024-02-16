from client import client, init_client
from discord import Message
from commands import chat, list_models, create_model, activate_model

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    

@client.event
async def on_message(message: Message):
    if message.content.startswith("$list"):
        await list_models.list_models(message)
    elif message.content.startswith("$create"):
        await create_model.create_model(message)
    elif message.content.startswith("$activate"):
        await activate_model.activate_model(message)
    else:
        await chat.chat(message)
    
init_client()