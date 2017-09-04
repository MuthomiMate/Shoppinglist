import os
from user import User
from shoppinglists import Shoppinglist
from flask import  session, render_template, request, redirect, g, url_for
from app import app

newuser = User()
Newshoppinglist=Shoppinglist()
"""Instantiating objects"""
app.secret_key = os.urandom(24)


@app.route('/', methods=['GET', 'POST'])
def reg():
    """Handles the requests for the register view"""
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
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
            return render_template('dashboard.html', data=session)
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
            print(shoppinglistname)
            if result == 2:
                error = "that shopping list name already exists"
                result = Newshoppinglist.get_myshopping_lists(owner)
                shoppingitems = Newshoppinglist.getitems() 
                return render_template('dashboard.html', data=error,datas=result, items=shoppingitems)
            if result == 3:
                shoppingitems = Newshoppinglist.getitems()
 
                error = "Please fill all the fields"
                result = Newshoppinglist.get_myshopping_lists(owner) 
                return render_template('dashboard.html', data=error,datas=result, items=shoppingitems)                   
            if result == 1:
                result = Newshoppinglist.get_myshopping_lists(owner)
                shoppingitems = Newshoppinglist.getitems()  
                return render_template('dashboard.html', datas=result, items=shoppingitems)        
            return redirect('/login/')
        else:
            return render_template('dashboard.html')
    else:
        return render_template('login.html')

@app.route('/delete/')
def delete():
    """define route to delete a shoppinglist"""
    if g.user:
        res = Newshoppinglist.get_shopping_list(shoppinglistname)
        if res:
            result = Newshoppinglist.delete(shoppinglistname)
            if result == True:
                message = "successfully deleted"
                return render_template('dashboard.html', data=message)
            else:
                message = "shopping list was not deleted"
                return render_template('dashboard.html', data=message)               
        else:
            message = "not found"
            return render_template('dashboard.html', data=message)
    else:
        return render_template('login.html')

@app.route('/editshoppinglist/<shoppinglistname>')
def editshoppinglist(shoppinglistname):
    """defining route to get the post to edit"""
    if g.user:
        res = Newshoppinglist.get_shopping_list(shoppinglistname)
        if res:
            return render_template('dashboard.html', data=res)   
        return render_template('dashboard.html')
    else:
        return render_template('login.html')

@app.route('/editshopping/', methods=['GET', 'POST'])
def editshopping():
    """defining route to edit a shoppinglist"""
    if g.user:
        if request.method == "POST":
            old = request.form['old']
            sentence = request.form['shoppinglistname']
            Postlist = sentence.split(' ')
            shoppinglistname = ''.join(Postlist)
            owner = session['email']
            result = Newshoppinglist.edit(old, shoppinglistname, owner)
            if result == 1:
                message = "shopping list successfully updated"
                result = Newshoppinglist.get_myshopping_lists(owner)    
                return render_template('dashboard.html', msg=message)
            elif result == 2:
                return render_template('dashboard.html')  
            elif result ==3:
                msg="shopping list not found"
                return render_template('dashboard.html')
    else:
        return render_template('login.html')


@app.route('/createitem/', methods=['GET', 'POST'])
def additems():
    """Handles the  requests for creating an item"""
    if g.user:
        if request.method == "POST":
            sentence = request.form['shoppinglistname']
            itemlist = sentence.split(' ')
            shoppinglistname= ''.join(itemlist)
            itemname = request.form['itemname']
            owner = session['email']
            result = Newshoppinglist.createitem(shoppinglistname, itemname, owner)
            if result == 1:
                shoppingitems = Newshoppinglist.getitems()
                # print (shoppingitems)
                # print('yes')
                result = Newshoppinglist.get_myshopping_lists(owner)       
                return render_template('dashboard.html', datas=result, items=shoppingitems)           
            elif result == 2:
                shoppingitems = Newshoppinglist.getitems()
                message = "item already exists"
                result = Newshoppinglist.get_shopping_lists()       
                return render_template('dashboard.html',datase=result,items=shoppingitems, data=message)
            elif result == 3:
                shoppingitems = Newshoppinglist.getitems()
                message = "ishopping list does not exist"
                result = Newshoppinglist.get_shopping_lists()       
                return render_template('dashboard.html',datase=result,items=shoppingitems, data=message)
            elif result == 4:
                shoppingitems = Newshoppinglist.getitems()
                message = "shopping list does not exist"
                result = Newshoppinglist.get_shopping_lists()       
                return render_template('dashboard.html',datase=result,items=shoppingitems, data=message)
            elif result == 5:
                shoppingitems = Newshoppinglist.getitems()
                message = "Fill all the deatils"
                result = Newshoppinglist.get_shopping_lists()       
                return render_template('dashboard.html',datase=result,items=shoppingitems, data=message)

        else:
            return render_template('dashboard.html' )
    return render_template('login.html' )

@app.route('/edititem/', methods=['GET','POST'])
def edititem():
    """Handles  requests for editing an item"""
    if g.user:
        if request.method == "POST":
            sentence = request.form['item']
            itemlist = sentence.split(' ')
            item = ''.join(itemlist)
            post = request.form['itemname']
            old = request.form['old']
            owner = session['email']
            result = Newshoppinglist.itemedit(item, old)
            if result == 1:
                shoppingitems = Newshoppinglist.getitems()
                print(shoppingitems)
                result = Newshoppinglist.get_myshopping_lists(owner)        
                return render_template('dashboard.html', datas=result, items=shoppingitems)
            elif result == 2:
                return render_template('dashboard.html')
            else:
                return render_template('dashboard.html')  
        else:
            shoppingitems = Newshoppinglist.getitems()
            for dic in shoppingitems:
                result = Newshoppinglist.get_shopping_lists()       
                return render_template('dashboard.html', datas=result, items=shoppingitems)        
    else:
        return render_template('login.html')

@app.route('/deleteitem', methods=['GET', 'POST'])
def deleteitem():
    """Handles requests for deleting an item"""
    if g.user:
        item = request.form['shoppinglistname']
        itemname = request.form['itemname']
        owner = session['email']
        itemowner = session['email']
        result = Newshoppinglist.deleteitem(itemname)
        if result == True:
            message = "successfully deleted"
            shoppingitems = Newshoppinglist.getitems()
            results = Newshoppinglist.get_myshopping_lists(owner)           
            return render_template('dashboard.html', msg=message, datas=results, items=shoppingitems )
        else:
            return render_template('dashboard.html')
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    """Handles requests to logout a user"""
    session.pop('user', None)
    return redirect(url_for('logins'))