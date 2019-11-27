from src.characters import Hero,Villain
from src.items import Item

class Area:
    """ zone de la carte, 
    peut être un sol et contenir un objet et un personnage
    ou être un mur et ne doit rien contenir.
    """
    def __init__(self, x, y, genre):
        self.x = x
        self.y = y
        #trouver un nom en anglais pour "sol ou mur"
        self.genre = genre
    
    def __str__(self):
        return self.genre+" "



class Maze:
    
    def __init__(self,chemin):
        #create an array that contains each area of the maze
        self.map = list(list())
        self.items = list()
        #read the maze.txt file to get the map, each area
        with open('maze.txt', 'r') as f:
            for i in range(10):
                line = f.readline()
                lineList = list()
                j=0
                for char in line:                    
                    if char==" " or char=="\n":
                        continue
                    else:
                        lineList.append(Area(j,i,char))
                    j+=1
                self.map.append(lineList)
                
            f.readline()
            line = f.readline()
            #read characters
            line=line.split("\t")
            self.MG = Hero(int(line[1]),int(line[2]))
            line=f.readline()
            line=line.split("\t")
            self.Guard = Villain(int(line[1]),int(line[2]),line[3],line[4],line[5])

            f.readline()
            #read items
            for i in range(3):
                line = f.readline()
                line = line.split("\t")
                item = Item(line[0],int(line[1]),int(line[2]))
                self.items.append(item)

    def __str__(self):
        map_string = ""
        # a representation of the maze
        count=0
        for i in self.map:
            map_string+='{}\t'.format(count)
            for j in i:
                hasItem = False
                for k in self.items:
                    if k.x==j.x and k.y==j.y:
                        hasItem = True
                        break
                if self.MG.x==j.x and self.MG.y==j.y:
                    map_string += 'G '
                elif self.Guard.x==j.x and self.Guard.y==j.y:
                    map_string += 'V '
                elif hasItem == True:
                    map_string += 'O '
                else:
                    map_string+=j.genre+" "
            map_string+="\n"
            count+=1
        map_string+="\n"
        for i in self.items:
            if i.x==self.MG.x and self.MG.y==i.y:
                map_string += "lying on the floor, waiting to be gathered: {}".format(i.name)
        
        #printing items location
        for i in self.items:
            print("{}:({};{})".format(i.name,i.x,i.y))


        #printing the inventory
        map_string += ('\ninventory: \n')
        for i in self.MG.inventory:
            map_string += "{}\n".format(i)
        return map_string
    
    def test_victoire(self):
        missing_item = False
        for i in self.Guard.deathItems:
            item_in_inventory = False
            for j in self.MG.inventory:
                if i == j:
                    item_in_inventory = True
                    break
            if not item_in_inventory:
                print("You Lost!")
                missing_item = True
                break
        if not missing_item:
            print("You Won!")