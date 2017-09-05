Shoppingitems= []
"""an empty list to store my items"""

class Shoppinglist(object):
    Shoppinglists = {}
    """an empty list to store my shoppinglists"""
    def __init__(self, shoppinglistname=None, owner=None, itemname=None):
        """initializing class instance variables"""
        self.shoppinglistname = shoppinglistname
        self.itemname=itemname
        self.owner = owner

    def create(self, shoppinglistname, owner):
        """defining method to create shopping list"""
        if shoppinglistname != '':
            #call the get_myshopping_lists function that contains individual user shoppinglists 
            my_shoppings = self.get_myshopping_lists(owner)
            if my_shoppings != {}:
                #check's if user already has a shopping list
                if shoppinglistname not in my_shoppings.keys():
                    self.Shoppinglists[shoppinglistname] = {
                    'shoppinglistname':shoppinglistname,
                    'owner':owner,
                    }
                    return 1
                else:
                    return 2
            else:
                #user's first shopping list
                self.Shoppinglists[shoppinglistname] = {
                'shoppinglistname':shoppinglistname,
                'owner':owner,
                }
                return 1
        else:
            return 3

    def get_myshopping_lists(self, owner):
        """defining method to get one user's shopping lists"""
        data = self.Shoppinglists
        my_shoppings = {}
        for shoppinglistname in data.keys():
            #loop through the shoppinglistnames in the shopping list and assign the dictionary to variables
            shopping = data[shoppinglistname]
            shoppingowner = shopping['owner']
            if shoppingowner == owner:
                my_shoppings[shoppinglistname] = {
                'shoppinglistname': shoppinglistname,
                'owner': owner,
                }
            else:
                result = my_shoppings
        return my_shoppings

    def delete(self, shoppinglistname):
        """defining method to delete shopping list"""
        if shoppinglistname in self.Shoppinglists.keys():
            #checks if the shoppinglistname being deleted exists
            del self.Shoppinglists[shoppinglistname]
            return 1
        else:
            return 2

    def get_shopping_lists(self):
        """defining method to get all shopping lists"""
        return self.Shoppinglists

    def get_shopping_list(self, shoppinglistname):
        """defining method to get one shopping lists"""
        return self.Shoppinglists[shoppinglistname]

    def edit(self, old, shoppinglistname, owner):
        """defining method to edit shopping list"""
        if  shoppinglistname != '':
            if old in self.Shoppinglists.keys():
                del self.Shoppinglists[old]
                self.Shoppinglists[shoppinglistname] = {
                    'shoppinglistname' : shoppinglistname,
                    'owner' : owner,
                    }
                return 1
            else:
                return 3
        else:
            return 2

    def createitem(self, itemname, shoppinglistname,owner):
        if itemname != '':
            Shoppingitems.append({'shoppinglistname': shoppinglistname, 'itemname': itemname})
            return 1
        return 2
        """defining method to create an item in a shopping list"""
        # if shoppinglistname != '' and itemname != '':
        #     my_shoppings = self.get_myshopping_lists(owner)
        #     if my_shoppings != {}:
        #         #check's if user already has a shopping list
        #         if shoppinglistname in self.Shoppinglists.keys():
        #             for dic in range(len(Shoppingitems)):

        #                 if Shoppingitems[dic]['itemname'] != itemname :
        #                     Shoppingitems.append({'shoppinglistname': shoppinglistname, 'itemname': itemname})
        #                     return 1
        #                 return 2
        #             return Shoppingitems.append({'shoppinglistname': shoppinglistname, 'itemname': itemname})
        #         return 3
        #     return 4
        # return 5    
    def getitems(self):
        """ defining method to delete an item from shopping list"""
        return Shoppingitems

    def itemedit(self, itemname, old):
        """defining method to edit an item in a shopping"""
        if itemname != "":
            for dic in range(len(Shoppingitems)):
                if Shoppingitems[dic]['itemname'] == old:
                    del Shoppingitems[dic]['itemname']
                    Shoppingitems[dic]['itemname'] = itemname
                    return 1
        else:
            return 2

    def deleteitem(self,itemname):
        """ defining method to delete an item from shopping"""
        for dic in range(len(Shoppingitems)):
            if Shoppingitems[dic]['itemname'] == itemname:
                del Shoppingitems[dic]
                result = 1
            else:
                result = 2

        return result   



 