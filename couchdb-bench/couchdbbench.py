import couchdbkit
import time

TOTAL = 10000

def run_test():
    server = couchdbkit.Server("http://localhost:5984")
    db = server.get_or_create_db("test")

    start = time.time()
    for i in range(TOTAL):
        doc = {"key": i, "value": ("Hello World. %d" % i) }
        db.save_doc(doc)
    end = time.time()
    diff = end - start
    print "INSERSION TIME : %s sec" % diff
    print "INSERSION TIME : %s m sec /item" % (diff*1000/TOTAL)
    
    try:
        db.delete_doc("_design/viewtest")
    except:
        pass
 
    design_doc = {
        "_id": "_design/viewtest",
        "language": "javascript",
        "views":
            {"all": {"map":
                         """function(doc) { if (doc.key) {emit(doc.key, doc) }} """
                     }
             }
        }
    res = db.save_doc(design_doc)
     
    for num in (10, 100, 1000): #, 2000, 5000, 10000):
        start = time.time()
        for i in range(num):
            doc = db.view("viewtest/all", key=i)
        end = time.time()
        print "FETCH NUM %d" % num
        diff = end - start
        print "FETCH NUM : %d" % num
        print "FETCH TIME : %s sec" % (diff)
        print "FETCH TIME : %s m sec/1 item" % (diff*1000/num)

    db.delete_doc(res["id"])

if __name__ == "__main__":
    run_test()
