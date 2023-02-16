# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(1800, 640, "Still Life")

# Set the background color
arcade.set_background_color(arcade.color.BONE)

# Get ready to draw
arcade.start_render()

# Primera prueba..
'''arcade.draw_circle_filled(100,100,50,arcade.color.DARK_SALMON)
arcade.draw_circle_filled(180,100,50,arcade.color.DARK_SALMON)
arcade.draw_rectangle_filled(140,200,80,200,arcade.color.DARK_SALMON)
arcade.draw_parabola_filled(95,150,185,150,arcade.color.CHERRY_BLOSSOM_PINK)
arcade.draw_line(140,355,140,375,arcade.color.BLACK)'''

# Table
arcade.draw_rectangle_filled(650,250,1200,150,arcade.color.LIGHT_BROWN)
arcade.draw_lrtb_rectangle_filled(55,75,200,0,arcade.color.LIGHT_BROWN)
arcade.draw_lrtb_rectangle_filled(1225,1245,200,0,arcade.color.LIGHT_BROWN)

# Bowl
arcade.draw_ellipse_filled(650,300,600,150,arcade.color.COCOA_BROWN)
arcade.draw_ellipse_outline(650,300,600,150,arcade.color.DARK_BROWN)

#Apple
arcade.draw_circle_filled(780,320,60,arcade.color.RED_ORANGE)
arcade.draw_circle_outline(780,320,60,arcade.color.DARK_RED)

#Pear
arcade.draw_arc_filled(590,320,120,80,arcade.color.YELLOW_GREEN,135,405)
arcade.draw_arc_outline(590,320,120,80,arcade.color.DARK_GREEN,135,405)
arcade.draw_parabola_filled(548,200,632,140,arcade.color.YELLOW_GREEN)
arcade.draw_parabola_outline(548,200,632,140,arcade.color.DARK_GREEN)
arcade.draw_triangle_filled(548,350,632,350,590,315,arcade.color.YELLOW_GREEN)

#
#arcade.draw_circle_filled(100, 100, 5, arcade.color.CHERRY_BLOSSOM_PINK)
#arcade.draw_circle_filled(180, 100, 5, arcade.color.CHERRY_BLOSSOM_PINK)
#sample code
    #arcade.draw_circle_filled(x, y, radio, arcade.color.)
    #arcade.draw_rectangle_filled(x,y,largo,alto color)
    #arcade.draw_triangle_filled(x1,y1.x2,y2,x3,y3,largo,alto color)
    #_lrtb_rectangle_filled(left rigth top bottom por coordenadas de donde están estas)
    #polygon tiene [x,y] por cada punto del polígono

# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()

