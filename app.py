import os

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html", **os.environ)


@app.route("/healthcheck")
def healthcheck():
    return "WORKING"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    debug = os.environ.get("DEBUG") in ("True", "true", "t", "1")
    app.run(host="0.0.0.0", port=port, debug=debug)
