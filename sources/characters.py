"""module definition for the characters classes"""


class Character:
    """abstract class about characters like Mac Gyver and the Villain"""

    def __init__(self, x, y):
        """constructor"""
        self.x = x
        self.y = y


class Hero(Character):
    """class defining a hero, mainly Mac Gyver in this game"""
    def __init__(self, x, y):
        """constructor for a Hero"""
        super().__init__(x, y)
        self.name = "Mac Gyver"
        self.inventory = {}
    
    def move(self, dir):
        if dir=="NORTH":
            self.y -= 1
        elif dir == "SOUTH":
            self.y += 1
        elif dir == "WEST":
            self.x -= 1
        elif dir == "EAST":
            self.x += 1

    def gather_item(self, i):
        """gather an Item on the floor at the position of the hero.
        i is an Item"""
        self.inventory[i.name] = [i.x, i.y]


class Villain(Character):
    """class defining a Villain, mainly the keeper"""
    def __init__(self, name, x, y, di1, di2, di3):
        """constructor for a villain"""
        super().__init__(x, y)
        self.name = name
        self.death_items = []
        self.death_items.append(di1)
        self.death_items.append(di2)
        self.death_items.append(di3)
