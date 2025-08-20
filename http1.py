from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST']) #URL can be accessed with both GET and POST methods.
def login():
    if request.method == 'POST':
        return "Processing login..."
    else:  # request.method == 'GET'
        return "Login Page"
@app.post('/submit')
def submit():
    if request.method == 'POST':
        return "This is a POST request!"
    else:  # Default is GET
        return "This is a GET request!"