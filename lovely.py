#gpl

import love

images = []
rot = 0

#Define your own callbacks here.

def load():
    images.append(love.graphics.newImage("ship.png"))

def update(dt):
    global rot
    rot = rot + (2 * dt)
    

def draw():
    love.graphics.clear()
    love.graphics.draw(images[0], None, 50, 50, rot)


#Then redefine love's default callbacks with your own

love.load = load
love.update = update
love.draw = draw


#finally initiate love
love.init()


