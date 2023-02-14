import os
import sqlite3
from connect_discord.discord_controller import DiscordBot


class desktopWin:
    def __init__(self, BASE_DIR, DISCORD_TOKEN):
        self.BASE_DIR = BASE_DIR
        self.DISCORD_TOKEN = DISCORD_TOKEN
        self.discord = DiscordBot(user=None)
        self.start()

    def start(self):
        self.discord.run(self.DISCORD_TOKEN)

    def start_connect_discord(self):
        pass
