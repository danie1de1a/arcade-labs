import arcade


def pithagoras(b, c):
    from math import sqrt
    a = sqrt(b**2+c**2)
    return a


def red_caterpillar(leng, r, window_x, window_y):
    """l, r, window_x and window_y allow int type
    Creates a caterpillar of leng length from a random point in the window with window_x for x-axis and
    window_y for y-axis. If the radius is too big, the process might not work as intended
    Conditions: l, r>0, pithagoras function defined"""
    from random import randint
    counter = 0
    x = randint(r, window_x)
    y = randint(r, window_y)
    while counter <= leng:
        print(x, y)
        var = randint(-r, r)
        if x < r:
            print('a')
            x += var
            y = pithagoras(r, var)
        elif y < r:
            print('b')
            y += var
            x += pithagoras(r, var)
        elif (x+r) > window_x:
            print('c')
            x += var
            y += pithagoras(r, x)
        elif (y+r) > window_y:
            print('d')
            y += var
            x += pithagoras(r, var)
        else:
            print('e')
            x += var
            y += pithagoras(r, var)
        x = round(x)
        y = round(y)
        if r < x < (window_x-r) and r < y < (window_y-r):
            arcade.draw_circle_filled(x, y, r, arcade.color.RED)
            arcade.draw_circle_outline(x, y, r, arcade.color.BARN_RED)
        counter += 1


arcade.open_window(800, 640, "Caterpillar")

arcade.set_background_color(arcade.color.LAWN_GREEN)

arcade.start_render()
"""test"""
red_caterpillar(100, 10, 800, 640)
arcade.finish_render()

arcade.run()
