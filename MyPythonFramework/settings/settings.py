import os

HOST_NAME = '127.0.0.1'

PORT = 8000


# S:\Programmer\Projects\MyPythonFramework\
BASE_DIR = "\\".join((dict(os.environ)['PATH']).split(";")[0].replace('\\', '/').split('/')[:-2]) + "\\"

FRONTEND_DIR = BASE_DIR + "frontend\\"

APPS = ['django_app']

# print(str(FRONTEND_DIR)[1:])
os.environ.setdefault('BASE_DIR', str(BASE_DIR))
os.environ.setdefault('HOST_NAME', str(HOST_NAME))
os.environ.setdefault('PORT', str(PORT))
os.environ.setdefault('FRONTEND_DIR', str(FRONTEND_DIR))  # S:\Programmer\Projects\MyPythonFramework\frontend\
os.environ.setdefault('APPS', " ".join(APPS))

