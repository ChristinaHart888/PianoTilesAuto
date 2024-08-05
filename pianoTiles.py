from pynput.mouse import Controller, Button, Listener

from mss import mss

def on_click(x, y, button, pressed):
    if (pressed):
        print('Mouse clicked at ({0}, {1})'.format(x, y))

# with Listener(on_click=on_click) as listener:
#     listener.join()

def tile_bot():
    x_coordinate = 3207
    y_coordinate = 554
    x2 = 3741
    y2 = 741
    screenshot = (x_coordinate, y_coordinate, x2, y2)
    space = (x2 - x_coordinate) / 4
    middle_tile = (space/2, space/2 + space, space/2 + space * 2, space/2 + space * 3)
    mouse = Controller()
    with mss() as sct:
        print('sct {0}'.format(screenshot))
        img = sct.grab(screenshot)
        for mid in middle_tile:
            mid = round(mid)
            if img.pixel(mid, 0)[0] == 0 and img.pixel(mid, 14)[0] == 0:
                mouse.position = (x_coordinate + mid, y_coordinate + 109)
                mouse.click(Button.left, 1)
                print("Click")
#(-960, 917), (-184, 543)
# (3207, 741)
# (3742, 554)

# on_click()
while True:
    tile_bot()