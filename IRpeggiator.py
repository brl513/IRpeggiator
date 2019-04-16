from microbit import * # Import everything from microbit library
import math # Import math library

def midiNoteOn(chan, n, vel): # Defines the function for midiNoteOn
    MIDI_NOTE_ON = 0x90 # Defines constant for note on using hexadecimal
    if chan > 15: # Only 16 channels (0 to 15) so anything above returns function.
        return
    if n > 127: # Only 128 midi notes (0 to 127) so anything above returns function.
        return
    if vel > 127: # Only 128 midi velocity values (0 to 127) so anything above returns function.
        return
    msg = bytes([MIDI_NOTE_ON | chan, n, vel]) # Stores all information in bytes form as variable 'msg'
    uart.write(msg) # Sends 'msg' down MIDI cable


def midiNoteOff(chan, n, vel): # Defines the function for midiNoteOff
    MIDI_NOTE_OFF = 0x80 # Defines constant for note off using hexadecimal
    if chan > 15: # Only 16 channels (0 to 15) so anything above returns function.
        return
    if n > 127: # Only 128 midi notes (0 to 127) so anything above returns function.
        return
    if vel > 127: # Only 128 midi velocity values (0 to 127) so anything above returns function.
        return
    msg = bytes([MIDI_NOTE_OFF | chan, n, vel]) # Stores all information in bytes form as variable 'msg'
    uart.write(msg) # Sends 'msg' down MIDI cable


def midiControlChange(chan, n, value): # Defines the function for midiNoteOff
    MIDI_CC = 0xB0 # Defines constant for note off using hexadecimal
    if chan > 15: # Only 16 channels (0 to 15) so anything above returns function.
        return
    if n > 127: # Only 128 midi notes (0 to 127) so anything above returns function.
        return
    if value > 127: # Only 128 midi velocity values (0 to 127) so anything above returns function.
        return
    msg = bytes([MIDI_CC | chan, n, value]) # Stores all information in bytes form as variable 'msg'
    uart.write(msg) # Sends 'msg' down MIDI cable

def Start(): # Defines function that sets up the MIDI connection through the cables
    uart.init(baudrate=31250, bits=8, parity=None, stop=1, tx=pin0)
    # 'baudrate' determines bits per second for MIDI. 'bits' determines how many bits are sent at a time for MIDI. 'tx' determines which pin the data is sent through.

# Next section is the main program

Start() # Calls start function so MIDI connection is active
lastA = False # Initialised variable as value 'False' for is_pressed or is_touched pins
lastB = False # Same as above
lastC = False # Same as above
lastD = 0 # Initialised variable as value '0' for digital pins
lastE = 0 # Same as above
lastF = 0 # Same as above
BUTTON_A_NOTE = 36 # Initialises note to button A (Values here don't really matter due to not actual determining pitch of arpeggiator)
BUTTON_B_NOTE = 39 # Initialises note to button B
BUTTON_C_NOTE = 43 # Initialises note to button C
BUTTON_D_NOTE = 46 # Initialises note to button D
BUTTON_E_NOTE = 47 # Initialises note to button E
BUTTON_F_NOTE = 48 # Initialises note to button F
last_pot = 0 # Initialised variable as value '0' for analog pin
while True: # Initiates an endless while loop
    pot = pin2.read_analog() # Initialises variable that stores analog pin value
    if last_pot != pot: # If last pot and pot aren't equal then do the following:
        velocity = math.floor(pot / 1024 * 127) # Sets new variable 'velocity' to a value between 0 and 127 based on pot value.
        midiControlChange(0, 23, velocity) # Calls MIDICC function and assigns the velocity to it.
    last_pot = pot # Resets last pot to current pot value

    a = button_a.is_pressed() # Initialises variable that stores the is_pressed. 'True' or 'False'.
    b = button_b.is_pressed() # Same as above
    c = pin1.is_touched() # Same as above
    d = pin8.read_digital() # Initialises variable that stores the digital pin value. '1' or '0'.
    e = pin12.read_digital() # Same as above
    f = pin16.read_digital() # Same as above
    if a is True and lastA is False: # If statement that checks the current value compared to the previous value and turns the note on or off.
        midiNoteOn(0, BUTTON_A_NOTE, 127)
    elif a is False and lastA is True:
        midiNoteOff(0, BUTTON_A_NOTE, 127) # If statement that checks the current value compared to the previous value and turns the note on or off.
    if b is True and lastB is False:
        midiNoteOn(1, BUTTON_B_NOTE, 127) # If statement that checks the current value compared to the previous value and turns the note on or off.
    elif b is False and lastB is True:
        midiNoteOff(1, BUTTON_B_NOTE, 127) # If statement that checks the current value compared to the previous value and turns the note on or off.
    if c is True and lastC is False:
        midiNoteOn(2, BUTTON_C_NOTE, 127) # If statement that checks the current value compared to the previous value and turns the note on or off.
    elif c is False and lastC is True:
        midiNoteOff(2, BUTTON_C_NOTE, 127) # If statement that checks the current value compared to the previous value and turns the note on or off.
    if d is 1 and lastD is 0:
        midiNoteOn(3, BUTTON_D_NOTE, 127) # If statement that checks the current value compared to the previous value and turns the note on or off.
    elif d is 0 and lastD is 1:
        midiNoteOff(3, BUTTON_D_NOTE, 127) # If statement that checks the current value compared to the previous value and turns the note on or off.
    if e is 1 and lastE is 0:
        midiNoteOn(4, BUTTON_E_NOTE, 127) # If statement that checks the current value compared to the previous value and turns the note on or off.
    elif e is 0 and lastE is 1:
        midiNoteOff(4, BUTTON_E_NOTE, 127) # If statement that checks the current value compared to the previous value and turns the note on or off.
    if f is 1 and lastF is 0:
        midiNoteOn(5, BUTTON_F_NOTE, 127) # If statement that checks the current value compared to the previous value and turns the note on or off.
    elif f is 0 and lastF is 1:
        midiNoteOff(5, BUTTON_F_NOTE, 127) # If statement that checks the current value compared to the previous value and turns the note on or off.

    lastA = a # Resets the last value to the current value
    lastB = b # Same as above
    lastC = c # Same as above
    lastD = d # Same as above
    lastE = e # Same as above
    lastF = f # Same as above