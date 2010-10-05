
import pymongo
from pymongo.objectid import ObjectId
from flask import Flask, request, flash, render_template, url_for
from flask import session, redirect
from flask import g

def req_start():
    g.mongo = pymongo.Connection()

def req_end(response):
    g.mongo.disconnect()
    del g.mongo
    return response

app = Flask(__name__)
app.debug = True
app.before_request(req_start)
app.after_request(req_end)

@app.route("/")
@app.route("/<oid>")
def index(oid = None):
    db = g.mongo.blog
    if oid:
        entries = db.entry.find({"_id": ObjectId(oid)})
    else:
        entries = db.entry.find().sort([("created", -1)])

    return render_template("index.html", entries=entries)

@app.route("/edit")
@app.route("/edit/<oid>")
def edit(oid=None):
    db = g.mongo.blog
    if not oid:
        entry = {}
    else:
        entry = db.entry.find_one({"_id": ObjectId(oid)})

    return render_template("edit.html", entry=entry)

@app.route("/save", methods=["POST"])
def save():
    db = g.mongo.blog
    form = request.form
    oid = form.get("oid", None)
    if not oid:
        entry = {}
    else:
        entry = db.entry.find_one({"_id": ObjectId(oid)})
        
    entry["title"] = form["title"]
    entry["body"] = form["body"]
    result = db.entry.save(entry)
    oid = str(result)

    return redirect(url_for("index", oid=oid))

@app.route("/delete", methods=["POST"])
def delete():
    db = g.mongo.blog
    form = request.form
    oid = form.get("oid", None)
    if oid:
        entry = db.entry.find_one({"_id": ObjectId(oid)})
        db.entry.remove(entry)
        
    return redirect(url_for("index"))
   
if __name__ == "__main__":
    app.run()
