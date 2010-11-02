import memcache
import time

TOTAL = 10000
def run_test():
    client = memcache.Client(["localhost:11211"])
    print "insert"
    start = time.time()
    for i in range(TOTAL):
        client.add("%d" % i, "Hello, World. %d" % i)
    end = time.time()
    diff = end - start
    print "INSERSION TIME : %s sec" % diff
    print "INSERSION TIME : %s m sec/1 item" % (diff*1000/TOTAL)

    print "fetch"
    num = TOTAL
    start = time.time()
    for i in range(num):
        result = client.get("%d" % i)
    end = time.time()
    diff = end - start
    print "FETCH NUM : %d" % num
    print "FETCH TIME : %s sec" % (diff)
    print "FETCH TIME : %s m sec/1 item" % (diff*1000/num)
    

if __name__ == "__main__":
    run_test()
