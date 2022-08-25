# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        #testing to see if styles work lol
        self.wfile.write(bytes("<html><head><title>Python Web Server</title></head>", "utf-8"))
        self.wfile.write(bytes(
        "<p style='background-color:#FFFFE0;font-size:50px;text-align:center;'>Request %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body style='background-color:#B0C4DE;'>", "utf-8"))
        self.wfile.write(bytes("<p>This is a webserver built with python</p>", "utf-8"))
        self.wfile.write(bytes("<p>host name<br> %s</p>" % hostName, "utf-8"))
        self.wfile.write(bytes("<p>server port<br> %s</p>" % serverPort, "utf-8"))
        self.wfile.write(bytes("<footer style='padding:10;size:100%;'><p style='font-size:20px;text-align:center;'>A python webserver<p/></footer>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("[ INFO ] PYTHON WEBSERVER ... \n")
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
