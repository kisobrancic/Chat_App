from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///messages.db"

db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    text = db.Column(db.String)

@app.route("/")
def index():
    messages = Message.query.all()

    return render_template("index.html", messages=messages)

@app.route("/send", methods=["POST"])
def send():
    username = request.form.get("username")
    text = request.form.get("text")

    message = Message(username=username, text=text)

    db.session.add(message)
    db.session.commit()

    return redirect("/")

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run()
