# lgpl
#import pdb;pdb.set_trace()

from love.superclasses import Object

class Drawable(Object):
    pass

class Texture(Drawable):
    _type = "Texture"

class Image(Texture):
    _type = "Image"
    _texture = 0
    _width = 0
    _height = 0
    
    def getHeight(self):
        return self._height
        
    def getWidth(self):
        return self._width

    def setData(self, texture):
        self._texture = texture

    def setHeight(self, h ):
        self._height = h
        return
        
    def setWidth(self, w ):
        self._width = w
        return

class Quad(Object):
    _type = "Quad"
    _x, _y, _w, _h, _sw, _sh = 0, 0, 1, 1, 1, 1
    
    def getViewport(self):
        return self._x, self._y, self._w, self._h
    def setViewport(self, x, y, w, h):
        self._x = x
        self._y = y
        self._w = w
        self._h = h
    
