from src.characters import Hero,Villain
from src.items import Item

class Area:
    """ zone de la carte, 
    peut être un sol et contenir un objet et un personnage
    ou être un mur et ne doit rien contenir.
    """
    def __init__(self,x,y,genre):
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
            self.Guard = Villain(int(line[1]),int(line[2]))

            f.readline()
            line = f.readline()
            #read items
            line = line.split("\t")
            item = Item(line[0],line[1],line[2])
            self.items.append(item)
            
            line = f.readline()
            line = line.split("\t")
            item = Item(line[0],line[1],line[2])
            self.items.append(item)
        
    def __str__(self):
        mapString = ""
        # a representation of the maze
        
        #mapString = "case: ({0};{1})\t\tMG({2};{3})".format(self.map[2][2].x,self.map[2][2].y,self.MG.x,self.MG.y)
        compteur=0
        for i in self.map:
            mapString+='{}\t'.format(compteur)
            for j in i:
                for k in self.items:
                    if k.x==j.x and k.y==j.y:
                        mapString+='O '
                    continue
                if self.Guard.x==j.x and self.Guard.y==j.y:
                    mapString += 'V '
                elif self.MG.x==j.x and self.MG.y==j.y:
                    mapString += 'G '
                else:
                    mapString+=j.genre+" "
            mapString+="\n"
            compteur+=1
        mapString+="\n"
        for i in self.items:
               mapString += "{}:\t{}\t{}".format(i.name,i.x,i.y)
        return mapString