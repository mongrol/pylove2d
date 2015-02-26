#gpl

import love

images = []
rot = 0
myQuad = None

#Define your own callbacks here.

def load():
    global myQuad
    images.append(love.graphics.newImage("ship.png"))
    myQuad = love.graphics.newQuad(0, 0, 21, 16, 21, 16)
    love.graphics.setColor(255, 255, 0, 0)

def update(dt):
    global rot
    rot = rot + (2 * dt)
    

def draw():
    love.graphics.clear()
    love.graphics.draw(images[0], myQuad, 50, 50, 0, 1, 1)
    love.graphics.line(40, 140, 200, 140)
    love.graphics.point(50,150)
    love.graphics.rectangle("fill", 10, 150, 10, 10)
    love.graphics.rectangle("line", 10,170, 10, 10)
    
#Then redefine love's default callbacks with your own

love.load = load
love.update = update
love.draw = draw


#finally initiate love

love.init()


