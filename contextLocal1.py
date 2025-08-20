from flask import Flask, request, g

app = Flask(__name__)

@app.before_request
def before_request_func():
    g.user = "soha"  # temporary variable for this request

@app.route('/')
def home():
    return f"Hello {g.user}, your method is {request.method}"

@app.route('/greet')
def greet():
    return f"Greet Hello {g.user}, your method is {request.method}"

if __name__ == "__main__":
    app.run(debug=True)
