from flask import Flask, url_for

app = Flask(__name__)

@app.route("/img")
def home():
    # This will generate the correct URL for logo.png inside static folder
    return f"<h1>Welcome!</h1><img src='{url_for('static', filename='Img.jpg')}' height='200px' width='300px' alt='Logo'>"


@app.route("/css")
def css():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>CSS Example</title>
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='style.css')}">
    </head>
    <body>
        <h1>CSS Example</h1>
        <p>This is styled with CSS!</p>
    </body>
    </html>
    """