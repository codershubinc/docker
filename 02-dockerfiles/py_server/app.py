
from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8080


class HelloHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Extract the path after the leading '/'
        any_path = self.path[1:]
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(f"hello {any_path}".encode())


print(f"Starting server on port {PORT}")
with HTTPServer(("", PORT), HelloHandler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
