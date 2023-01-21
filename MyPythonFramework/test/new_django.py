# from http.server import HTTPServer, BaseHTTPRequestHandler
#
#
# class MyHandler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(200)
#         self.send_header("Content-type", "text/html")
#         self.end_headers()
#         with open("index.html", "r") as file:
#             self.wfile.write(bytes(file.read(), "utf8"))


# httpd = HTTPServer(("", 8000), MyHandler)
# httpd.serve_forever()


# class Framework:
#     def __init__(self):
#         self.routes = {}
#
#     def add_route(self, path, callback):
#         self.routes[path] = callback
#
#     def serve(self, path):
#         callback = self.routes.get(path)
#         if callback:
#             callback()
#         else:
#             raise ValueError("Route not found.")


# app = Framework()
#
#
# def index():
#     print("Welcome to the index page.")
#
#
# def about():
#     print("Learn more about us.")
#
#
# app.add_route("/", index)
# app.add_route("/about", about)
#
# app.serve("/")  # Output: Welcome to the index page.
# app.serve("/about")  # Output: Learn more about us.

# import os
# # from BaseHTTPServer import HTTPServer
# # from SimpleHTTPServer import SimpleHTTPRequestHandler
# from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
# ROUTES = [
#     ('/', '/var/www/doc-html')
# ]
#
#
# class MyHandler(SimpleHTTPRequestHandler):
#     def translate_path(self, path):
#         # default root -> cwd
#         root = os.getcwd()
#
#         # look up routes and get root directory
#         for patt, rootDir in ROUTES:
#             if path.startswith(patt):
#                 path = path[len(patt):]
#                 root = rootDir
#                 break
#         # new path
#         return os.path.join(root, path)
#
#
# if __name__ == '__main__':
#     httpd = HTTPServer(('127.0.0.1', 8000), MyHandler)
#     print('Starting server, use <Ctrl-C> to stop')
#     httpd.serve_forever()


import inspect

def current_function():
    print(inspect.stack()[1][3])

def index():
    current_function()

index()