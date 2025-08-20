from flask import Flask, request

app = Flask(__name__)

@app.route('/example', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def example():
    if request.method == 'GET':
        return " This is a GET request (usually for fetching data)"
    elif request.method == 'POST':
        return " This is a POST request (usually for creating data)"
    elif request.method == 'PUT':
        return " This is a PUT request (usually for updating/replacing data)"
    elif request.method == 'PATCH':
        return " This is a PATCH request (usually for partially updating data)"
    elif request.method == 'DELETE':
        return " This is a DELETE request (usually for deleting data)"
    else:
        return "Unknown request method"


if __name__ == '__main__':
    app.run(debug=True)
