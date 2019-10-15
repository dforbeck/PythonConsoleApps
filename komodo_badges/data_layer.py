
class Badge:
    """ To collect a list of doors to access """
# initialize badge class
    def __init__(self, badge_id, doors =[]):
        self.badge_id
        self.doors = doors

# add a door to a badge

    def add_door(self, to_add):
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