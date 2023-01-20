import os

HOST_NAME = '127.0.0.1'

PORT = 8000

BASE_DIR = "\\".join((dict(os.environ)['PATH']).split(";")[0].replace('\\','/').split('/')[:-2])

FRONTEND_DIR = BASE_DIR + "/frontend"
