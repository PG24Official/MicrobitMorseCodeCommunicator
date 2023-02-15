// Morse code .
input.onButtonPressed(Button.A, function () {
    if (morseActive == 0) {
        morseActive = 1
        music.playTone(988, music.beat(BeatFraction.Quarter))
    }
    morseActive = 0
})
input.onButtonPressed(Button.AB, function () {
    if (canReread == 1) {
        control.reset()
    }
})
// Morse code -
input.onButtonPressed(Button.B, function () {
    if (morseActive == 0) {
        morseActive = 1
        music.playTone(988, music.beat(BeatFraction.Half))
    }
    morseActive = 0
})
// Initialization
let canReread = 0
let morseActive = 0
morseActive = 0
canReread = 0
basic.showString("A=.")
basic.showString("B=-")
basic.showString("A+B TO RE-READ INSTRUCTIONS")
canReread = 1
