from geventwebsocket.handler import WebSocketHandler
from gevent import pywsgi
from gevent import socket
import gevent

chat_clients = set()

def read_server(fileobj):
    while True:
        data = fileobj.readline()
        if not data:
            print "end read_server"
            break
        for client in chat_clients:
            client.send(data)

def handle_chat(ws):
    chat_clients.add(ws)
    while True:
        message = ws.wait()
        if message is None:
            break
        fileobj.write("msg:" + message + "\n")
        fileobj.flush()

    chat_clients.remove(ws)

def app(environ, start_response):
    path = environ["PATH_INFO"]
    if path == "/":
        start_response("200 OK", [("Content-Type", "text/html")])
        return open("chat.html").read() % port
    elif path == "/chat":
        handle_chat(environ["wsgi.websocket"])
    else:
        start_response("404 Not Found", [])
        return []

if __name__ == "__main__":
    import sys
    index = int(sys.argv[1])
    port = 3000 + index
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 3000))
    fileobj = sock.makefile()
    gevent.spawn(read_server, fileobj)

    server = pywsgi.WSGIServer(("", port), app, handler_class=WebSocketHandler)
    server.serve_forever()
