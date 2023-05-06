import socketserver
from http.server import BaseHTTPRequestHandler
import os
from core import main_core

FRONTEND_DIR = os.environ.get('FRONTEND_DIR')


# print(main_core.mass_routers)

class Server(BaseHTTPRequestHandler):
    def __init__(self, request: bytes, client_address: tuple[str, int], server: socketserver.BaseServer):
        super().__init__(request, client_address, server)
        self.mass_url = None
        self.path_one = None
        self.path_two = None
        self.file_url = None

    def do_GET(self):
        # self.mass_url = str(self.path).split('/')
        print("main_core.mass_routers", main_core.mass_routers)
        for router in main_core.mass_routers:
            keys = list(router.keys())
            # print(router[keys[0]]['path'])
            # print(self.path)
            print(keys)
            self.path_one = router[keys[0]]['path']
            self.path_two = router[keys[0]]['path']
            self.file_url = router[keys[0]]['url_file']
            if self.path_one[:1] != "/":
                self.path_two = self.path + "/"

            print("path_one:",str(self.path_one))
            print("path_two:",str(self.path_two))

            if self.path == self.path_one or self.path == self.path_two:
                self.path = FRONTEND_DIR + "/" + self.file_url
            try:
                split_path = os.path.splitext(self.path)
                request_extension = split_path[1]
                if request_extension != ".py":
                    f = open(self.path).read()
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(bytes(f, 'utf-8'))
                    break
                else:
                    f = "File not found"
                    self.send_error(404, f)
                    break
            except Exception as e:
                f = "File not found"
                print(e)
                # self.send_error(404, f)
                # break
            # break
