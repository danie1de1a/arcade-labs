import arcade
import random

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.1
SPRITE_SCALING_BANANA = 0.1
SPRITE_SCALING_COCONUT = 0.015

BANANA = 69
COCONUT = 10

LARGO_PANTALLA = 600
ANCHO_PANTALLA = 800

class MyGame(arcade.View):
    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__()

        # Variables that will hold sprite lists.
        self.player_list = arcade.SpriteList()
        self.banana_list = arcade.SpriteList()
        self.coconut_list = arcade.SpriteList()

        # Set up the player info
        self.player_sprite = arcade.Sprite("player_sprite.png", SPRITE_SCALING_PLAYER)
        self.window.score = 0

        # Don't show the mouse cursor
        self.window.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """
        # Set up the player
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(BANANA):
            banana = arcade.Sprite("good_sprite.png", SPRITE_SCALING_BANANA)
            banana.center_x = random.randrange(ANCHO_PANTALLA)
            banana.center_y = random.randrange(LARGO_PANTALLA)
            self.banana_list.append(banana)

        for i in range(COCONUT):
            coconut = arcade.Sprite("bad_sprite.png", SPRITE_SCALING_COCONUT)
            coconut.center_x = 20+random.randrange(ANCHO_PANTALLA-40)
            coconut.center_y = random.randrange(LARGO_PANTALLA)
            coconut.direction = 1
            self.coconut_list.append(coconut)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.banana_list.draw()
        self.coconut_list.draw()
        center_x=75
        for i in range(len(self.coconut_list)-2):
            arcade.draw_circle_filled(center_x,LARGO_PANTALLA-20,7,arcade.color.RED)
            center_x+=15
        # Put the text on the screen.
        arcade.draw_text("Vidas:",10,LARGO_PANTALLA-25,arcade.color.WHITE,14)
        if (self.window.score > 0):
            output = "Mono-felicidad: " + str(self.window.score)
        else:
            output = "Mono está triste :("
        arcade.draw_text("Nivel: "+str(self.window.nivel), 10, 40, arcade.color.WHITE, 18)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 18)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y


    def update(self, delta_time):
        """ Movement and game logic """
        self.banana_list.update()
        self.coconut_list.update()

        for coconut in self.coconut_list:
            coconut.center_x += self.window.speed*coconut.direction
            if 20 > coconut.center_x or coconut.center_x > (ANCHO_PANTALLA-20):
                coconut.direction *= -1


        # Generate a list of all sprites that collided with the player.
        banana_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.banana_list)
        coconut_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coconut_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for banana in banana_hit_list:
            banana.remove_from_sprite_lists()
            self.window.score += 1

        if (len(self.banana_list) == 0) or (len(self.coconut_list) < 3):
            game_over_view = GameOverView()
            self.window.show_view(game_over_view)

        for coconut in coconut_hit_list:
            coconut.remove_from_sprite_lists()
            self.window.score -= 9

class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
        self.window.total_score += self.window.score

    def on_draw(self):
        arcade.start_render()
        """
        Draw "Game over" across the screen.
        """
        if self.window.score>0:
            arcade.draw_text("Felicidades, has hecho feliz al mono", 15, 400, arcade.color.WHITE, 35)
            arcade.draw_text("Haz click para jugar al mono-juego", 150, 300, arcade.color.WHITE, 24)
        else:
            arcade.draw_text("Muy mal, el mono ahora está muy triste", 15, 400, arcade.color.WHITE, 32)
            arcade.draw_text("Haz click para salir", 220, 300, arcade.color.WHITE, 24)

        arcade.draw_text("Mono-felicidad: "+str(self.window.total_score), 10,20,arcade.color.WHITE, 24)


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if self.window.score>0:
            juego = MyGame()
            self.window.score = 0
            self.window.speed += 2
            self.window.nivel += 1
            self.window.show_view(juego)
            juego.setup()
        else:
            arcade.close_window()
def main():
    """ Main method """
    window = arcade.Window(ANCHO_PANTALLA, LARGO_PANTALLA, "Mono-Juego")
    juego = MyGame()
    window.score = 0
    window.speed = 2
    window.nivel = 1
    window.total_score = window.score
    window.show_view(juego)
    juego.setup()
    arcade.run()

if __name__ == "__main__":
    main()