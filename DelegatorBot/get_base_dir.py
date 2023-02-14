import os

from dotenv import load_dotenv


def get():
    load_dotenv()
    return os.environ['BASE_DIR']
