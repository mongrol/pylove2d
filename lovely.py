#import love.window
#import love.event
import love


'''
boot.lua contains boot(), init(), run()
1. Boot() - Load game file and decide if game or nogame. Assume no game for now
2. init() - Setup screen.
3. run() - Loop
'''

def boot():
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
'''
            
        if love.window and love.graphics and love.window.isCreated():
            love.graphics.clear()
            love.graphics.origin()
            if love.draw:
                love.draw()
            love.graphics.present()


        if love.timer:
            love.timer.sleep(0.001)
        '''
        
#top level love callbacks for nogame

def main():
    '''comment'''
    boot()
    init()
    run()

if __name__ == "__main__":
    main()

