from datetime import datetime
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(50), nullable=False)
    exercise = db.Column(db.String(40), nullable=False)
    weight = db.Column(db.String(10), nullable=False)
    set = db.Column(db.String(10), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        record = Record(day=request.form.get("day"),
                        exercise=request.form.get("exercise"),
                        weight=request.form.get("weight"),
                        set=request.form.get("set"))
        db.session.add(record)
        db.session.commit()

    records = Record.query.all()
    return render_template("home.html", records=records)