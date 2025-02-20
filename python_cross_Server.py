import http.server
import ssl

PORT = 8000

class CustomRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()

httpd = http.server.HTTPServer(("192.168.1.45", PORT), CustomRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile="cert.pem", keyfile="key.pem", server_side=True)

print(f"Serving HTTPS at https://localhost:{PORT}")
httpd.serve_forever()


