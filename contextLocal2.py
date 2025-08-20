from flask import Flask, request, g

app = Flask(__name__)
@app.before_request
def before_request_func():
    if request.path == '/':
        g.user = "Soha"   # set only for `/` request

@app.route('/')
def home():
    return f"Hello {g.user}"

@app.route('/greet')
def greet():
    return f"Greet Hello {getattr(g, 'user', 'NOT SET')}"

if __name__ == "__main__":
    app.run(debug=True)
