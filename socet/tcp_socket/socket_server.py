import os
import socket
import tkinter
import threading
import _thread
import json

# path_to_json = 'S:/Programmer/Projects/socet/tcp_socket/docs'
# main_url = ''
# Сборка:
path_to_json = 'C:/programmer/tcp_socket/docs'
# Сборка:
main_url = 'C:/programmer/tcp_socket/' 


def new_connection(__connection: any) -> None:
    print("connection start...")

    while True:
        data = __connection.recv(1024)
        # print(data.decode("utf-8"), type(data.decode("utf-8")))
        data_json = json.loads(data.decode("utf-8"))
        # print(type(data_json))
        json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
        for data_one in data_json:

            if data_one['file_name'] in json_files:
                with open(path_to_json + "\\" + data_one['file_name'], 'rb') as f:
                    try:
                        config = json.dumps(f.read())
                        if config == data_one['data']:
                            continue
                        else:
                            with open(path_to_json + "\\" + data_one['file_name'], 'w') as ff:
                                json.dump(data_one['data'], ff)
                    except:
                        with open(path_to_json + "\\" + data_one['file_name'], 'w') as ff:
                            json.dump(data_one['data'], ff)
            else:
                with open(path_to_json + "\\" + data_one['file_name'], 'w') as ff:
                    json.dump(data_one['data'], ff)

        res = f"[request]: {data} {type(data)}"
        global _set_text
        _set_text(res)  # tk_label.config(text="")
        print(res)

        if not data:
            __connection.send(b"[response]: MOT_ANY_DATA 400")
            break
        else:
            __connection.send(b"[response]: OK 200")

    __connection.close()
    pass


# TODO сервер, listener "слушатель" -> ip:port (порт занят и открыт)
def backend_server() -> None:  # 192.168.0.127:8000

    global _set_text
    _set_text("server started")

    with open(main_url+"config.json", 'rb') as f:
        config = json.load(f)  # config = json.loads(f.read())

    host = config["host"]  # localhost
    port = config["port"]  # 8000
    print(host, port)

    print_lock = threading.Lock()
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind((host, port))
    my_socket.listen(5)

    while True:
        connection, address = my_socket.accept()
        print_lock.acquire()

        _thread.start_new_thread(new_connection, (connection,))
    my_socket.close()


def start_server():
    threading.Thread(target=backend_server).start()


def frontend_server() -> None:
    tk_windows = tkinter.Tk()
    tk_windows.title("our server")
    tk_windows.geometry("300x100")

    tk_label = tkinter.Label(tk_windows, text="server ready to start")
    tk_label.grid(row=0, column=0)

    def __set_text(__text: str) -> None:
        tk_label.config(text=__text)

    global _set_text
    _set_text = __set_text

    tk_button = tkinter.Button(tk_windows, text="start server", command=start_server)
    tk_button.grid(row=1, column=0)

    tk_windows.mainloop()


if __name__ == '__main__':
    # заглушка, чтобы код не ругался на тип данных
    def _set_text_ph(__text: str) -> None:
        pass

    _set_text = _set_text_ph  # промежуточная глобальная переменная для будущего хранения функции для установки
    # текста в поле

    frontend_server()

# области видимости


# a1 = 12  # глобальные
# print(a1)
#
#
# def set1():
#     global a1
#     a1 = 15  # локальная для set1
#     print(a1)
#     # def set2():
#     #     a1 = 17
#
#
# set1()
# print(a1)


# b1 = 12
# print(b1)
#
#
# def set4(val1: int) -> int:
#     return val1 ** 2
#
#
# b1 = set4(9)
# print(b1)  # 81
#
# b1 = set4
# print(b1)  # <function set4 at 0x0000012D307C60E0>
# b2 = b1(9)
# print(b2)  # 81
