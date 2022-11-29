from flask import Flask, render_template, request

#! TURN THIS FILE INTO A FLASK APPLICATION
app = Flask(__name__)

#! We then use the route() decorator to tell Flask what URL should trigger our function.


@app.route("/", methods=["GET", "POST"])
def homePage():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        return render_template("greet.html", user_name=request.args.get("user_name", "default name"))
