from flask import Flask, flash, render_template, redirect, url_for, get_flashed_messages

app = Flask(__name__)
app.secret_key = "mysecretkey"  # Required for flashing (uses session)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login')
def login():
    # Flashing a success message
    flash("You were successfully logged in!", "success")
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    # Flashing an error message
    flash("You have been logged out!", "error")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)