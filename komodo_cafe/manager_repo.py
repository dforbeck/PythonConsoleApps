from data_layer import Menu, Item

current_menu = Menu()

def read_menu(): # option 1 refactored
    return current_menu.read()

def create_item(name, price): # option 2 refactored
    new_item = Item(name, price)
    current_menu.add_item(new_item)
    return f"{new_item} successfully added."

def change_item(index, name, price):
    to_edit = current_menu.contents[index]
    price = float(price or to_edit.price)  
    # had to convert here to a float in case blank in question
    if name:
        to_edit.change_name(name)
    if price:
        to_edit.change_price(price)
    return f'{to_edit} was successfully modified.'
