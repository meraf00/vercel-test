import os
from flask import Flask, render_template
from dotenv import load_dotenv
from util import prettyprint

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET")


@app.route("/")
def home():
    return render_template("home.html", env=os.getenv("ENV"), prettyprint=prettyprint)


if __name__ == "__main__":
    app.run(debug=True)
