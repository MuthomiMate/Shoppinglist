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

    def tests_edit_shoppinglis(self):
        """defining method to test for editing a shoppinglist"""
        self.shoppings.Shoppinglists = {} 
        self.shoppings.create('muthomi', 'muthomi@gmail.com')
        output = self.shoppings.edit('muthomi', 'mate', 'muthomi@gmail.com')
        self.assertEqual(1, output, "shopping list successfully edited")

    def tests_edit_null_title(self):
        """defining method to test for editing a shoppinglist and leaving the name null"""
        self.shoppings.Shoppinglists = {} 
        self.shoppings.create('muthomi', 'muthomi@gmail.com')
        output = self.shoppings.edit('muthomi', '', 'muthomi@gmail.com')
        self.assertEqual(2,output,"Please fill the name field")

    def tests_edit_name_not_found(self):
        """defining method to test for editing a shoppinglist and leaving the name null"""
        self.shoppings.Shoppinglists = {} 
        self.shoppings.create('muthomi', 'muthomi@gmail.com')
        output = self.shoppings.edit('mate', 'mwiti', 'muthomi@gmail.com')
        self.assertEqual(3,output,"Please fill the name field")

    def tests_Add_item(self):
        """defining method to test adding an item in a shoppinglist"""
        self.shoppings.ShoppingItems = []
        current_count = len(self.shoppings.ShoppingItems)
        output = self.shoppings.createitem('muthomi', 'muthomi','muthomi@gmail.com')
        self.assertEqual(current_count+1, output, "Item successfully added")

    def tests_addEmpty_item(self):
        """defining method to test adding an empty item in a shoppinglist"""
        self.shoppings.ShoppingItems = []
        output = self.shoppings.createitem('', 'mate','muthomi@gmail.com')
        self.assertEqual(2,output,"Cannot add an empty item ") 
    def tests_delete_null_item(self):
        """defining method to test deleting an item that doesn't exist in a shoppinglist"""
        self.shoppings.ShoppingItems = []
        self.shoppings.createitem('mate', 'mate','muthomi@gmail.com')
        output = self.shoppings.deleteitem('fish')
        self.assertEqual(2, output, "Cannot Delete an item that does not exist") 

    def tests_delete_items(self):
        """defining method to test deleting an  existing item"""
        self.shoppings.ShoppingItems = []
        item = self.shoppings.createitem('mate', 'mate','muthomi@gmail.com')
        output = self.shoppings.deleteitem(item)
        self.assertEqual(2, output, "Item successfully deleted") 

    def tests_edit_item(self):
        """defining method to test editing an  existing item"""
        self.shoppings.ShoppingItems = []
        self.shoppings.createitem('mate', 'mate','muthomi@gmail.com')
        output = self.shoppings.itemedit('mate', 'mate')
        self.assertEqual(1, output, "Item successfully edited")

    def tests_edit_null_item(self):
        """defining method to test editing an empty item field"""
        self.shoppings.Shoppingitems = []
        self.shoppings.createitem('mate', 'mate', 'muthomi@gmail.com')
        output = self.shoppings.itemedit('', 'mate')
        self.assertEqual(2, output, "The item can not be empty")    

if __name__ == "__main__":
    unittest.main()        