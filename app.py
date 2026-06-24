from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Hello World! My K8s Project is working!</h1>")

server = HTTPServer(('0.0.0.0', 5000), MyHandler)
print("Server started on port 5000...")
server.serve_forever()