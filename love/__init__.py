import love.event
import love.graphics
import love.window

images = []

handlers = {}
def create_handlers():
    print ("creating handlers")
    handlers["keypressed"] = keypressed
    handlers["keyreleased"] = keyreleased

def draw():
    #draw default love2d screen
    love.graphics.draw(images[0], None, 0, 0)

def errhand():
    pass

def focus():
    pass

def init():
    '''
    create default settings
    load love modules
    load conf file
    create window - DONE
    create event handlers(callbacks) - DONE
    setup timestep
    version check
    '''
    love.create_handlers()
    print (love.handlers)
    love.window.set_mode(600,480,0)
    run()
    
def keypressed(*args):
    print ("pressed", args[0])

def keyreleased(*args):
    if args[0] == "escape":
        print ("quiting")
        close()
#        love.event.quit()

def load():
    images.append(love.graphics.newImage("ship.png"))
    print (images[0].getType())
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
    love.event.pump()

    '''
    if love.load then love.load(arg) end

    -- We don't want the first frame's dt to include time taken by love.load.
    if love.timer then love.timer.step() end
    '''
    dt = 0

    # Main loop time.
    while running: 
        #pump sdl for all current events and put them in our lovely queue
        love.event.pump()

        for message in love.event.poll():
            print (message, message.name)
            if message.name == "quit":
                running = False
                if not love.quit or not love.quit():
                    if love.audio:
                        love.audio.stop()
                        return
            if message.name != 0:
                love.handlers[message.name](message.a, message.b, message.c, message.d)
        love.event.clear()
        
        '''
        # Update dt, as we'll be passing it to update
        if love.timer:
            love.timer.step()
            dt = love.timer.getDelta()
'''
        # Call update and draw
        if love.update:
            love.update(dt) # will pass 0 if love.timer is disabled

            
        if love.window and love.graphics:# and love.window.isCreated():
            love.graphics.clear()
#            love.graphics.origin()

        if love.draw:
            love.draw()

'''
            love.graphics.present()


        if love.timer:
            love.timer.sleep(0.001)
        '''

def textinput():
    pass

def threaderror():
    pass

def update(dt):
    pass

def visible():
    pass


'''
boot.lua contains boot(), init(), run()
1. Boot() - Load game file and decide if game or nogame. Assume no game for now
2. init() - Setup screen.
3. run() - Loop
'''






