import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from core import User

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="-", intents=intents)


user = User()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    print(message.author, ":", message.content)
    if message.author == client.user:
        return

    message_text = message.content
    if message_text.startswith('new goal'):
        msg = await client.wait_for('message',
                                    check=lambda m: m.channel == message.channel and m.author.id == message.author.id)
        user.new_goal(msg.content)
        await message.channel.send("Цель добавлена.")
    elif message_text.startswith('get goals'):
        goals = user.get_goals()
        transform_goals = "Ваше цели:\n"
        if goals:
            for i in goals:
                transform_goals += f"*{i}\n"
        else:
            transform_goals = "У вас пока нет целей. Добавьте их с помощью new goal"
        await message.channel.send(transform_goals)

    await message.channel.send("Извини не понял твоего вопроса")


client.run(TOKEN)
