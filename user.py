import re

users = {}


class User(object):
    """
    Class to handle  user functions
    """

    def __init__(self, name=None, email=None, password=None):
        """ Initializing  class instance variables"""
        self.name = name
        self.email = email
        self.password = password

    def register(self, email, name, password, cpassword):
        """defining method to create account"""
        if re.match("[a-zA-Z0-9- .]+$",name):
            if name != '' and email != '' and password != '':
                if name not in users.keys():
                    if email not in users.keys():
                        if password == cpassword:
                            regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
                            regPass = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
                            result = email
                            if re.search(regex, result):
                                if re.search(regPass, password):
                                    users[email] = {
                                        'name': name,
                                        'email': email,
                                        'pass': password,
                                    }
                                    return 1
                                return 7

                            return 2
                        return 3
                    return 4
                return 5
            return 6
        return 8


    def login(self, email, password):
        """ defining method to Log in user"""
        if email != '' and password != '':
            if email in users.keys():
                result = users[email]
                pword = result['pass']
                if pword == password:
                    return 1
                return 2
            return 3
        return 4

    def get_user_name(self, email):
        if email in users.keys():
            result = users[email]
            return result['name']
        return False

    def get_user_email(self, email):
        if email in users.keys():
            result = users[email]
            return result['email']
        return False
