from flask import Flask #import Flask class
app = Flask(__name__) #create flask application instance
@app.route('/') #define rout for home page as '/'
def hello(): #function that rins when '/' is accessed
  return "<p>Hello</p>" #return a simple HTML response - to browser
@app.route('/login')
def login():
  return "<p>Login Page</p>" 
@app.route('/about')
def about():
  return "<p>About Page</p>"




# if __name__== '__main__':
#   app.run(debug=True)