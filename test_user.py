import unittest

from user import User

class UsersTest(unittest.TestCase):
	def setUp(self):
		self.mimi=User()


"""tests if the email is correct"""
	def email_test(self):
		self.assertEqual(self.mimi.email, 'muthomimate@gmail.com', msg='Invalid email')

"""tests if the pname is correct"""
	def name_test(self):
		self.assertEqual(self.mimi.name, 'muthomi', msg='Invalid name')

"""tests if the password is correct"""	
	def password_test(self):
		self.assertEqual(self.mimi.password, 'muthomi', msg='Invalid Password')

"""tests if the username is correct"""	
	def username_test(self):
		self.assertEqual(self.mimi.username, 'muthomi', msg='Invalid Username')
		