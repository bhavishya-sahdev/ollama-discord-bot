from discord import Message
from client import data, context
async def activate_model(message: Message):
    args = message.content.split(" ", 1)
    data.update_model(args[1])
    channel_id = str(message.channel.id)
    if channel_id in context:
        context[channel_id]['messages'] = []
    await message.reply(f"Activated {data.model}")