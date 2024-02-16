from discord import Message
from client import client, ollamaClient, context, data
import json

async def chat(message: Message):
    if message.author == client.user:
        return
    if not message.content:
        return
    
    channel_id = str(message.channel.id)
    if not channel_id in context:
        context[channel_id] = {
            "messages": []
        }
    elif len(context[channel_id]['messages']) >= 10:
        context[channel_id]['messages'].pop(0)

    
    content = {
        "author": {"author_name": message.author.name, "author_nick_name": message.author.nick},
        "content": message.content
    }

    context[channel_id]['messages'].append({
        'role': 'user',
        'content': json.dumps(content),
    })

    try: 
        await message.channel.typing()
        response = await ollamaClient.chat(model=data.model, messages=context[channel_id]['messages'])
        context[channel_id]['messages'].append(response['message'])
        await message.reply(response['message']['content'])
    except Exception as e: 
        print(e)