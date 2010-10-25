from geventwebsocket.handler import WebSocketHandler
from gevent import pywsgi
import gevent

chat_clients = set()

def handle(ws):
    if ws.path == "/chat":
        chat_clients.add(ws)
        while True:
            message = ws.wait()
            if message is None:
                break
            # TODO: send to all
            for client in chat_clients:
                client.send(message)

        chat_clients.remove(ws)

def app(environ, start_response):
    path = environ["PATH_INFO"]
    if path == "/":
        start_response("200 OK", [("Content-Type", "text/plain")])
        return ["start"]
    elif path == "/chat":
        handle(environ["wsgi.websocket"])
    else:
        start_response("404 Not Found", [])
        return []

if __name__ == "__main__":
    server = pywsgi.WSGIServer(("", 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
