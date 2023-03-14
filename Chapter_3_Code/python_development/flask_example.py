#!/usr/bin/env python
from flask import Flask

app = Flask(__name__)

# Simple routing to root
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# More specific path
@app.route("/devices")
def devices():
    return "<p>You are at /devices</p>"

# variable in path
@app.route("/devices/<host>")
def host(host):
    return f"<p>You are at /devices/{host}</p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

