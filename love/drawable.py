# lgpl
#import pdb;pdb.set_trace()

from love.superclasses import Object

class Drawable(Object):
    pass

class Image(Drawable):
    _type = "Image"
    image = 0
