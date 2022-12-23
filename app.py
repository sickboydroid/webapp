from flask import Flask, request, render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    if request.method == "GET":
        print("Called via GET")
        return render_template('resp.html', username=request.args.get("user-name", "unknown"), secure="securely")
    elif request.method == "POST":
        print("Called via POST")
        return render_template('resp.html', username=request.form.get("user-name", "unknown"), secure="unsecurely")
    return render_template("Something was wrong!!")

@app.route("/say", methods=['PUT'])
def hey():
    if(request.method == 'PUT'):
        print("Called via PUT")
    print(request)
    return "WOW you called me, great"



Flask.run(app, debug=True)
