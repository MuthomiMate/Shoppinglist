import sys
import unittest

from user import User


class Usertest(unittest.TestCase):
    """
        Class containing all the test in class user
    """

    def setUp(self):
        """Defining setUp() method that runs prior to each test."""
        self.newUser = User()

    def test_create_account(self):
        """defining method to test for creating user account"""
        self.newUser.users = {}
        current_count = len(self.newUser.users)
        result = self.newUser.register( 'muthomi@gmail.com', 'muthomi', 'muthomi', 'pass', 'pass')
        self.assertEqual(current_count+1, result, "User succesfully created")   

    def test_register_null_name(self):
        """defining method to test for creating user account with an empty name field"""
        output=self.newUser.register('muthomi@gmail.com','', 'muthomi', 'pass','pass')
        self.assertEqual(6, output, "Please fill your name")

    def test_register_null_username(self):
        """defining method to test for created user account with an empty username field"""
        output=self.newUser.register('muthomi@gmail.com','muthomi', '', 'pass','pass')    
        self.assertEqual(6, output, "Username is empty")

    def test_register_null_email(self):
        """defining method to test for creating user account with an empty email"""
        output=self.newUser.register('','muthomi', 'muthomi','pass','pass')
        self.assertEqual(6, output, "Email is Empty ")    
        
    def test_null_password(self):
        """ defining method to test for creating user account with an empty passsword field"""
        output=self.newUser.register('muthomi@gmail.com','muthomi', 'muthomi', '','pass')
        self.assertEqual(6, output, "Please the password filed") 
 
    def test_cpassword_is_password(self):
        """defining method to test for created user's password is equal to confirm password"""
        output=self.newUser.register('muthomi@gmail.com','muthomi', 'muthomi', 'pass','pas')    
        self.assertEqual(3, output, "password mismatch")

    def test_existing_useremail(self):
        """defining method to test for an existing user email """
        self.newUser.users = {}
        self.newUser.register('muthomi@gmail.com','muthomi', 'muthom', 'pass','pass')
        result = self.newUser.register('muthomi@gmail.com','muthomi', 'muthomi', 'pass','pass')
        self.assertEqual(4, result, "Email already registered")

    # def test_existing_username(self):
    #     """defining method to test if username has already been taken """
    #     self.newUser.users = {}
    #     self.newUser.register('muthomi@gmail.com','muthomi', 'muthomi', 'pass','pass')
    #     result = self.newUser.register('muthom@gmail.com','muthomi', 'muthomi', 'pass','pass')
    #     self.assertEqual(5, result, "username has already been taken")
    
		