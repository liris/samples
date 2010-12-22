import pymongo
import time

TOTAL = 10000
def run_test():
    conn = pymongo.Connection()
    db = conn.test
    tbl = db.test_tbl
    tbl.save({"no" : -1, "body": ("Hello World. %d" % -1) })
    # insertion test
    start = time.time()
    for i in range(TOTAL):
        tbl.save({"no" : i, "body": ("Hello World. %d" % i) })
    end = time.time()
    diff = end - start
    print "INSERSION TIME : %s sec" % diff
    print "INSERSION TIME : %s m sec/1 item" % (diff*1000/TOTAL)

    time.sleep(10)

    # fetch time
    print "Search from 0"
    for num in (10, 100, 1000, 2000, 5000, 10000):
        start = time.time()
        for i in range(num):
            result = tbl.find_one({"no": i})
        end = time.time()
        diff = end - start
        print "FETCH NUM : %d" % num
        print "FETCH TIME : %s sec" % (diff)
        print "FETCH TIME : %s m sec/1 item" % (diff*1000/num)

    print "Search from 10000"
    for num in (10, 100, 1000, 2000, 5000, 10000):
        start = time.time()
        for i in range(num):
            result = tbl.find_one({"no": TOTAL - i})
        end = time.time()
        diff = end - start
        print "FETCH NUM : %d" % num
        print "FETCH TIME : %s sec" % (diff)
        print "FETCH TIME : %s m sec/1 item" % (diff*1000/num)

    print "CREATE INDEX"
    tbl.create_index("no")
    tbl.find_one({"no": 1})

    # fetch time
    print "Search from 0 with index"
    for num in (10, 100, 1000, 2000, 5000, 10000):
        if num > TOTAL:
            break
        start = time.time()
        for i in range(num):
            result = tbl.find_one({"no": i})
        end = time.time()
        diff = end - start
        print "FETCH NUM : %d" % num
        print "FETCH TIME : %s sec" % (diff)
        print "FETCH TIME : %s m sec/1 item" % (diff*1000/num)

    print "Search from 10000 with index"
    for num in (10, 100, 1000, 2000, 5000, 10000):
        if num > TOTAL:
            break
        start = time.time()
        for i in range(num):
            result = tbl.find_one({"no": TOTAL - i})
        end = time.time()
        diff = end - start
        print "FETCH NUM : %d" % num
        print "FETCH TIME : %s sec" % (diff)
        print "FETCH TIME : %s m sec/1 item" % (diff*1000/num)
    


if __name__ == "__main__":
    run_test()
