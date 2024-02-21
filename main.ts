let sonar = 0
while (!(input.buttonIsPressed(Button.A))) {
    basic.showIcon(IconNames.No)
}
basic.showIcon(IconNames.Happy)
basic.pause(1000)
cuteBot.motors(25, 25)
basic.forever(function () {
    sonar = cuteBot.ultrasonic(cuteBot.SonarUnit.Centimeters)
    if (sonar < 15) {
        basic.showIcon(IconNames.Skull)
        cuteBot.motors(0, 0)
        basic.pause(1000)
        cuteBot.motors(randint(-50, -100), 0)
        basic.pause(500)
    } else {
        basic.showIcon(IconNames.Sword)
        cuteBot.motors(25, 25)
    }
})
