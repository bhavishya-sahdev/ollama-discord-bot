from client import ollamaClient
from discord import Message
import json

async def list_models(message: Message):
    message.channel.typing()
    res = await ollamaClient.list()
    res = "```JSON\n" + json.dumps(res, indent=2) + "```"
    await message.reply(res)