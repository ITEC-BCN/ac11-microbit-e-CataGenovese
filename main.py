x = 2
y = 2
executant = True

def on_button_pressed_a():
    global executant
    executant = False

input.on_button_pressed(Button.A, on_button_pressed_a)

while executant:
    led.plot(x, y)
    basic.pause(50)
    led.unplot(x, y)

    accX = input.acceleration(Dimension.X)
    accY = input.acceleration(Dimension.Y)

    if accX < -150 and x > 0:
        x -= 1
    if accX > 150 and x < 4:
        x += 1
    if accY < -150 and y > 0:
        y -= 1
    if accY > 150 and y < 4:
        y += 1


def on_forever():
    temperatura = input.temperature()
    led.plot_bar_graph(temperatura, 50)
basic.forever(on_forever)