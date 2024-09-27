from flask import Flask, render_template, blueprints
from controlers import controler

app = Flask(__name__)

app.register_blueprint(controler.Gamer)


@app.route("/")
def hello_world():
    return render_template("html.html")

if __name__ == '__main__':
    app.run(debug = True)




