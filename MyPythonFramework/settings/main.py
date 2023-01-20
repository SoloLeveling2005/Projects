import time
from http.server import HTTPServer
from server import Server
from settings import HOST_NAME, PORT


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


if type(HOST_NAME) != str:
    message_except = "Переменная" + color.BLUE + ' HOST_NAME' + color.END + " имеет тип 'STRING'"
    raise Exception(message_except)

if type(PORT) != int:
    raise Exception("Переменная" + color.BLUE + ' PORT' + color.END + " имеет тип 'INTEGER'")

if __name__ == "__main__":
    httpd = HTTPServer((HOST_NAME, PORT), Server)
    print(time.asctime(), "Start Server - " + f"http://{HOST_NAME}:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), 'Stop Server - %s:%s' % (HOST_NAME, PORT))
