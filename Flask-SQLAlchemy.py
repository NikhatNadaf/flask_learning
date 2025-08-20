from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)

# Define a model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

@app.route('/')
def home():
    user = User.query.first()
    return f"Hello {user.name}" if user else "No users found"
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)