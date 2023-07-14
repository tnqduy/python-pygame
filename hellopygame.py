import pygame as pg
pg.init()

running = -1
screenSize = (750, 1334)
screen = pg.display.set_mode(screenSize)
clock = pg.time.Clock()


class SpaceShip:
    def __init__(self):
        sprite = pg.image.load("ship3.png")
        sprite = pg.transform.scale(sprite, (50, 50))
        screen.blit(sprite, (0, 0))
        pg.display.update()


def main():

    background = pg.image.load("background.jpg")
    background = pg.transform.scale(background, screenSize)

    space_ship = SpaceShip()

    # screen.blit(background, (0, 0))
    pg.display.update()

    update()


def update():
    global running
    while running:
        # poll for events
        # pg.QUIT event means the user clicked X to close your window
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pg.display.flip()

        clock.tick(60)  # limits FPS to 60

    pg.quit()


main()
