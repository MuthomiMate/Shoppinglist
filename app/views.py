import os
from user import User
from flask import  session, render_template, request, redirect, g, url_for
from app import app

newuser = User()
"""Instantiating objects"""



@app.route('/', methods=['GET', 'POST'])
def reg():
    """Handles the requests for the register view"""
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['usernma']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['cpassword']
        result = newuser.register(email, name, username, password, cpassword)
        if result == 1:
            session['user'] = name
            return render_template('login.html')
        elif result == 6:
            msg = ("please fill all the fields")
            return render_template('register.html', data=msg)
        elif result == 5:
            msg = ("Username has alredy been taken")
            return render_template('register.html', data=msg)
        elif result == 3:
            msg = ("password do not match")	
            return render_template('register.html', data=msg)
        elif result == 2:
            error = "email must be a valid email"
            return render_template('register.html', data=error)	
        elif result == 4:
            error = "email already registered"
            return render_template('register.html', data=error)	
    else:
        return render_template('register.html')
                		
@app.route('/login', methods=['GET', 'POST'])
def logins():
    """Handles the requests for the login view"""
    if request.method == "POST":
        emailLogin = request.form['email']
        passLogin = request.form['password']
        loginResult = newuser.login(emailLogin, passLogin)
        if loginResult == 1:
            name = newuser.get_user_name(emailLogin)
            email = newuser.get_user_email(emailLogin)
            session['user'] = name
            session['email'] = email
            return render_template('home.html', data=session)
        elif loginResult == 2:
            error = "Password mismatch"
            return render_template('login.html', data=error)	
        elif loginResult == 3:
            error = "The user does not exist please register and try again"
            return render_template('login.html', data=error)	
        elif loginResult == 4:
            error = "Please fill all the fields"
            return render_template('register.html', data=error)	 	
        else:
            error = "Wrong credentials please try again"
            return render_template ('login.html',data=error) 
    else:
        return render_template('login.html')