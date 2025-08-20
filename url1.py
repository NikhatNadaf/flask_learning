from flask import Flask,url_for,redirect
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def index():
  return 'Welcome! <a href="' + url_for('profile', username='Maggie') + '">Go to Maggie\'s profile</a>'

@app.route('/user/<username>')
def profile(username):
  return f"Hello, {username}! "

@app.route('/go-to-profile')
def go_to_profile():
  return redirect(url_for('index'))
@app.route("/<name>")
def hello(name):
    # return f"Hello, {name}!"
    return 1/0;