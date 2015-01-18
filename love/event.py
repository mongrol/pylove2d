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
    pass

def pump():
    #called by love.run()

    # Get sdl events
    # convert them to love messages
    # put them in the queue

    sdl_event = sdl.Event()
    while (sdl.pollEvent(sdl_event)):
#        ("sdl_event.type: ", sdl_event.type)
        if sdl_event.type == sdl.KEYDOWN:
            keyname = sdl.getKeyName(sdl_event.key.keysym.sym)
            print ("Keypressed", keyname)
        if sdl_event.type == sdl.KEYUP:
            keyname = sdl.getKeyName(sdl_event.key.keysym.sym)
            print ("Keyreleased", keyname)
        queue.append(convert(sdl_event))

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

def convert(event):
    #converts SDL events into love
    msg = Message()
    #print (event.type)
    if event.type == sdl.KEYDOWN:
        msg.name = "keypressed"
        keys = createKeyMap()
        msg.a = keys[event.key.keysym.sym]
        #print (event.key.keysym.sym)
        print ("pressed key", msg.a)
    elif event.type == sdl.KEYUP:
        msg.name = "keyreleased"
        keys = createKeyMap()
        msg.a = keys[event.key.keysym.sym]
        #print (event.key.keysym.sym)
        print ("released key", msg.a)
    return msg

def createKeyMap():
    #	using love::keyboard::Keyboard;

    k = {}
    k[sdl.K_RETURN] = "return"
    k[sdl.K_UNKNOWN] = 0
    k[sdl.K_ESCAPE] = "escape"
    k[sdl.K_SPACE] = "space"
    
    return k

    '''
	k[sdl.K_BACKSPACE] = Keyboard::KEY_BACKSPACE
	k[sdl.K_TAB] = Keyboard::KEY_TAB
	k[sdl.K_EXCLAIM] = Keyboard::KEY_EXCLAIM
	k[sdl.K_QUOTEDBL] = Keyboard::KEY_QUOTEDBL
	k[sdl.K_HASH] = Keyboard::KEY_HASH
	k[sdl.K_DOLLAR] = Keyboard::KEY_DOLLAR
	k[sdl.K_AMPERSAND] = Keyboard::KEY_AMPERSAND
	k[sdl.K_QUOTE] = Keyboard::KEY_QUOTE
	k[sdl.K_LEFTPAREN] = Keyboard::KEY_LEFTPAREN
	k[sdl.K_RIGHTPAREN] = Keyboard::KEY_RIGHTPAREN
	k[sdl.K_ASTERISK] = Keyboard::KEY_ASTERISK
	k[sdl.K_PLUS] = Keyboard::KEY_PLUS
	k[sdl.K_COMMA] = Keyboard::KEY_COMMA
	k[sdl.K_MINUS] = Keyboard::KEY_MINUS
	k[sdl.K_PERIOD] = Keyboard::KEY_PERIOD
	k[sdl.K_SLASH] = Keyboard::KEY_SLASH
	k[sdl.K_0] = Keyboard::KEY_0
	k[sdl.K_1] = Keyboard::KEY_1
	k[sdl.K_2] = Keyboard::KEY_2
	k[sdl.K_3] = Keyboard::KEY_3
	k[sdl.K_4] = Keyboard::KEY_4
	k[sdl.K_5] = Keyboard::KEY_5
	k[sdl.K_6] = Keyboard::KEY_6
	k[sdl.K_7] = Keyboard::KEY_7
	k[sdl.K_8] = Keyboard::KEY_8
	k[sdl.K_9] = Keyboard::KEY_9
	k[sdl.K_COLON] = Keyboard::KEY_COLON
	k[sdl.K_SEMICOLON] = Keyboard::KEY_SEMICOLON
	k[sdl.K_LESS] = Keyboard::KEY_LESS
	k[sdl.K_EQUALS] = Keyboard::KEY_EQUALS
	k[sdl.K_GREATER] = Keyboard::KEY_GREATER
	k[sdl.K_QUESTION] = Keyboard::KEY_QUESTION
	k[sdl.K_AT] = Keyboard::KEY_AT

	k[sdl.K_LEFTBRACKET] = Keyboard::KEY_LEFTBRACKET
	k[sdl.K_BACKSLASH] = Keyboard::KEY_BACKSLASH
	k[sdl.K_RIGHTBRACKET] = Keyboard::KEY_RIGHTBRACKET
	k[sdl.K_CARET] = Keyboard::KEY_CARET
	k[sdl.K_UNDERSCORE] = Keyboard::KEY_UNDERSCORE
	k[sdl.K_BACKQUOTE] = Keyboard::KEY_BACKQUOTE
	k[sdl.K_a] = Keyboard::KEY_A
	k[sdl.K_b] = Keyboard::KEY_B
	k[sdl.K_c] = Keyboard::KEY_C
	k[sdl.K_d] = Keyboard::KEY_D
	k[sdl.K_e] = Keyboard::KEY_E
	k[sdl.K_f] = Keyboard::KEY_F
	k[sdl.K_g] = Keyboard::KEY_G
	k[sdl.K_h] = Keyboard::KEY_H
	k[sdl.K_i] = Keyboard::KEY_I
	k[sdl.K_j] = Keyboard::KEY_J
	k[sdl.K_k] = Keyboard::KEY_K
	k[sdl.K_l] = Keyboard::KEY_L
	k[sdl.K_m] = Keyboard::KEY_M
	k[sdl.K_n] = Keyboard::KEY_N
	k[sdl.K_o] = Keyboard::KEY_O
	k[sdl.K_p] = Keyboard::KEY_P
	k[sdl.K_q] = Keyboard::KEY_Q
	k[sdl.K_r] = Keyboard::KEY_R
	k[sdl.K_s] = Keyboard::KEY_S
	k[sdl.K_t] = Keyboard::KEY_T
	k[sdl.K_u] = Keyboard::KEY_U
	k[sdl.K_v] = Keyboard::KEY_V
	k[sdl.K_w] = Keyboard::KEY_W
	k[sdl.K_x] = Keyboard::KEY_X
	k[sdl.K_y] = Keyboard::KEY_Y
	k[sdl.K_z] = Keyboard::KEY_Z

	k[sdl.K_CAPSLOCK] = Keyboard::KEY_CAPSLOCK

	k[sdl.K_F1] = Keyboard::KEY_F1
	k[sdl.K_F2] = Keyboard::KEY_F2
	k[sdl.K_F3] = Keyboard::KEY_F3
	k[sdl.K_F4] = Keyboard::KEY_F4
	k[sdl.K_F5] = Keyboard::KEY_F5
	k[sdl.K_F6] = Keyboard::KEY_F6
	k[sdl.K_F7] = Keyboard::KEY_F7
	k[sdl.K_F8] = Keyboard::KEY_F8
	k[sdl.K_F9] = Keyboard::KEY_F9
	k[sdl.K_F10] = Keyboard::KEY_F10
	k[sdl.K_F11] = Keyboard::KEY_F11
	k[sdl.K_F12] = Keyboard::KEY_F12

	k[sdl.K_PRINTSCREEN] = Keyboard::KEY_PRINTSCREEN
	k[sdl.K_SCROLLLOCK] = Keyboard::KEY_SCROLLLOCK
	k[sdl.K_PAUSE] = Keyboard::KEY_PAUSE
	k[sdl.K_INSERT] = Keyboard::KEY_INSERT
	k[sdl.K_HOME] = Keyboard::KEY_HOME
	k[sdl.K_PAGEUP] = Keyboard::KEY_PAGEUP
	k[sdl.K_DELETE] = Keyboard::KEY_DELETE
	k[sdl.K_END] = Keyboard::KEY_END
	k[sdl.K_PAGEDOWN] = Keyboard::KEY_PAGEDOWN
	k[sdl.K_RIGHT] = Keyboard::KEY_RIGHT
	k[sdl.K_LEFT] = Keyboard::KEY_LEFT
	k[sdl.K_DOWN] = Keyboard::KEY_DOWN
	k[sdl.K_UP] = Keyboard::KEY_UP

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

	k[sdl.K_LCTRL] = Keyboard::KEY_LCTRL
	k[sdl.K_LSHIFT] = Keyboard::KEY_LSHIFT
	k[sdl.K_LALT] = Keyboard::KEY_LALT
	k[sdl.K_LGUI] = Keyboard::KEY_LGUI
	k[sdl.K_RCTRL] = Keyboard::KEY_RCTRL
	k[sdl.K_RSHIFT] = Keyboard::KEY_RSHIFT
	k[sdl.K_RALT] = Keyboard::KEY_RALT
	k[sdl.K_RGUI] = Keyboard::KEY_RGUI

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



