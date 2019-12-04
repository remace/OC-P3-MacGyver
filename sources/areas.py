"""module with the definitions of an area and of a Maze"""

from sources.characters import Hero, Villain
from sources.items import Item

import pygame
from pygame.locals import *


class Area:
    """ Area on the map. has an index in each dimension: x and y"""

    def __init__(self, x, y, genre):
        self.x = x
        self.y = y
        self.genre = genre  # genre: whether the tile is a floor ("S") or a wall ("M")

    def __str__(self):
        return self.genre + " "


class Maze:
    """ represents the maze with:
    a 2-dimension array of areas,
    and an array of items lying on the ground
    """

    def __init__(self, link):
        """Maze constructor
            link parameter is the link to a maze file
        """
        # create an array that contains each area of the maze
        self.map = list(list())
        self.items = list()
        # read the maze.txt file to get the map, each area
        with open(link, 'r') as file:
            for i in range(10):
                line = file.readline()
                line_list = list()
                j = 0
                for char in line:
                    if char == " " or char == "\n":
                        continue
                    else:
                        line_list.append(Area(j, i, char))
                    j += 1
                self.map.append(line_list)

            file.readline()
            line = file.readline()
            # read characters
            line = line.split("\t")
            self.mac_gyver = Hero(int(line[1]), int(line[2]))
            line = file.readline()
            line = line.split("\t")
            self.guard = Villain(line[0], int(line[1]), int(line[2]), line[3], line[4], line[5])

            file.readline()
            # read items 
            # TODO emplacement aléatoire et non lu dans le fichier
            for i in range(3):
                line = file.readline()
                line = line.split("\t")
                item = Item(line[0], int(line[1]), int(line[2]))
                self.items.append(item)

    def __str__(self):
        """ representing the map in a text terminal"""
        map_string = ""
        # a representation of the maze
        for i in self.map:
            for j in i:
                has_item = False
                for k in self.items:
                    if k.x == j.x and k.y == j.y:
                        has_item = True
                        break
                if self.mac_gyver.x == j.x and self.mac_gyver.y == j.y:
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
            if i.x == self.mac_gyver.x and self.mac_gyver.y == i.y:
                map_string += "lying on the floor, waiting to be gathered: {}".format(i.name)

        # printing the inventory
        map_string += '\ninventory: \n'
        for i in self.mac_gyver.inventory:
            map_string += "{}\n".format(i)
        return map_string

    def print(self, window):
        """representing the maze in a pygame window"""
        for i in self.map:
            for j in i:
                if j.genre == "M":
                    wall_image = pygame.image.load("img/wall.png").convert()
                    window.blit(wall_image, (j.x*32, j.y*32))
                elif j.genre == "S":
                    floor_image = pygame.image.load("img/floor.png").convert()
                    window.blit(floor_image, (j.x*32, j.y*32))
                    
        for i in self.items:
            item_image = pygame.image.load("img/item.png").convert_alpha()
            window.blit(item_image, (32*i.x, 32*i.y))

        # print the keeper's image
        keeper_image = pygame.image.load("img/keeper.png").convert_alpha()
        window.blit(keeper_image, (32*self.guard.x, 32*self.guard.y))

        # print Mac gyver's image
        mac_gyver_image = pygame.image.load("img/mac_gyver.png").convert_alpha()
        window.blit(mac_gyver_image, (32*self.mac_gyver.x, 32*self.mac_gyver.y))
        
        # print the inventory items
        counter = 0
        for i in self.mac_gyver.inventory:
            item_image = pygame.image.load("img/"+i+".png").convert()
            window.blit(item_image, ((counter+1)*32+counter*64, 560-64))
            counter += 1
        # print the inventory frame
        for i in range(10):
            window.blit(floor_image, (32*i, 560-3*32))
        for i in [0, 3, 6, 9]:
            window.blit(floor_image, (32*i, 560-2*32))
        for i in [0, 3, 6, 9]:
            window.blit(floor_image, (32*i, 560-32))

        if self.mac_gyver.x == 1 and self.mac_gyver.y == 1:
            text = "moving: Z,Q,S,D or arrows.\n gathering an item: e or space"
        else:
            text = ""
        police = pygame.font.Font("font/Android 101.ttf", 15)
        y = 430
        for line in text.splitlines():
            rendered_line = police.render(line, True, pygame.Color("#FFFFFF"))
            rect_text = rendered_line.get_rect()
            rect_text.center = (160, y)
            window.blit(rendered_line, rect_text)
            y += 17

    def test_victoire(self):
        """function testing if the game ends with a victory or a lose.
        should be called only when Mac Gyver walks on a keeper
        """
        for i in self.guard.death_items:
            item_in_inventory = False
            for j in self.mac_gyver.inventory:
                if i == j:
                    item_in_inventory = True
                    break
            if not item_in_inventory:
                return "lose"
        return "win"
