"""Lab 07 - User Control"""

import arcade
from random import randint
from math import sqrt
# --- Constantes ---
ANCHO_PANTALLA=800
LARGO_PANTALLA=600

class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color
    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)
    def update(self):
        # Move the ball
        if self.position_y>=LARGO_PANTALLA-25-self.radius or self.position_y<=25+self.radius:
            self.change_y = -self.change_y
        if self.position_x>=ANCHO_PANTALLA-25-self.radius or self.position_x<=25+self.radius:
            self.change_x = -self.change_x
        self.position_y += self.change_y
        self.position_x += self.change_x
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(ANCHO_PANTALLA,LARGO_PANTALLA,"Control del Usuario")
        self.ball = Ball(400, 300, 1, 1, 30, arcade.color.AMARANTH_PINK)
    def on_draw(self):
        arcade.set_background_color(arcade.color.BONE)
        arcade.start_render()
        self.box()
        self.ball.draw()

    def box(self):
        r=self.ball.radius
        arcade.draw_rectangle_filled(ANCHO_PANTALLA/2, LARGO_PANTALLA/2, ANCHO_PANTALLA-(r*2), LARGO_PANTALLA-(r*2), arcade.color.AMARANTH)
        arcade.draw_lrtb_rectangle_filled(r, r*2, LARGO_PANTALLA-r, r, arcade.color.AMARANTH_PURPLE)
        arcade.draw_lrtb_rectangle_filled(r, ANCHO_PANTALLA-r, r*2, r, arcade.color.AMARANTH_PURPLE)
        arcade.draw_lrtb_rectangle_filled(r, ANCHO_PANTALLA-r, LARGO_PANTALLA-r, LARGO_PANTALLA-(r*2), arcade.color.AMARANTH_PURPLE)
        arcade.draw_lrtb_rectangle_filled(ANCHO_PANTALLA-(r*2), ANCHO_PANTALLA - r, LARGO_PANTALLA-r, r, arcade.color.AMARANTH_PURPLE)
        arcade.draw_line(ANCHO_PANTALLA-r, r, ANCHO_PANTALLA-r, LARGO_PANTALLA-r, arcade.color.BLACK)
        arcade.draw_line(r, r, r, LARGO_PANTALLA-r, arcade.color.BLACK)
        arcade.draw_line(r, r, ANCHO_PANTALLA-r, r, arcade.color.BLACK)
        arcade.draw_line(r, LARGO_PANTALLA-r, ANCHO_PANTALLA-r, LARGO_PANTALLA-r, arcade.color.BLACK)
    def update(self, delta_time):
        self.ball.update()

    def on_mouse_press(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        if (745>=x>=55)&(545>=y>=55):
            self.ball.position_x = x
            self.ball.position_y = y
    def on_key_press(self, key, modifiers):
        if key==arcade.key.D:
            self.ball.change_x+=1
        elif key==arcade.key.W:
            self.ball.change_y+=1
        elif key == arcade.key.A:
            self.ball.change_x -= 1
        elif key == arcade.key.S:
            self.ball.change_y -= 1
def main():
    window = MyGame()
    arcade.run()


main()
