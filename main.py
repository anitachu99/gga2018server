from flask import Flask, request, render_template, redirect, jsonify
app = Flask(__name__)


event_1 = 0
event_2 = 0
event_3 = 0

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/event-1", methods = ["POST"])
def set_event_1():
    if request.method == "POST":
        print("Is true? {}".format(request.form["event-1"] is not None))
        if request.form["event-1"] is not None:
            global event_1
            event_1 += 1
            print("Event-1: {}".format(event_1))
    return redirect("/")


@app.route("/event-2", methods = ["POST"])
def set_event_2():
    if request.method == "POST":
        if request.form["event-2"] is not None:
            global event_2
            event_2 += 1
    return redirect("/")


@app.route("/event-3", methods = ["POST"])
def set_event_3():
    if request.method == "POST":
        if request.form["event-3"] is not None:
            global event_3
            event_3 += 1
    return redirect("/")


@app.route("/get-data", methods = ["GET"])
def get_votes():
    global event_1
    global event_2
    global event_3
    vote_value_pairs = {
        "event-1": event_1,
        "event-2": event_2,
        "event-3": event_3
    }
    return jsonify(**vote_value_pairs)


if __name__ == '__main__':
    app.run()
