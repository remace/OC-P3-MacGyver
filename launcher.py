"""launcher of the game, contents all the interaction logic"""
from src.areas import Maze

def main():
    """starting the game"""
    maze = Maze("maze.txt")
    exit_game = False
    while not exit_game:
        print(maze)
        action = input("which action?\n(zqsd for a movement,"
                       "e for gathering what lies on the floor,"
                       "then press enter)\n")
        if action == "z":
            if maze.map[maze.mac_gyver.y-1][maze.mac_gyver.x].genre != "M":
                maze.mac_gyver.y -= 1
                print("moving to the north")
            else:
                print("Ouch! There's a Wall!")
            if maze.mac_gyver.x == maze.guard.x and maze.mac_gyver.y == maze.guard.y:
                maze.test_victoire()
                exit_game = True

        elif action == "q":
            if maze.map[maze.mac_gyver.y][maze.mac_gyver.x-1].genre != "M":
                maze.mac_gyver.x -= 1
                print("moving to the west")
            else:
                print("Ouch! There's a Wall!")
            if maze.mac_gyver.x == maze.guard.x and maze.mac_gyver.y == maze.guard.y:
                maze.test_victoire()
                exit_game = True

        elif action == "s":
            if maze.map[maze.mac_gyver.y+1][maze.mac_gyver.x].genre != "M":
                maze.mac_gyver.y += 1
                print("moving to the south")
            else:
                print("Ouch! There's a Wall!")
            if maze.mac_gyver.x == maze.guard.x and maze.mac_gyver.x == maze.guard.y:
                maze.test_victoire()
                exit_game = True

        elif action == "d":
            if maze.map[maze.mac_gyver.y][maze.mac_gyver.x+1].genre != "M":
                maze.mac_gyver.x += 1
                print("moving to the east")
            else:
                print("Ouch! There's a Wall")
            if maze.mac_gyver.x == maze.guard.x and maze.mac_gyver.y == maze.guard.y:
                maze.test_victoire()
                exit_game = True

        elif action == "e":
            count = 0
            for i in maze.items:
                if i.x == maze.mac_gyver.x and i.y == maze.mac_gyver.y:
                    maze.mac_gyver.gather_item(i)
                    maze.items.remove(i)
                    print('gathered item: {}'.format(i.name))
                    count += 1
            if count == 0:
                print("there's no item to gather")
        else:
            exit_game = True

main()
