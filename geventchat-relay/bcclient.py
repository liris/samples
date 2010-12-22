import gevent
from gevent import socket


def write(fileobj, sock):
    phrase = ["msg:hello\n", "msg:quit\n", "msg:from\n", "msg:gevent\n", "quit:gevent\n"]
    for p in phrase:
        fileobj.write(p)
        fileobj.flush()
        print "write from spawn " + p
        gevent.sleep(1)

def doit():
    print "sock"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 3000))
    print "connected"
    fileobj = s.makefile()
    gevent.spawn(write, fileobj, s)
    fileobj.write('Hello, world\n')
    fileobj.flush()
    print "flush"
    while True:
        data = fileobj.readline()
        if not data:
            print "break"
            break
    #s.close()
        print 'Received', repr(data)

job = gevent.spawn(doit)
gevent.joinall([job])
