from gevent.server import StreamServer

class BCServer:
    def __init__(self):
        self.clients = []

    def received(self, socket, addr):
        fileobj = socket.makefile()
        self.clients.append(fileobj)
        try:
            while True:
                line = fileobj.readline()
                if not line:
                    break
                if line.startswith("quit:"):
                    break
                if line.startswith("msg:"):
                    msg = line.split(":", 1)[1]
                    for fo in self.clients:
                        try:
                            fo.write(msg)
                            fo.flush()
                        except Exception, e:
                            print p
        except Exception, e:
            print e
        finally:
            self.clients.remove(fileobj)


if __name__ == "__main__":
    bcs = BCServer()
    server = StreamServer(("0.0.0.0", 3000), bcs.received)
    server.serve_forever()
