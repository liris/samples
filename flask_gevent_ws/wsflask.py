from geventwebsocket.handler import WebSocketHandler
from gevent import pywsgi
import gevent
from flask import Flask, request, flash, render_template, url_for
from flask import session, redirect, g
from flaskext.babel import Babel, gettext

app = Flask(__name__)

chat_html = """
<html>
<head><title>Web Socket Chat</title></head>
<body>
<script>
var ws = new WebSocket("ws://127.0.0.1:5000/chat");
ws.onopen = function() {
};

ws.onmessage = function(message) {
 var txtNode = document.createTextNode(message.data);
 var brNode = document.createElement('br');
 var cnode = document.getElementById("content");
 cnode.appendChild(txtNode);
 cnode.appendChild(brNode);
};
window.onunload = function(){
  ws.close();
};
</script>
<h1>Web Socket Chat</h1>
<div id="content">
</div>
<input id="message" type="text" onChange="javascript:ws.send(this.value);this.value='';"/>
</body>
</html>
"""

chat_clients = set()

def handle_chat(ws):
    chat_clients.add(ws)
    while True:
        message = ws.wait()  
        if message is None:
            break
        for client in chat_clients:
            client.send(message)

    chat_clients.remove(ws)

@app.route("/")
def index():
    return "hello"

def myapp(environ, start_response):
    path = environ["PATH_INFO"]
    if path == "/":
        return app(environ, start_response)
    elif path == "/chat":
        handle_chat(environ["wsgi.websocket"])
    elif path == "/chat.html":
        start_response("200 OK", [])
        return chat_html
    else:
        return app(environ, start_response)

if __name__ == "__main__":
    server = pywsgi.WSGIServer(("", 5000), myapp, handler_class=WebSocketHandler)
    server.serve_forever()
