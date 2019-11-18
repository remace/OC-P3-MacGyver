from src.character import *

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
                
            line = f.readline()
            line = f.readline()
            line=line.split("\t")
            self.MG = Hero(int(line[1]),int(line[2]))
            line=f.readline()
            line=line.split("\t")
            self.Guard = Villain(int(line[1]),int(line[2]))

            #print("MacGyver ({0};{1})".format(self.MG.x,self.MG.y))
        
    def __str__(self):
        mapString = ""
        # a representation of the maze
        
        #mapString = "case: ({0};{1})\t\tMG({2};{3})".format(self.map[2][2].x,self.map[2][2].y,self.MG.x,self.MG.y)
        for i in self.map:
            for j in i:
                if self.Guard.x==j.x and self.Guard.y==j.y:
                    mapString += 'H '
                elif self.MG.x==j.x and self.MG.y==j.y:
                    mapString += 'G '
                else:
                    mapString+=j.genre+" "
            mapString+="\n"
        return mapString