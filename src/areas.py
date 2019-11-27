from src.characters import Hero, Villain
from src.items import Item


class Area:
    """ Area on the map. has an index in each dimension: x and y
    """

    def __init__(self, x, y, genre):
        self.x = x
        self.y = y
        self.genre = genre  # genre: whether the tile is a floor or a wall

    def __str__(self):
        return self.genre + " "


class Maze:
    """ represents the maze with a 2-dimension array of areas, and an array of items lying on the ground """

    def __init__(self, link):
        # create an array that contains each area of the maze
        self.map = list(list())
        self.items = list()
        # read the maze.txt file to get the map, each area
        with open(link, 'r') as f:
            for i in range(10):
                line = f.readline()
                line_list = list()
                j = 0
                for char in line:
                    if char == " " or char == "\n":
                        continue
                    else:
                        line_list.append(Area(j, i, char))
                    j += 1
                self.map.append(line_list)

            f.readline()
            line = f.readline()
            # read characters
            line = line.split("\t")
            self.mg = Hero(int(line[1]), int(line[2]))
            line = f.readline()
            line = line.split("\t")
            self.guard = Villain(line[0], int(line[1]), int(line[2]), line[3], line[4], line[5])

            f.readline()
            # read items
            for i in range(3):
                line = f.readline()
                line = line.split("\t")
                item = Item(line[0], int(line[1]), int(line[2]))
                self.items.append(item)

    def __str__(self):
        map_string = ""
        # a representation of the maze
        for i in self.map:
            for j in i:
                has_item = False
                for k in self.items:
                    if k.x == j.x and k.y == j.y:
                        has_item = True
                        break
                if self.mg.x == j.x and self.mg.y == j.y:
                    map_string += 'G '
                elif self.guard.x == j.x and self.guard.y == j.y:
                    map_string += 'V '
                elif has_item:
                    map_string += 'O '
                else:
                    map_string += j.genre + " "
            map_string += "\n"
        map_string += "\n"
        for i in self.items:
            if i.x == self.mg.x and self.mg.y == i.y:
                map_string += "lying on the floor, waiting to be gathered: {}".format(i.name)

        # printing the inventory
        map_string += '\ninventory: \n'
        for i in self.mg.inventory:
            map_string += "{}\n".format(i)
        return map_string

    def test_victoire(self):
        """function testing if the game ends with a victory or a lose.
        should be called only when Mac Gyver walks on a keeper
        """
        missing_item = False
        for i in self.guard.death_items:
            item_in_inventory = False
            for j in self.mg.inventory:
                if i == j:
                    item_in_inventory = True
                    break
            if not item_in_inventory:
                print("You Lost!")
                missing_item = True
                break
        if not missing_item:
            print("You Won!")
