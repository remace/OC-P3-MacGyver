class Character:
    def __init__(self,x,y,direction):
        self.x = x
        self.y = y
        self.direction = direction


class Hero(Character):
    """class defining a hero, mainly MacGyver in this game"""
    def __init__(self,x,y,direction):
        print('coucou')
        pass

class Villain(Character):
    def __init__(self,x,y,direction,name):
        pass
    def __del__(self):
        pass
