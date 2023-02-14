# todo Менеджер приложений

import os

from dotenv import load_dotenv, set_key
from notification.main import main as notification
from desktopWin.main import desktopWin

import argparse
import os

# todo Получаем путь до главной папки проекта
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
current_directory = os.getcwd()
set_key('.env', 'BASE_DIR', current_directory)

# todo Функция для добавления запуска через консоль
print('Для остановки приложения нажмите Ctrl+C')
parser = argparse.ArgumentParser(exit_on_error=False)
parser.add_argument("code", help="no help")
args, unknown_args = parser.parse_known_args()

if args.code.lower() == "runserver":
    os.system("color 02 & cd basic & python main.py")
elif args.code.lower() == "runappwin":
    notification()
    app = desktopWin(BASE_DIR=current_directory, DISCORD_TOKEN=TOKEN)


