from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['POST', 'GET'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    
@app.route('/welcome', methods=['POST','GET'])
def welcome():
    
    username = request.form.get('username')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    username_error = ''
    password_error = ''
    password2_error = ''

    if len(username) < 3 or len(username) > 20 or (' ') in username:
        username_error = 'Length of username must be 3-20 countinuous characters'
        username=''

    if len(password) < 3 or len(password) > 20 or (' ') in password:
        password_error = 'Length of password must be 3-20 continuous characters'
        password=''

    elif password2 != password:
        password2_error = 'Passwords do not match'
        password2=''

    if not any([username_error, password_error, password2_error]):
        return render_template('welcome.html', user=username)
    else:
        return render_template('signup.html', username_e=username_error, password_e= password_error, password2_e=password2_error)
        username=username
        password=password
        password2=password2

    
app.run()
