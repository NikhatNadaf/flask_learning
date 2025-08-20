from flask import Flask, render_template

app = Flask(__name__)

@app.errorhandler(404)
def not_found_error(error):
    return "Oops! Page not found (404)", 404

@app.errorhandler(500)
def internal_error(error):
    return "Something went wrong (500)", 500
