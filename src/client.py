import discord
import os
import dotenv
from ollama import AsyncClient

dotenv.load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
context = {}

class Data:
    def __init__(self) -> None:
        self.model = "llama2"

    def update_model(self, model: str):
        self.model = model

data = Data()

ollamaClient = AsyncClient()

def init_client():
    client.run(os.environ.get("DISCORD_TOKEN"))
