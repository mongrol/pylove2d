import love.event
import love.graphics
import love.window


handlers = {}
def create_handlers():
    print ("creating handlers")
    handlers["keypressed"] = keypressed
    handlers["keyreleased"] = keyreleased

def draw():
    pass

def errhand():
    pass

def focus():
    pass

def keypressed(*args):
    print ("pressed", args[0])

def keyreleased(*args):
    if args[0] == "escape":
        print ("quiting")
        close()
#        love.event.quit()

def load():
    img = love.graphics.newImage("test")
    print (img.getType())
    pass

def mousefocus():
    pass

def mousepressed():
    pass

def mousereleased():
    pass

def close():
    #replacement for love.quit avoiding reserved keyword
    exit()
    pass

def resize():
    pass

def run():
    pass

def textinput():
    pass

def threaderror():
    pass

def update(dt):
    pass

def visible():
    pass





