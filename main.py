import discord
import asyncio
import random
import os

TOKEN = os.environ["DISCORD_TOKEN"]
CHANNEL_ID = int(os.environ["CHANNEL_ID"])

questions = [
    "Что бы ты выбрал: летать или быть невидимым?",
    "Если бы ты мог переместиться в любое время — куда?",
    "Какой суперспособностью ты бы хотел обладать?",
    "Какое у тебя самое яркое воспоминание из детства?",
    "Что бы ты сказал себе 5 лет назад?"
]

intents = discord.Intents.default()

class DailyBot(discord.Client):
    async def setup_hook(self):
        # Запускаем задачу после полной инициализации
        self.bg_task = self.loop.create_task(self.send_daily_question())

    async def on_ready(self):
        print(f"✅ Бот вошёл как {self.user}")

    async def send_daily_question(self):
        await self.wait_until_ready()
        channel = self.get_channel(CHANNEL_ID)
        while True:
            question = random.choice(questions)
            await channel.send(f"❓ *Дневной вопрос:*\n{question}")
            await asyncio.sleep(86400)  # 24 часа

client = DailyBot(intents=intents)
client.run(TOKEN)