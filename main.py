sonar = 0
while not (input.button_is_pressed(Button.A)):
    basic.show_icon(IconNames.NO)

basic.show_icon(IconNames.HAPPY)

basic.pause(1000)
cuteBot.motors(25, 25)

def on_forever():
    global sonar
    sonar = cuteBot.ultrasonic(cuteBot.SonarUnit.CENTIMETERS)
    if sonar < 15:
        basic.show_icon(IconNames.SKULL)
        cuteBot.motors(0, 0)
        basic.pause(1000)
        cuteBot.motors(randint(-50, -100), 0)
        basic.pause(500)
    else:
        basic.show_icon(IconNames.SWORD)
        cuteBot.motors(25, 25)
basic.forever(on_forever)
