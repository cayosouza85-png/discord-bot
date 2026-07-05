import discord
import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logado como {client.user}")

    canal = client.get_channel(1522012868487151810)
    if canal:
        await canal.send("🤖 Olá! Estou online!")

client.run(TOKEN)
