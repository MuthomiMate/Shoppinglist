import os
from user import User
from shoppinglists import Shoppinglist
from flask import session, render_template, request, redirect, g, url_for
from app import app

newuser = User()
Newshoppinglist = Shoppinglist()
"""Instantiating objects"""
app.secret_key = os.urandom(24)


@app.route('/', methods=['GET', 'POST'])
def register():
    """Handles the requests for the register view"""
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['cpassword']
        result = newuser.register(email, name, password, cpassword)
        if result == 1:
            session['user'] = name
            message = "Account created sucessfully"
            return render_template('login.html', data=message)

        elif result == 6:
            message = ("please fill all the fields")
            return render_template('register.html', data=message)
        elif result == 8:
            message = ("Special characters not allowed in field name")
            return render_template('register.html', data=message)
        elif result == 7:
            message = (
                "Password should have minimum eight characters, at least one letter and one number")
            return render_template('register.html', data=message)
        elif result == 5:
            message = ("Username has alredy been taken")
            return render_template('register.html', data=message)
        elif result == 3:
            message = ("password do not match")
            return render_template('register.html', data=message)
        elif result == 2:
            error = "email must be a valid email"
            return render_template('register.html', data=error)
        elif result == 4:
            error = "email already registered"
            return render_template('register.html', data=error)
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
            owner = session['email']
            result = Newshoppinglist.get_myshopping_lists(owner)
            shoppingitems = Newshoppinglist.getitems()
            error = "login sucessful"
            return render_template('dashboard.html', success=error, datas=result, items=shoppingitems,
                                   owner=owner)
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
            return render_template('login.html', data=error)
    return render_template('login.html')


@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']


@app.route('/create/', methods=['GET', 'POST'])
def createshoppinglist():
    """Handles creation of shoppinglists"""
    if g.user:
        if request.method == "POST":
            sentence = request.form['shoppinglistname']
            Postlist = sentence.split(' ')
            shoppinglistname = ''.join(Postlist)
            owner = session['email']
            result = Newshoppinglist.create(shoppinglistname, owner)
            if result == 2:
                error = "that shopping list name already exists"
                result = Newshoppinglist.get_myshopping_lists(owner)
                shoppingitems = Newshoppinglist.getitems()
                return render_template('dashboard.html', data=error, datas=result,
                                       items=shoppingitems, owner=owner)
            if result == 3:
                shoppingitems = Newshoppinglist.getitems()

                error = "Please fill all the fields"
                result = Newshoppinglist.get_myshopping_lists(owner)
                return render_template('dashboard.html', data=error, datas=result,
                                       items=shoppingitems, owner=owner)
            if result == 4:
                shoppingitems = Newshoppinglist.getitems()

                error = "Special characters not allowed"
                result = Newshoppinglist.get_myshopping_lists(owner)
                return render_template('dashboard.html', data=error, datas=result,
                                       items=shoppingitems, owner=owner)
            if result == 1:
                result = Newshoppinglist.get_myshopping_lists(owner)
                shoppingitems = Newshoppinglist.getitems()
                return render_template('dashboard.html', datas=result,
                                       items=shoppingitems, owner=owner)
            return redirect('/login/')
        return render_template('dashboard.html')
    return render_template('login.html')


@app.route('/delete/', methods=['GET', 'POST'])
def delete():
    """define route to delete a shoppinglist"""
    if g.user:
        if request.method == "POST":
            sentence = request.form['shoppinglistname']
            Postlist = sentence.split(' ')
            owner = owner = session['email']
            shoppinglistname = ''.join(Postlist)
            res = Newshoppinglist.get_shopping_list(shoppinglistname)
            if res:
                result = Newshoppinglist.delete(shoppinglistname)
                if result == 1:
                    message = "successfully deleted"
                    result = Newshoppinglist.get_myshopping_lists(owner)
                    shoppingitems = Newshoppinglist.getitems()
                    return render_template('dashboard.html', success=message, datas=result,
                                           items=shoppingitems, owner=owner)
                else:
                    message = "Not successfully deleted"
                    result = Newshoppinglist.get_myshopping_lists(owner)
                    shoppingitems = Newshoppinglist.getitems()
                    return render_template('dashboard.html', success=message, datas=result,
                                           items=shoppingitems, owner=owner)
            else:
                message = "not found"
                result = Newshoppinglist.get_myshopping_lists(owner)
                shoppingitems = Newshoppinglist.getitems()
                return render_template('dashboard.html', data=message, datas=result,
                                       items=shoppingitems, owner=owner)
        return render_template('dashboard.html')
    return render_template('login.html')


@app.route('/editshoppinglist/<shoppinglistname>')
def editshoppinglist(shoppinglistname):
    """defining route to get the post to edit"""
    if g.user:
        res = Newshoppinglist.get_shopping_list(shoppinglistname)
        if res:
            return render_template('dashboard.html', data=res)
        return render_template('dashboard.html')
    return render_template('login.html')


@app.route('/editshopping/', methods=['GET', 'POST'])
def editshopping():
    """defining route to edit a shoppinglist"""
    if g.user:
        if request.method == "POST":
            old = request.form['old']
            sentence = request.form['shoppinglistname']
            postlist = sentence.split(' ')
            shoppinglistname = ''.join(postlist)
            owner = session['email']
            result = Newshoppinglist.edit(old, shoppinglistname, owner)
            if result == 1:
                message = "shopping list successfully updated"
                result = Newshoppinglist.get_myshopping_lists(owner)

                shoppingitems = Newshoppinglist.getitems()
                return render_template('dashboard.html', success=message,
                                       datas=result, items=shoppingitems, owner=owner)
            elif result == 2:
                message = "shopping list not found"
                result = Newshoppinglist.get_myshopping_lists(owner)
                shoppingitems = Newshoppinglist.getitems()
                return render_template('dashboard.html', data=message,
                                       datas=result, items=shoppingitems, owner=owner)
            elif result == 3:
                result = Newshoppinglist.get_myshopping_lists(owner)
                shoppingitems = Newshoppinglist.getitems()
                message = "shopping list not found"
                return render_template('dashboard.html', data=message,
                                       datas=result, items=shoppingitems, owner=owner)
            elif result == 4:
                result = Newshoppinglist.get_myshopping_lists(owner)
                shoppingitems = Newshoppinglist.getitems()
                message = "special characters not allowed"
                return render_template('dashboard.html', data=message,
                                       datas=result, items=shoppingitems, owner=owner)
    return render_template('login.html')


@app.route('/createitem/', methods=['GET', 'POST'])
def additems():
    """Handles the  requests for creating an item"""
    if g.user:
        if request.method == "POST":
            sentence = request.form['shoppinglistname']
            itemlist = sentence.split(' ')
            shoppinglistname = ''.join(itemlist)
            itemname = request.form['itemname']
            owner = session['email']
            result = Newshoppinglist.createitem(
                shoppinglistname, itemname, owner)
            if result == 1:
                shoppingitems = Newshoppinglist.getitems()
                result = Newshoppinglist.get_myshopping_lists(owner)
                return render_template('dashboard.html', datas=result, items=shoppingitems, owner=owner)
            elif result == 2:
                shoppingitems = Newshoppinglist.getitems()
                message = "item already exists"
                result = Newshoppinglist.get_myshopping_lists(owner)
                return render_template('dashboard.html', datas=result,
                                       items=shoppingitems, data=message, owner=owner)
            elif result == 3:
                shoppingitems = Newshoppinglist.getitems()
                message = "Special characters not allowed"
                result = Newshoppinglist.get_myshopping_lists(owner)
                return render_template('dashboard.html', datas=result,
                                       items=shoppingitems, data=message, owner=owner)
        return render_template('dashboard.html')
    return render_template('login.html')


@app.route('/edititem/', methods=['GET', 'POST'])
def edititem():
    """Handles  requests for editing an item"""
    if g.user:
        if request.method == "POST":
            sentence = request.form['item']
            itemlist = sentence.split(' ')
            item = ''.join(itemlist)
            old = request.form['old']
            owner = session['email']
            result = Newshoppinglist.itemedit(item, old)
            if result == 1:
                shoppingitems = Newshoppinglist.getitems()
                message = "edited successfully"
                result = Newshoppinglist.get_myshopping_lists(owner)

                return render_template('dashboard.html', success=message, items=shoppingitems,
                                       datas=result, owner=owner)
            elif result == 2:
                shoppingitems = Newshoppinglist.getitems()
                result = Newshoppinglist.get_myshopping_lists(owner)
                return render_template('dashboard.html')
            shoppingitems = Newshoppinglist.getitems()
            result = Newshoppinglist.get_myshopping_lists(owner)
            return render_template('dashboard.html', datas=result,
                                   items=shoppingitems, owner=owner)
        else:
            shoppingitems = Newshoppinglist.getitems()
            result = Newshoppinglist.get_shopping_lists()
            return render_template('dashboard.html', datas=result,
                                   items=shoppingitems, owner=owner)
    return render_template('login.html')


@app.route('/deleteitem', methods=['GET', 'POST'])
def deleteitem():
    """Handles requests for deleting an item"""
    if g.user:
        shoppinglistname = request.form['shoppinglistname']
        itemname = request.form['itemname']
        owner = session['email']
        result = Newshoppinglist.deleteitem(itemname, shoppinglistname)
        if result == 1:
            message = "successfully deleted"
            shoppingitems = Newshoppinglist.getitems()
            results = Newshoppinglist.get_myshopping_lists(owner)
            return render_template('dashboard.html', success=message,
                                   datas=results, items=shoppingitems, owner=owner)
        else:
            message = "Item not deleted"
            shoppingitems = Newshoppinglist.getitems()
            results = Newshoppinglist.get_myshopping_lists(owner)
            return render_template('dashboard.html', data=message,
                                   datas=results, items=shoppingitems, owner=owner)
    return render_template('login.html')


@app.route('/logout')
def logout():
    """Handles requests to logout a user"""
    session.pop('user', None)
    return redirect(url_for('logins'))
