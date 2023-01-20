from http.server import BaseHTTPRequestHandler
import os
from settings import FRONTEND_DIR




class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = FRONTEND_DIR + '/index.html'
        try:
            split_path = os.path.splitext(self.path)
            request_extension = split_path[1]
            if request_extension != ".py":
                f = open(self.path).read()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(f, 'utf-8'))
            else:
                f = "File not found"
                self.send_error(404, f)
        except Exception as e:
            f = "File not found"
            print(e)
            self.send_error(404, f)
