

from flask import Flask, request

app = Flask(__name__)

index = 0

def show_cookie(path):
    global index
    html = "<html><body><h1>Cookie<h1><ul>"
    sortedKeys = request.cookies.keys()
    sortedKeys.sort()
    for key in sortedKeys:
        html += "<li>%s = %s</li>" % (key, request.cookies[key])
    html += "</ul></body></html>"

    response = app.make_response(html)
    index += 1
    value = "%d" % index
    value += "z"*512

    response.set_cookie("Eater%s%03d" % (path[1:], index), value=value, path=path)

    return response


@app.route("/")
def show_root():
    return show_cookie("/")

@app.route("/sub")
def show_sub():
    return show_cookie("/sub")

app.run(debug=True, host="0.0.0.0")
