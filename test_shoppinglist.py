import sys

import unittest
from shoppinglists import Shoppinglist

class Shoppingtest(unittest.TestCase):
    """
       Class performing unit testing for class ShoppingList
    """
       
    def setUp(self):
        """Defining setUp() method that runs prior to each test."""
        self.shoppings = Shoppinglist()       
        self.shoppings.Shoppinglists = {}

    def test_for_creating_a_shoppinglist(self):
        """ defining method to test for Creating a shopping list """
        current_count = len(self.shoppings.Shoppinglists)
        output = self.shoppings.create('Shoppinglist 1', 'muthomi@gmail.com')
        self.assertEqual(current_count+1, output, "Shopping list successfully created")

    def test_if_name_empty(self):
        """defining method to test for adding a shopping list with an empty title """
        output = self.shoppings.create('', 'owner')
        self.assertEqual(3, output, "please fill all fields")

    def tests_if_shopping_exists(self):
        """defining method to test for adding a shopping list That already exists """
        self.shoppings.create('muthomi', 'muthomi@gmail.com')
        output = self.shoppings.create('muthomi', 'muthomi@gmail.com')
        self.assertEqual(2, output, "That shopping list already exists!") 

    def tests_delete_shoppinglist(self):
        """defining method to test for deleting a shoppinglist"""
        self.shoppings.Shoppinglists = {}
        self.shoppings.create('muthomi', 'muthomi@gmail.com')
        output = self.shoppings.delete('muthomi')
        self.assertEqual(1, output, "Succesfully deleted!")

    def tests_delete_an_unavailable_shoppinglist(self):
        """defining method to test for deleting a shopping list that does not exist""" 
        self.shoppings.Shoppinglists = {}
        self.shoppings.create('muthomi', 'muthomi@gmail.com')
        output = self.shoppings.delete('nnnnnn')
        self.assertEqual(2, output, "You can not delete a shopping list that does not exist")    