from markupsafe import escape
from flask import Flask
app = Flask(__name__)
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
@app.route("/path/<variable_name>")
def function_name(variable_name):
    return f"You entered: {variable_name}"
