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



"""valor_maxim = 50
executant = True

def dibuix_barra(temp, maxim):
    columnes = int(temp * 5 / maxim)
    columnes = max(0, min(columnes, 5))
    basic.clear_screen()
    for x in range(columnes):
        for y in range(5):
            led.plot(x, 4 - y)

while executant:
    temperatura = input.temperature()
    dibuix_barra(temperatura, valor_maxim)
    basic.pause(100)
    if input.button_is_pressed(Button.A): 
        ejecutando = False
"""