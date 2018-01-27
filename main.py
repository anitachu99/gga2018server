from flask import Flask, request, render_template, redirect, jsonify
app = Flask(__name__)

global_events = {
    "event_1": 0,
    "event_2": 0,
    "event_3": 0
}


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/event-1", methods=["POST"])
def set_event_1():
    event_name = "event_1"
    if request.method == "POST":
        if request.form[event_name] is not None:
            set_event(event_name)
            print(global_events)
    return redirect("/")


@app.route("/event-2", methods=["POST"])
def set_event_2():
    event_name = "event_2"
    if request.method == "POST":
        if request.form[event_name] is not None:
            set_event(event_name)
            print(global_events)
    return redirect("/")


@app.route("/event-3", methods=["POST"])
def set_event_3():
    event_name = "event_3"
    if request.method == "POST":
        if request.form[event_name] is not None:
            set_event(event_name)
            print(global_events)
    return redirect("/")


@app.route("/get-data", methods=["GET"])
def get_votes():
    global global_events
    return jsonify(**global_events)


@app.route("/_reset-event1")
def reset_event_1():
    global global_events
    global_events["event_1"] = 0
    print(global_events)
    return redirect("/")


@app.route("/_reset-event2")
def reset_event_2():
    global global_events
    global_events["event_2"] = 0
    print(global_events)
    return redirect("/")


@app.route("/_reset-event3")
def reset_event_3():
    global global_events
    global_events["event_3"] = 0
    print(global_events)
    return redirect("/")


@app.route("/_reset-all-events")
def reset_all_events():
    """
    This function should not be publicly invoked!
    """
    global global_events
    global_events = global_events.fromkeys(global_events.keys(), 0)
    print(global_events)
    return redirect("/")


def set_event(name):
    """
    Increments the event based on the name if the key exists
    """
    global global_events
    if name in global_events:
        global_events[name] += 1
    else:
        global_events[name] = 0


if __name__ == '__main__':
    app.run()
