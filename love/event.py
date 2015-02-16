import sdl
from collections import deque

queue = deque([])

class Message:
    def __init__(self, name=0, a=0, b=0, c=0, d=0):
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    

def clear():
    #clear the queue
    queue.clear()

def poll():
    #returns iterator for the queue
    return queue.__iter__()


def pump():
    #called by love.run()

    # Get sdl events
    # convert them to love messages
    # put them in the queue

    sdl_event = sdl.Event()
    while (sdl.pollEvent(sdl_event)):
        msg = Message()

        if sdl_event.type == sdl.KEYDOWN:
            msg.name = "keypressed"
            keys = getKeyMap()
            msg.a = keys[sdl_event.key.keysym.sym]

        if sdl_event.type == sdl.KEYUP:
            msg.name = "keyreleased"
            keys = getKeyMap()
            msg.a = keys[sdl_event.key.keysym.sym]

        if sdl_event.type == sdl.WINDOWEVENT:
            if sdl_event.window.event == sdl.WINDOWEVENT_FOCUS_GAINED:
                msg.name = "focus"
                msg.a = sdl_event.window.windowID
            elif sdl_event.window.event == sdl.WINDOWEVENT_RESIZED:
                msg.name = "resize"
                msg.a = sdl_event.window.data1
                msg.b = sdl_event.window.data2
            elif sdl_event.window.event == sdl.WINDOWEVENT_SHOWN:
                msg.name = "visible"
                msg.a = True
            elif sdl_event.window.event == sdl.WINDOWEVENT_HIDDEN:
                msg.name = "visible"
                msg.a = False
            elif sdl_event.window.event == sdl.WINDOWEVENT_ENTER:
                msg.name = "mousefocus"
                msg.a = True
            elif sdl_event.window.event == sdl.WINDOWEVENT_LEAVE:
                msg.name = "mousefocus"
                msg.a = False
        
        if sdl_event.type == sdl.MOUSEBUTTONDOWN:
            msg.name = "mousepressed"
            buttons = getMouseMap()
            msg.a = sdl_event.button.x
            msg.b = sdl_event.button.y
            msg.c = buttons[sdl_event.button.button]

        if sdl_event.type == sdl.MOUSEBUTTONUP:
            msg.name = "mousereleased"
            buttons = getMouseMap()
            msg.a = sdl_event.button.x
            msg.b = sdl_event.button.y
            msg.c = buttons[sdl_event.button.button]

        queue.append(msg)


def push():
    #pushes message onto queue
    pass


def quit():
    #quit event to the queue
    msg = Message()
    msg.name = "quit"
    queue.append(msg)


def wait():
    #wait on input before proceeding
    pass


def getKeyMap():

    k = {}
    k[sdl.K_RETURN] = "return"
    k[sdl.K_UNKNOWN] = 0
    k[sdl.K_ESCAPE] = "escape"
    k[sdl.K_SPACE] = "space"

    k[sdl.K_BACKSPACE] = "backspace"
    k[sdl.K_TAB] = "tab"
    k[sdl.K_EXCLAIM] = "!"
    k[sdl.K_QUOTEDBL] = '"'
    k[sdl.K_HASH] = "#"
    k[sdl.K_DOLLAR] = "$"
    k[sdl.K_AMPERSAND] = "%"
    k[sdl.K_QUOTE] = "'"
    k[sdl.K_LEFTPAREN] = "{"
    k[sdl.K_RIGHTPAREN] = "}"
    k[sdl.K_ASTERISK] = "*"
    k[sdl.K_PLUS] = "+"
    k[sdl.K_COMMA] = ","
    k[sdl.K_MINUS] = "-"
    k[sdl.K_PERIOD] = "."
    k[sdl.K_SLASH] = "/"
    k[sdl.K_0] = "0"
    k[sdl.K_1] = "1"
    k[sdl.K_2] = "2"
    k[sdl.K_3] = "3"
    k[sdl.K_4] = "4"
    k[sdl.K_5] = "5"
    k[sdl.K_6] = "6"
    k[sdl.K_7] = "7"
    k[sdl.K_8] = "8"
    k[sdl.K_9] = "9"
    k[sdl.K_COLON] = ":"
    k[sdl.K_SEMICOLON] = ";"
    k[sdl.K_LESS] = "<"
    k[sdl.K_EQUALS] = "="
    k[sdl.K_GREATER] = ">"
    k[sdl.K_QUESTION] = "?"
    k[sdl.K_AT] = "@"
    k[sdl.K_LEFTBRACKET] = "("
    k[sdl.K_BACKSLASH] = "\\"
    k[sdl.K_RIGHTBRACKET] = ")"
    k[sdl.K_CARET] = "^"
    k[sdl.K_UNDERSCORE] = "_"
    k[sdl.K_BACKQUOTE] = "`"
    k[sdl.K_a] = "a"
    k[sdl.K_b] = "b"
    k[sdl.K_c] = "c"
    k[sdl.K_d] = "d"
    k[sdl.K_e] = "c"
    k[sdl.K_f] = "f"
    k[sdl.K_g] = "g"
    k[sdl.K_h] = "h"
    k[sdl.K_i] = "i"
    k[sdl.K_j] = "j"
    k[sdl.K_k] = "k"
    k[sdl.K_l] = "l"
    k[sdl.K_m] = "m"
    k[sdl.K_n] = "n"
    k[sdl.K_o] = "o"
    k[sdl.K_p] = "p"
    k[sdl.K_q] = "q"
    k[sdl.K_r] = "r"
    k[sdl.K_s] = "s"
    k[sdl.K_t] = "t"
    k[sdl.K_u] = "u"
    k[sdl.K_v] = "v"
    k[sdl.K_w] = "w"
    k[sdl.K_x] = "x"
    k[sdl.K_y] = "y"
    k[sdl.K_z] = "z"

    k[sdl.K_CAPSLOCK] = "capslock"
    
    k[sdl.K_F1] = "f1"
    k[sdl.K_F2] = "f2"
    k[sdl.K_F3] = "f3"
    k[sdl.K_F4] = "f4"
    k[sdl.K_F5] = "f5"
    k[sdl.K_F6] = "f6"
    k[sdl.K_F7] = "f7"
    k[sdl.K_F8] = "f8"
    k[sdl.K_F9] = "f9"
    k[sdl.K_F10] = "f10"
    k[sdl.K_F11] = "f11"
    k[sdl.K_F12] = "f12"

    k[sdl.K_PRINTSCREEN] = "printscreen"
    k[sdl.K_SCROLLLOCK] = "scrolllock"
    k[sdl.K_PAUSE] = "pause"
    k[sdl.K_INSERT] = "insert"
    k[sdl.K_HOME] = "home"
    k[sdl.K_PAGEUP] = "pageup"
    k[sdl.K_DELETE] = "delete"
    k[sdl.K_END] = "end"
    k[sdl.K_PAGEDOWN] = "pagedown"
    k[sdl.K_RIGHT] = "right"
    k[sdl.K_LEFT] = "left"
    k[sdl.K_DOWN] = "down"
    k[sdl.K_UP] = "up"

    k[sdl.K_LCTRL] = "lctrl"
    k[sdl.K_LSHIFT] = "lshift"
    k[sdl.K_LALT] = "lalt"
    k[sdl.K_LGUI] = "lgui"
    k[sdl.K_RCTRL] = "rctrl"
    k[sdl.K_RSHIFT] = "rshift"
    k[sdl.K_RALT] = "ralt"
    k[sdl.K_RGUI] = "rgui"

    return k

    '''
	k[sdl.K_NUMLOCKCLEAR] = Keyboard::KEY_NUMLOCKCLEAR
	k[sdl.K_KP_DIVIDE] = Keyboard::KEY_KP_DIVIDE
	k[sdl.K_KP_MULTIPLY] = Keyboard::KEY_KP_MULTIPLY
	k[sdl.K_KP_MINUS] = Keyboard::KEY_KP_MINUS
	k[sdl.K_KP_PLUS] = Keyboard::KEY_KP_PLUS
	k[sdl.K_KP_ENTER] = Keyboard::KEY_KP_ENTER
	k[sdl.K_KP_0] = Keyboard::KEY_KP_0
	k[sdl.K_KP_1] = Keyboard::KEY_KP_1
	k[sdl.K_KP_2] = Keyboard::KEY_KP_2
	k[sdl.K_KP_3] = Keyboard::KEY_KP_3
	k[sdl.K_KP_4] = Keyboard::KEY_KP_4
	k[sdl.K_KP_5] = Keyboard::KEY_KP_5
	k[sdl.K_KP_6] = Keyboard::KEY_KP_6
	k[sdl.K_KP_7] = Keyboard::KEY_KP_7
	k[sdl.K_KP_8] = Keyboard::KEY_KP_8
	k[sdl.K_KP_9] = Keyboard::KEY_KP_9
	k[sdl.K_KP_PERIOD] = Keyboard::KEY_KP_PERIOD
	k[sdl.K_KP_COMMA] = Keyboard::KEY_KP_COMMA
	k[sdl.K_KP_EQUALS] = Keyboard::KEY_KP_EQUALS

	k[sdl.K_APPLICATION] = Keyboard::KEY_APPLICATION
	k[sdl.K_POWER] = Keyboard::KEY_POWER
	k[sdl.K_F13] = Keyboard::KEY_F13
	k[sdl.K_F14] = Keyboard::KEY_F14
	k[sdl.K_F15] = Keyboard::KEY_F15
	k[sdl.K_F16] = Keyboard::KEY_F16
	k[sdl.K_F17] = Keyboard::KEY_F17
	k[sdl.K_F18] = Keyboard::KEY_F18
	k[sdl.K_F19] = Keyboard::KEY_F19
	k[sdl.K_F20] = Keyboard::KEY_F20
	k[sdl.K_F21] = Keyboard::KEY_F21
	k[sdl.K_F22] = Keyboard::KEY_F22
	k[sdl.K_F23] = Keyboard::KEY_F23
	k[sdl.K_F24] = Keyboard::KEY_F24
	k[sdl.K_EXECUTE] = Keyboard::KEY_EXECUTE
	k[sdl.K_HELP] = Keyboard::KEY_HELP
	k[sdl.K_MENU] = Keyboard::KEY_MENU
	k[sdl.K_SELECT] = Keyboard::KEY_SELECT
	k[sdl.K_STOP] = Keyboard::KEY_STOP
	k[sdl.K_AGAIN] = Keyboard::KEY_AGAIN
	k[sdl.K_UNDO] = Keyboard::KEY_UNDO
	k[sdl.K_CUT] = Keyboard::KEY_CUT
	k[sdl.K_COPY] = Keyboard::KEY_COPY
	k[sdl.K_PASTE] = Keyboard::KEY_PASTE
	k[sdl.K_FIND] = Keyboard::KEY_FIND
	k[sdl.K_MUTE] = Keyboard::KEY_MUTE
	k[sdl.K_VOLUMEUP] = Keyboard::KEY_VOLUMEUP
	k[sdl.K_VOLUMEDOWN] = Keyboard::KEY_VOLUMEDOWN

	k[sdl.K_ALTERASE] = Keyboard::KEY_ALTERASE
	k[sdl.K_SYSREQ] = Keyboard::KEY_SYSREQ
	k[sdl.K_CANCEL] = Keyboard::KEY_CANCEL
	k[sdl.K_CLEAR] = Keyboard::KEY_CLEAR
	k[sdl.K_PRIOR] = Keyboard::KEY_PRIOR
	k[sdl.K_RETURN2] = Keyboard::KEY_RETURN2
	k[sdl.K_SEPARATOR] = Keyboard::KEY_SEPARATOR
	k[sdl.K_OUT] = Keyboard::KEY_OUT
	k[sdl.K_OPER] = Keyboard::KEY_OPER
	k[sdl.K_CLEARAGAIN] = Keyboard::KEY_CLEARAGAIN

	k[sdl.K_THOUSANDSSEPARATOR] = Keyboard::KEY_THOUSANDSSEPARATOR
	k[sdl.K_DECIMALSEPARATOR] = Keyboard::KEY_DECIMALSEPARATOR
	k[sdl.K_CURRENCYUNIT] = Keyboard::KEY_CURRENCYUNIT
	k[sdl.K_CURRENCYSUBUNIT] = Keyboard::KEY_CURRENCYSUBUNIT


	k[sdl.K_MODE] = Keyboard::KEY_MODE

	k[sdl.K_AUDIONEXT] = Keyboard::KEY_AUDIONEXT
	k[sdl.K_AUDIOPREV] = Keyboard::KEY_AUDIOPREV
	k[sdl.K_AUDIOSTOP] = Keyboard::KEY_AUDIOSTOP
	k[sdl.K_AUDIOPLAY] = Keyboard::KEY_AUDIOPLAY
	k[sdl.K_AUDIOMUTE] = Keyboard::KEY_AUDIOMUTE
	k[sdl.K_MEDIASELECT] = Keyboard::KEY_MEDIASELECT
	k[sdl.K_WWW] = Keyboard::KEY_WWW
	k[sdl.K_MAIL] = Keyboard::KEY_MAIL
	k[sdl.K_CALCULATOR] = Keyboard::KEY_CALCULATOR
	k[sdl.K_COMPUTER] = Keyboard::KEY_COMPUTER
	k[sdl.K_AC_SEARCH] = Keyboard::KEY_APP_SEARCH
	k[sdl.K_AC_HOME] = Keyboard::KEY_APP_HOME
	k[sdl.K_AC_BACK] = Keyboard::KEY_APP_BACK
	k[sdl.K_AC_FORWARD] = Keyboard::KEY_APP_FORWARD
	k[sdl.K_AC_STOP] = Keyboard::KEY_APP_STOP
	k[sdl.K_AC_REFRESH] = Keyboard::KEY_APP_REFRESH
	k[sdl.K_AC_BOOKMARKS] = Keyboard::KEY_APP_BOOKMARKS

	k[sdl.K_BRIGHTNESSDOWN] = Keyboard::KEY_BRIGHTNESSDOWN
	k[sdl.K_BRIGHTNESSUP] = Keyboard::KEY_BRIGHTNESSUP
	k[sdl.K_DISPLAYSWITCH] = Keyboard::KEY_DISPLAYSWITCH
	k[sdl.K_KBDILLUMTOGGLE] = Keyboard::KEY_KBDILLUMTOGGLE
	k[sdl.K_KBDILLUMDOWN] = Keyboard::KEY_KBDILLUMDOWN
	k[sdl.K_KBDILLUMUP] = Keyboard::KEY_KBDILLUMUP
	k[sdl.K_EJECT] = Keyboard::KEY_EJECT
	k[sdl.K_SLEEP] = Keyboard::KEY_SLEEP
'''

def getMouseMap():

    m = {}
    m[sdl.BUTTON_LEFT] = "l"
    m[sdl.BUTTON_MIDDLE] = "m"
    m[sdl.BUTTON_RIGHT] = "r"
    m[sdl.BUTTON_X1] = "x1"
    m[sdl.BUTTON_X2] = "x2"

    return m
