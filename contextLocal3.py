from flask import Flask, g, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "secret_key"

@app.before_request
def load_logged_in_user():
    user_id = session.get("user_id")
    if user_id is None:
        g.user = None
    else:
        # Normally fetched from DB
        g.user = {"id": user_id, "name": "Soha"}

@app.route('/')
def home():
    return f"Hello {g.user['name']} (User ID: {g.user['id']})" if g.user else "User Not logged in"

@app.route('/login')
def login():
    session['user_id'] = 101
    # redirect so that before_request runs again and sets g.user
    return redirect(url_for("home"))

@app.route('/logout')
def logout():
    session.pop("user_id", None)
    return redirect(url_for("home"))   # better UX, go back home

@app.route('/dashboard')
def dashboard():
    return f"Welcome {g.user['name']} to dashboard" if g.user else "Not logged in"

if __name__ == "__main__":
    app.run(debug=True)
