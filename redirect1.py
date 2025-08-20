from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome Home!"

@app.route('/old')
def old_page():
    # Redirects to /new
    return redirect(url_for('new_page'))

@app.route('/new')
def new_page():
    return "This is the NEW page!"
