#lovely graphics module
import math
import sdl
from love.drawable import Image
from love.drawable import Quad
import love

#graphics module globals
backgroundColor = [0, 0, 0]


def clear():
    global backgroundColor
    r,g,b= backgroundColor
    sdl.setRenderDrawColor (love.window.renderer, r, g, b, 0);
    sdl.renderClear(love.window.renderer)
    pass


def draw(image, quad=None, x=0, y=0, r=0, sx=1, sy=1, ox=0, oy=0):

    iw = image.getWidth()
    ih = image.getHeight()
    sw = quad._sw
    sh = quad._sh
    if quad == None:
        src_rect = sdl.Rect((0, 0,iw, ih))
    else:
        scale_x = sw / iw
        scale_y = sh / ih
        src_rect = sdl.Rect((0, 0, int(quad._w * scale_x),
                             int(quad._h * scale_y)))
        
    dest_rect = sdl.Rect((x,y,src_rect.w * sx,
                          src_rect.h * sy))
    center = sdl.Point((ox, oy))
    angle = math.degrees(r)
    sdl.renderCopyEx(love.window.renderer, image._texture, src_rect,
                     dest_rect, angle, center, 0)

    
def newImage( filename ):
    img = Image()
    surface = sdl.image.load(filename)
    texture = sdl.createTextureFromSurface(love.window.renderer,
                                           surface)
    img.setData(texture)
    img.setWidth(surface.w)
    img.setHeight(surface.h)
    return img


def newQuad(x, y, width, height, sw, sh):
    quad = Quad()
    quad._sw = sw
    quad._sh = sh
    quad.setViewport(x, y, width, height)
    return quad


def origin():
    pass

def present():
    sdl.renderPresent(love.window.renderer)


def setBackgroundColor(r, g, b, alpha=0):
    #TODO : alpha
    
    global backgroundColor
    backgroundColor = [r, g, b]

