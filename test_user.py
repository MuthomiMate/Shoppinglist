import unittest

from user import User

class UsersTest(unittest.TestCase):
	def setUp(self):
		self.mimi=User()

	def email_test(self):
		self.assertEqual(self.mimi.email, 'muthomimate@gmail.com', msg='Invalid email')

	
		