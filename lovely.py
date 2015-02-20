#gpl

import love

images = []
rot = 0
myQuad = None

#Define your own callbacks here.

def load():
    global myQuad
    images.append(love.graphics.newImage("ship.png"))
    myQuad = love.graphics.newQuad(0, 0, 8, 8, 21, 16)

def update(dt):
    global rot
    rot = rot + (2 * dt)
    

def draw():
    love.graphics.clear()
    love.graphics.draw(images[0], myQuad, 50, 50, 0, 1, 1)


#Then redefine love's default callbacks with your own

love.load = load
love.update = update
love.draw = draw


#finally initiate love

love.init()


