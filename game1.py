from pygame import *
display.set_caption('PinPong')
window = display.set_mode((700,500))
background = transform.scale(image.load('spalny.jpg'), (700,500))
clock = time.Clock()
finish = False

class GameSprite(spite.sprite):
    def __init__(self, player_1, player_2,)


run = True
while run:
    window.blit(background, (0,0))
    for e in event.get():
        if e.type == QUIT:
            run = False
    display.update()
    clock.tick(60)
