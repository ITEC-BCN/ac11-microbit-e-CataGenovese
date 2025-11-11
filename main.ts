let accX: number;
let accY: number;
let x = 2
let y = 2
let executant = true
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    executant = false
})
while (executant) {
    led.plot(x, y)
    basic.pause(50)
    led.unplot(x, y)
    accX = input.acceleration(Dimension.X)
    accY = input.acceleration(Dimension.Y)
    if (accX < -150 && x > 0) {
        x -= 1
    }
    
    if (accX > 150 && x < 4) {
        x += 1
    }
    
    if (accY < -150 && y > 0) {
        y -= 1
    }
    
    if (accY > 150 && y < 4) {
        y += 1
    }
    
}
basic.forever(function on_forever() {
    let temperatura = input.temperature()
    led.plotBarGraph(temperatura, 50)
})
