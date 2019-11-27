from src.areas import Maze

maze = Maze("maze.txt")
exit = False
while not exit:
    print(maze)
    action = input("which action?\n(zqsd for a movement, e for gathering what lies on the floor, then press enter)\n")
    if action == "z":
        if maze.map[maze.mg.y-1][maze.mg.x].genre != "M":
            maze.mg.y -= 1
            print("moving to the north")
        else:
            print("Ouch! There's a Wall!")
        if maze.mg.x == maze.guard.x and maze.mg.y == maze.guard.y:
            maze.test_victoire()
            exit = True
        
    elif action == "q":
        if maze.map[maze.mg.y][maze.mg.x-1].genre != "M":
            maze.mg.x -= 1
            print("moving to the west")
        else:
            print("Ouch! There's a Wall!")
        if maze.mg.x == maze.guard.x and maze.mg.y == maze.guard.y:
            maze.test_victoire()
            exit = True
        
    elif action == "s":
        if maze.map[maze.mg.y+1][maze.mg.x].genre != "M":
            maze.mg.y += 1
            print("moving to the south")
        else:
            print("Ouch! There's a Wall!")
        if maze.mg.x == maze.guard.x and maze.mg.x == maze.guard.y:
            maze.test_victoire()
            exit = True
        
    elif action == "d":
        if maze.map[maze.mg.y][maze.mg.x+1].genre != "M":
            maze.mg.x += 1
            print("moving to the east")
        else:
            print("Ouch! There's a Wall")
        if maze.mg.x == maze.guard.x and maze.mg.y == maze.guard.y:
            maze.test_victoire()
            exit = True
        
    elif action == "e":
        count = 0
        for i in maze.items:
            if i.x == maze.mg.x and i.y == maze.mg.y:
                maze.mg.gather_item(i)
                maze.items.remove(i)
                print('gathered item: {}'.format(i.name))
                count += 1
        if count == 0:
            print("there's no item to gather")
    else:
        exit = True
