#lovely graphics module
import math
import sdl
from love.drawable import Image
from love.drawable import Quad
import love

backgroundColor = [0, 0, 0]

def clear():
    pass

def draw(image, quad=None, x=0, y=0, r=0, sx=1, sy=1, ox=0, oy=0):
    src_rect = sdl.Rect((0,0,image.getWidth(), image.getHeight()))
    dest_rect = sdl.Rect((x,y,image.getWidth() * sx, image.getHeight() * sy))
    center = sdl.Point((ox, oy))
    angle = math.degrees(r)
    sdl.renderCopyEx(love.window.renderer, image._texture, src_rect, dest_rect, angle, center, 0)
    sdl.renderPresent(love.window.renderer)

def newImage( filename ):
    img = Image()
    surface = sdl.image.load(filename)
    print (love.window.renderer)
    texture = sdl.createTextureFromSurface(love.window.renderer, surface)
    img.setData(texture)
    img.setWidth(surface.w)
    img.setHeight(surface.h)
    print ("creating image from ", filename, " of size ", img.getWidth(), img.getHeight())
    return img

def newQuad():
    quad = Quad()
    return quad

def setBackgroundColor(r, g, b):
    pass

