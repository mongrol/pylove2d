import love.event
import love.graphics
import love.timer
import love.window


handlers = {}
def create_handlers():
    handlers["keypressed"] = keypressed
    handlers["keyreleased"] = keyreleased
    handlers["focus"] = focus
    handlers["mousefocus"] = mousefocus
    handlers["mousepressed"] = mousepressed
    handlers["mouserelease"] = mousereleased
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
    
def keypressed(*args):
    print ("pressed", args[0])

    
def keyreleased(*args):
    if args[0] == "escape":
        print ("quiting")
        close()
#        love.event.quit()


def load():
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
    running = True
    '''
    if love.math then
        love.math.setRandomSeed(os.time())
    end
    '''

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

def visible():
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
