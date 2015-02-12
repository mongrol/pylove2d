import sdl
import love

window = 0
renderer = 0

def set_mode(width, height, flags):
    #create window
    window = sdl.createWindow("Game Window", 0, 0, width, height, 0)
    if (window):
        #create renderer
        love.window.renderer = sdl.createRenderer(
            window, -1,
            sdl.RENDERER_ACCELERATED)
        if (renderer):
            sdl.setRenderDrawColor (renderer, 0, 0, 0, 0);
            sdl.renderClear(renderer)
            sdl.renderPresent(renderer)
            return renderer
        else:
            print ("Error: No renderer")
            return False
