import os
import discord


class DiscordBot(discord.Client):
    def __init__(self, user):
        self.user_id = user
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)

        @self.event
        async def on_message(message):
            message_author_id = message.author.id  # 813350277812846623
            message_author = message.author  # Solo_Leveling#2053
            message_text = message.content  # текст сообщения отправленный пользователем
            print(self.user_id)

    async def on_ready(self):
        print(f"Bot {self.user.display_name} is connected to server.")

# bot = DiscordBot()
# TOKEN = os.getenv("TOKEN")
# bot.run(TOKEN)
