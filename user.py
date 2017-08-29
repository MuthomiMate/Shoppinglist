import re

users = {};


class User(object):
    """
    Class to handle  user functions
    """

    def __init__(self, name=None, username=None, email=None, password=None):
        """ Initializing  class instance variables"""
        self.name = name
        self.email = email
        self.password = password

    def register(self, email, name, username, password, cpassword):
        """defining method to create account"""
        if name != '' and username and email != '' and password != '':
            if username not in users.keys():
                if email not in users.keys():
                    if password == cpassword:
                        regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
                        result = email
                        if re.search(regex, result):
                            users[email] = {
                            'name': name,
                            'username': username,
                            'email': email,
                            'pass': password,
                            }
                            print(users)
                            return 1
                        else:
                            return 2
                    else:
                        return 3
                else:
                    return 4
            else:
                return 5
        else:
            return 6
