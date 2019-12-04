"""launcher of the game, contents all the interaction logic"""
from sources.areas import Maze
import pygame
from pygame.locals import *


def main():
    """starting the game"""
    pygame.init()
    window = pygame.display.set_mode((320, 560), )
    pygame.display.set_caption("Mac Gyver")
    # icon=pygame.image.load("img/icon.png").convert()
    # pygame.display.set_icon(icon)
    collision_sound = pygame.mixer.Sound("sound/wall_collision.ogg")
    item_sound = pygame.mixer.Sound("sound/item_gathering.ogg")
    maze = Maze("maze.txt")

    win = ""
    freeze = False
    exit_game = False
    while not exit_game:
        if not freeze:
            window.fill((0, 0, 0))
        maze.print(window)
        pygame.display.flip()
        action = "a"
        for event in pygame.event.get():
            if event.type == QUIT:
                action = "quit"
            elif event.type == KEYDOWN and not freeze:
                if event.key == K_UP or event.key == K_z:
                    action = "z"
                elif event.key == K_LEFT or event.key == K_q:
                    action = "q"
                elif event.key == K_DOWN or event.key == K_s:
                    action = "s"
                elif event.key == K_RIGHT or event.key == K_d:
                    action = "d"
                elif event.key == K_SPACE or event.key == K_e:
                    action = "e"

        if action == "z":
            if maze.map[maze.mac_gyver.y - 1][maze.mac_gyver.x].genre != "M":
                maze.mac_gyver.y -= 1
            else:
                collision_sound.play()
            if maze.mac_gyver.x == maze.guard.x and maze.mac_gyver.y == maze.guard.y:
                win = maze.test_victoire()

        elif action == "q":
            if maze.map[maze.mac_gyver.y][maze.mac_gyver.x - 1].genre != "M":
                maze.mac_gyver.x -= 1
            else:
                collision_sound.play()
            if maze.mac_gyver.x == maze.guard.x and maze.mac_gyver.y == maze.guard.y:
                win = maze.test_victoire()

        elif action == "s":
            if maze.map[maze.mac_gyver.y + 1][maze.mac_gyver.x].genre != "M":
                maze.mac_gyver.y += 1
            else:
                collision_sound.play()
            if maze.mac_gyver.x == maze.guard.x and maze.mac_gyver.y == maze.guard.y:
                win = maze.test_victoire()

        elif action == "d":
            if maze.map[maze.mac_gyver.y][maze.mac_gyver.x + 1].genre != "M":
                maze.mac_gyver.x += 1
            else:
                collision_sound.play()
            if maze.mac_gyver.x == maze.guard.x and maze.mac_gyver.y == maze.guard.y:
                win = maze.test_victoire()

        elif action == "e":
            count = 0
            for i in maze.items:
                if i.x == maze.mac_gyver.x and i.y == maze.mac_gyver.y:
                    maze.mac_gyver.gather_item(i)
                    maze.items.remove(i)
                    item_sound.play()
                    count += 1
            if count == 0:
                print("there's no item to gather")
        elif action != "a":
            exit_game = True

        if win == "win" or win == "lose" or freeze:
            if not freeze:
                ending_screen(window, True if win == "win" else False)
                freeze = True
                win = ""


def ending_screen(window, win):
    if win:
        win_sound = pygame.mixer.Sound("sound/win.ogg")
        police = pygame.font.Font(None, 64)
        text = police.render("You WIN", True, pygame.Color("#00FF00"))
        rect_text = text.get_rect()
        rect_text.center = (160, 352)
        window.blit(text, rect_text)
        win_sound.play()

    else:
        lose_sound = pygame.mixer.Sound("sound/lose.ogg")
        police = pygame.font.Font(None, 64)
        text = police.render("You LOSE", True, pygame.Color("#FF0000"))
        rect_text = text.get_rect()
        rect_text.center = (160, 352)
        window.blit(text, rect_text)
        lose_sound.play()

    text = "pictures:\n Jesse Freeman and Dan Wolfe\ncoding:\nRemi Tauvel (studies project)"
    police = pygame.font.Font("font/Android 101.ttf", 15)
    y = 400
    for line in text.splitlines():
        rendered_line = police.render(line, True, pygame.Color("#FFFFFF"))
        rect_text = rendered_line.get_rect()
        rect_text.center = (160, y)
        window.blit(rendered_line, rect_text)
        y += 17


if __name__ == '__main__':
    main()
