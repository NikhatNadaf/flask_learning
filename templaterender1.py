from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html',user_name='Soha',age=25,education='B.Tech')

@app.route('/users')
def users():
  users_list = ['user1','user2','user3','user4','uer5']
  return render_template('users.html', users=users_list)

@app.route('/age/<int:age>')
def age(age):
  return render_template('age.html', age=age)