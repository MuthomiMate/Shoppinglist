import unittest

from user import User

class UsersTest(unittest.TestCase):
	def setUp(self):
		self.mimi=User()

	def email_test(self):
		self.assertEqual(self.mimi.email, 'muthomimate@gmail.com', msg='Invalid email')

	def name_test(self):
		self.assertEqual(self.mimi.name, 'muthomi', msg='Invalid name')
	
	def password_test(self):
		self.assertEqual(self.mimi.password, 'muthomi', msg='Invalid Password')

	def username_test(self):
		self.assertEqual(self.mimi.username, 'muthomi', msg='Invalid Username')
		