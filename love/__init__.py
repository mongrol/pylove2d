import time

import love.event
import love.graphics
import love.math
import love.timer
import love.window


handlers = {}
def create_handlers():
    handlers["keypressed"] = keypressed
    handlers["keyreleased"] = keyreleased
    handlers["focus"] = focus
    handlers["mousefocus"] = mousefocus
    handlers["mousepressed"] = mousepressed
    handlers["mousereleased"] = mousereleased
    handlers["resize"] = resize
    handlers["visible"] = visible
    handlers["joystickpressed"] = joystickpressed
    handlers["joystickreleased"] = joystickreleased
    handlers["joystickaxis"] = joystickaxis
    handlers["joystickhat"] = joystickhat
    
    
# General Callbacks
def draw():
    pass

def errhand():
    pass

def focus(windowID, b, c, d):
    pass

def init():
    '''
    create default settings if they don't exist
    load conf file
    create window - DONE
    create event handlers(callbacks) - DONE
    setup timestep - DONE
    version check
    '''
    
    #create love callback handlers
    love.create_handlers()
    
    #create window
    love.window.set_mode(600,480,0)

    #enter main loop
    run()
    
def keypressed(a, b=None, c=None, d=None):
    print ("pressed", a)

    
def keyreleased(a, b=None, c=None, d=None):
    print ("released", a)
    if a == "escape":
        print ("quiting")
        close()
#        love.event.quit()


def load():
    pass


def mousefocus(a, b=None, c=None, d=None):
    pass


def mousepressed(x, y, button, d=None):
    pass

def mousereleased(x, y, button, d=None):
    pass


def close():
    #replacement for love.quit avoiding reserved keyword
    exit()
    pass


def resize(w, h, c=None, d=None):
    pass
#    print ("Window resized to ",w, h)


def run():
    running = True

    if love.math:
        love.math.setRandomSeed(time.time())

    love.load()

    if love.event:
        love.event.pump()

    #if love.load then love.load(arg) end

    #don't want the first frame's dt to include time taken by love.load.
    if love.timer:
        love.timer.step()

    dt = 0

    # Main loop time.
    while running: 
        #pump sdl for all current events and put them in our queue
        if love.event:
            love.event.pump()

            for message in love.event.poll():
                if message.name == "quit":
                    running = False
                    if not love.quit or not love.quit():
                        if love.audio:
                            love.audio.stop()
                            return
                if message.name != 0:
                    love.handlers[message.name](message.a, message.b,
                                                message.c, message.d)
        love.event.clear()
        
        # Update dt, as we'll be passing it to update
        if love.timer:
            love.timer.step()
            dt = love.timer.getDelta()
            
        # Call update and draw
        if love.update:
            love.update(dt) # will pass 0 if love.timer is disabled

        if love.window and love.graphics:# and love.window.isCreated():
            love.graphics.clear()
            love.graphics.origin()
            if love.draw:
                love.draw()
            love.graphics.present()

        if love.timer:
            love.timer.sleep(0.0001)

                
def textinput():
    pass

def threaderror():
    pass

def update(dt):
    pass

def visible(a, b=None, c=None, d=None):
    pass


# Joystick Callbacks
def gamepadaxis():
    pass

def gamepadpressed():
    pass

def joystickadded():
    pass

def joystickaxis():
    pass

def joystickhat():
    pass

def joystickpressed():
    pass

def joystickreleased():
    pass

def joystickremoved():
    pass
