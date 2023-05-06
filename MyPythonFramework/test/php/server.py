from http.server import HTTPServer, BaseHTTPRequestHandler
import subprocess
import os




class PHPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        os.environ["php_path"] = str(self.path)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        try:
            # This line specifies the path of the PHP file
            output = subprocess.check_output(
                ['php', os.path.join(os.path.dirname(__file__), 'index.php')],
                cwd=os.path.dirname(__file__)
            )
            # print(output.title())
            self.wfile.write(output)
        except subprocess.CalledProcessError as e:
            self.send_error(404, 'File Not Found: %s' % self.path)


httpd = HTTPServer(('', 8000), PHPRequestHandler)
print("Server is running on port 8000")
httpd.serve_forever()
