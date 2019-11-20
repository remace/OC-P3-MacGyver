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
        

class Villain(Character):
    def __init__(self,x,y):
        self.name="Garde"
        self.x = x
        self.y = y

    def __del__(self):
        pass
