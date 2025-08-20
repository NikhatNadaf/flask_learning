from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "mysecretkey"  # Required for sessions

@app.route('/')
def home():
    if 'username' in session:
        return f"Welcome back, {session['username']}!"
    return "You are not logged in!"

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']  # Store data in session
        return redirect(url_for('home'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove username from session
    return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(debug=True)