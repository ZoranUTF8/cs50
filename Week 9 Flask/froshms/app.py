from flask import Flask, render_template, request
from models import Registrant
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy()
app.config['SECRET_KEY'] = "secret-key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database'

db.init_app(app)

registrants = {}
sports = [
    "Basketball",
    "Soccer",
    "Football"
]


@app.route("/")
def index():
    return render_template("index.html", sports=sports)


@app.route("/register", methods=["GET", "POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")


# if someone changes the select in dev tools
    if not sport or name not in sports:
        return render_template("error.html")

    newRegistrant = Registrant(
        sport_name=sport,
        user_name=name
    )

    db.session.add(newRegistrant)
    db.session.commit()

    registrants[name] = sport

    return render_template("success.html")


@app.route("/registrants")
def registrantsPage():
    return render_template("registrants.html", registrants=registrants)
