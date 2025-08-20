from flask import Flask, request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename="app.log", level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s")

@app.route('/')
def home():
    app.logger.info("Home page accessed")
    return "Welcome!"

@app.route('/error')
def cause_error():
    try:
        1 / 0
    except Exception as e:
        app.logger.error("Error occurred: %s", e)
        return "Something went wrong!", 500

if __name__ == '__main__':
    app.run(debug=True)