import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Bello! Bello Bello"
    return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
    headline = "Bye Bye Bye"
    return render_template("index.html", headline=headline)

@app.route("/david")
def david():
    return "Hello, david!"

@app.route("/time")
def time():
    now = datetime.datetime.now();
    # new_year = "Yes" if (now.month == 1 and now.day == 1) else "No"
    new_year = now.month == 1 and now.day == 1
    return render_template("newyear.html", new_year=new_year)

@app.route("/<string:name>")
def hello(name):
    return f"<h1>Hello, {name}!</h1>"

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
