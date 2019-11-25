class Character:
    def __init__(self,x,y):
        self.x = x
        self.y = y


class Hero(Character):
    """class defining a hero, mainly MacGyver in this game"""
    def __init__(self,x,y):
        self.name="Mac Gyver"
        self.x = x
        self.y = y
        self.inventory = {}
    
    def gatherItem(self, i):
        """gather an Item on the floor at the position of the hero.
        i is an Item"""
        self.inventory[i.name]=[i.x,i.y]
        

class Villain(Character):
    def __init__(self,x,y,di1,di2):
        self.name="Garde"
        self.x = x
        self.y = y
        self.deathItems=[]
        self.deathItems.append(di1)
        self.deathItems.append(di2)

    def __del__(self):
        pass
