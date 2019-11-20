cleafrom src.areas import Maze

maze = Maze("maze.txt")
exit = False
while exit==False: 
    print(maze)
    dir = input("quelle direction?")
    if dir == "z":
        if maze.map[maze.MG.y-1][maze.MG.x].genre!="M":
            maze.MG.y-=1
            print("mouvement vers le haut")
        else:
            print("Ouch! There's a Wall!")
    elif dir=="q":
        if maze.map[maze.MG.y][maze.MG.x-1].genre!="M":
            maze.MG.x-=1
            print("mouvement vers la gauche")
        else:
            print("Ouch! There's a Wall!")
    elif dir == "s":
        if maze.map[maze.MG.y+1][maze.MG.x].genre!="M":
            maze.MG.y+=1
            print("mouvement vers le bas")
        else:
            print("Ouch! There's a Wall!")
    elif dir == "d":
        if maze.map[maze.MG.y][maze.MG.x+1].genre!="M":
            maze.MG.x+=1
            print("mouvement vers la droite")
        else:
            print("Ouch! There's a Wall")
    else:
        exit = True