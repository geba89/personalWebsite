from flask import Flask, render_template, redirect, url_for, flash, send_from_directory
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def home_page():
    return render_template("index.html")


def main():
    app.run()

@app.route('/download')
def download():    
    return send_from_directory(directory='static', path='files/PiotrGebskiResume.pdf', as_attachment=True)


if __name__ == "__main__":
    main()