from src.areas import *
#from src.character import *

maze = Maze("maze.txt")
exit = False
while exit==False: 
    print(maze)
    dir = input("quelle direction?")
    if dir == "z":
        maze.MG.y-=1
        print("mouvement vers le haut")
    elif dir=="q":
        maze.MG.x-=1
        print("mouvement vers la gauche")
    elif dir == "s":
        maze.MG.y+=1
        print("mouvement vers le bas")
    elif dir == "d":
        maze.MG.x+=1
        print("mouvement vers la droite")
    else:
        exit = True
        