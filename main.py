from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def home_page():
    return render_template("index.html")


def main():
    app.run()

if __name__ == "__main__":
    main()