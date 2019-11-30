"""module definition for the characters classes"""
class Character:
    """abstract class about characters like Mac Gyver and the Villain"""
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Hero(Character):
    """class defining a hero, mainly MacGyver in this game"""
    def __init__(self, x, y):
        """constructor for a Hero"""
        Character.__init__(self, x, y)
        self.name = "Mac Gyver"
        self.inventory = {}

    def gather_item(self, i):
        """gather an Item on the floor at the position of the hero.
        i is an Item"""
        self.inventory[i.name] = [i.x, i.y]


class Villain(Character):
    """class defining a Villain, mainly the keeper"""
    def __init__(self, name, x, y, di1, di2, di3):
        """constructor for a villain"""
        Character.__init__(self, x, y)
        self.name = name
        self.death_items = []
        self.death_items.append(di1)
        self.death_items.append(di2)
        self.death_items.append(di3)
