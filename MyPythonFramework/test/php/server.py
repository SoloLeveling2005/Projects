from http.server import HTTPServer, CGIHTTPRequestHandler

# create a server on port 8000
server = HTTPServer(('', 8000), CGIHTTPRequestHandler)

# set the PHP interpreter path
CGIHTTPRequestHandler.cgi_directories = ['/path/to/php']

# start the server
server.serve_forever()