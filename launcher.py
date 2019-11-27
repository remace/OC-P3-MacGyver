from src.areas import Maze

maze = Maze("maze.txt")
exit = False
while exit==False: 
    print(maze)
    action = input("which action?\n(zqsd for a movement, e for gathering what lies on the floor, then press enter)\n")
    if action == "z":
        if maze.map[maze.MG.y-1][maze.MG.x].genre!="M":
            maze.MG.y-=1
            print("moving to the north")
        else:
            print("Ouch! There's a Wall!")
        if maze.MG.x==maze.Guard.x and maze.MG.y == maze.Guard.y:
            maze.test_victoire()
            exit = True
        
    elif action=="q":
        if maze.map[maze.MG.y][maze.MG.x-1].genre!="M":
            maze.MG.x-=1
            print("moving to the west")
        else:
            print("Ouch! There's a Wall!")
        if maze.MG.x==maze.Guard.x and maze.MG.y == maze.Guard.y:
            maze.test_victoire()
            exit = True
        
    elif action == "s":
        if maze.map[maze.MG.y+1][maze.MG.x].genre!="M":
            maze.MG.y+=1
            print("moving to the south")
        else:
            print("Ouch! There's a Wall!")
        if maze.MG.x==maze.Guard.x and maze.MG.x == maze.Guard.y:
            maze.test_victoire()
            exit = True
        
    elif action == "d":
        if maze.map[maze.MG.y][maze.MG.x+1].genre!="M":
            maze.MG.x+=1
            print("moving to the east")
        else:
            print("Ouch! There's a Wall")
        if maze.MG.x==maze.Guard.x and maze.MG.y == maze.Guard.y:
            maze.test_victoire()
            exit = True
        
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