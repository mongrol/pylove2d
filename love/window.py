import sdl

def set_mode(width, height, flags):
    window = sdl.createWindow("Game Window", 0, 0, width, height, 0)
    if (window):
        return True
