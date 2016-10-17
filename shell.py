from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest')
def hello_guest():
   print(request.args)
   return 'Hello %s as Guest'

@app.route('/user/')
def hello_user():
   return redirect(url_for('hello_guest', guest='devesh'))


if __name__ == '__main__':
   app.run(debug = True)