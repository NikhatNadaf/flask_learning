from flask import Flask
from markupsafe import escape
app= Flask(__name__)
@app.route('/') #default route
def default_route():
  return "<p>Welcome to the Flask App!</p>"

@app.route('/user/<username>') #accept string only
def show_user_profile(username):
  return 'User: '+ escape(username)

@app.route('/post/<int:post_id>') #accept integer(positive) only
def show_post(post_id):
  return 'Post ID: ' + str(post_id)

@app.route('/path/<path:subpath>') #accept any path(including slashes)
def show_subpath(subpath):
  return 'Subpath: ' + escape(subpath)
@app.route('/projects/')
def projects():
    return 'The project page'