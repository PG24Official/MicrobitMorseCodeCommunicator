# Morse code .

def on_button_pressed_a():
    global morseActive
    if morseActive == 0:
        morseActive = 1
        music.play_tone(988, music.beat(BeatFraction.QUARTER))
    morseActive = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    if canReread == 1:
        control.reset()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

# Morse code -

def on_button_pressed_b():
    global morseActive
    if morseActive == 0:
        morseActive = 1
        music.play_tone(988, music.beat(BeatFraction.HALF))
    morseActive = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

# Initialization
canReread = 0
morseActive = 0
morseActive = 0
canReread = 0
basic.show_string("A=.")
basic.show_string("B=-")
basic.show_string("A+B TO RE-READ INSTRUCTIONS")
canReread = 1
