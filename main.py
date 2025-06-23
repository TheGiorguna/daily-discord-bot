import discord
import random
import asyncio
import os

TOKEN = os.environ["DISCORD_TOKEN"]
CHANNEL_ID = 123456789012345678  # 🔁 Замени на ID своего канала

intents = discord.Intents.default()
client = discord.Client(intents=intents)

questions = [
    "Что бы ты выбрал: летать или быть невидимым?",
    "Если бы ты мог переместиться в любое время — куда?",
    "Какой суперспособностью ты бы хотел обладать?",
    "Какое у тебя самое яркое воспоминание из детства?",
    "Что бы ты сказал себе 5 лет назад?"
]

async def send_daily_question():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)
    while not client.is_closed():
        question = random.choice(questions)
        await channel.send(f"❓ *Дневной вопрос:*\n{question}")
        await asyncio.sleep(86400)  # 24 часа

@client.event
async def on_ready():
    print(f'Бот вошёл как {client.user}')

client.loop.create_task(send_daily_question())
client.run(TOKEN)