class Item:
    """    Item class is a representation for menu items."""
    def __init__(self, name, price):  
        """define what item is with init dunder """
        self.name = name
        self.price = price

    def __repr__(self):  # if call directly. overrides the system default "reper" (representation) 
        return f'[Item: {self.name}, ${self.price}]'

    def __str__(self):  # if in f string. overrides the system default "reper" (representation) 
        return f'[Item: {self.name}, ${self.price}]'

    def change_price(self, new_price):
        self.price = abs(new_price)
    
    def change_name(self, new_name):
        self.name = str(new_name)

class Menu:
    """ To collect a list of menu items """
    def __init__(self, contents=[]):
        self.contents = contents
    
    def __repr__(self):
        return f'Menu: {self.contents}'
    
    def add_item(self, to_add):
        if isinstance(to_add, Item):
            self.contents.append(to_add)
        else:
            to_add = False
        return to_add
    
    def read(self): 
        # Reads the menu
        return (self.contents)
    
    def remove_item(self, to_remove):
        if to_remove in self.contents:
            index = self.contents.index(to_remove)
            self.contents.pop(index)
        else:
            to_remove = False        
        return to_remove


new_menu = Menu()
print(new_menu)

new_item = Item("Apple", 9.99)

print(new_item)

new_menu.add_item(new_item)
print(new_menu.read())

new_menu.remove_item(new_item)
print(new_menu.read())