# /api/index.py

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Create a custom HTTP request handler
class handler(BaseHTTPRequestHandler):
    # Define how to handle GET requests
    def do_GET(self):
        print("Here => ", self.path)
        if self.path == "/home":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(
                "Python API Example - Welcome to the homepage!".encode("utf-8")
            )
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_data = {"message": "Not Found", "status": "error"}
            json_error_data = json.dumps(error_data)
            self.wfile.write(json_error_data.encode("utf-8"))
            
    # Handle POST requests
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # Get the size of data
        post_data = self.rfile.read(content_length)  # Get the data
        try:
            # Attempt to parse the post_data as JSON
            json_data = json.loads(post_data)
            response_message = f"POST Request Received: {json_data}"
        except json.JSONDecodeError:
            # If not valid JSON, just echo the raw data
            response_message = f"POST Request Received: {post_data.decode('utf-8')}"
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response_content = f"<html><body><h1>{response_message}</h1></body></html>"
        self.wfile.write(response_content.encode('utf-8'))

            
# Define server settings
def run(server_class=HTTPServer, handler_class=handler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Server running on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()