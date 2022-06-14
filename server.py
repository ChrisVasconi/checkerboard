from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def board():
    return render_template("index.html", num1=8)


@app.route("/4")
def four():
    return render_template('index.html', num1=4)


@app.route("/16")
def four_four():
    return render_template('index.html', num1=16)


if __name__ == "__main__":
    app.run(debug=True)
