from src.areas import Maze

maze = Maze("maze.txt")
exit = False
while exit==False: 
    print(maze)
    action = input("quelle action?")
    if action == "z":
        if maze.map[maze.MG.y-1][maze.MG.x].genre!="M":
            maze.MG.y-=1
            print("mouvement vers le haut")
        else:
            print("Ouch! There's a Wall!")
    elif action=="q":
        if maze.map[maze.MG.y][maze.MG.x-1].genre!="M":
            maze.MG.x-=1
            print("mouvement vers la gauche")
        else:
            print("Ouch! There's a Wall!")
    elif action == "s":
        if maze.map[maze.MG.y+1][maze.MG.x].genre!="M":
            maze.MG.y+=1
            print("mouvement vers le bas")
        else:
            print("Ouch! There's a Wall!")
    elif action == "d":
        if maze.map[maze.MG.y][maze.MG.x+1].genre!="M":
            maze.MG.x+=1
            print("mouvement vers la droite")
        else:
            print("Ouch! There's a Wall")
    elif action=="e":
        compteur=0
        for i in maze.items:
            if i.x==maze.MG.x and i.y==maze.MG.y:
                maze.MG.gatherItem(i)
                maze.items.remove(i)
                print('objet ramassé: {}'.format(i.name))
                compteur+=1
        if compteur==0:
            print('aucun objet à ramasser!')
    else:
        exit = True