Polygons

class polygon()

methods:
- set_color()
    - Takes in a tuple with three floats, ranging from 0-1
    - each value represents the proportion of red, green, and blue
    - Changes the color of the outline of the polygon to be drawn
- set_faces()
    - Takes in an integer, representing the number of faces in the polygon to be drawn
    - Values below 3 will draw a line
- set_bg()
    - Takes in a tuple with three floats, ranging from 0-1
    - each value represents the proportion of red, green, and blue
    - Changes the color of the background
- set_width()
    - Takes in an integer, representing the thickness of the outline of the polygon to be drawn
    - negative value throws an error
- set_face_len()
    - Takes in an integer, representing the length of each side of the polygon to be drawn
- set_fade()
    - Takes in a tuple with three floats, ranging from 0-1
    - each value represents the proportion of red, green, and blue
    - The color of the outline of the polygon to be drawn will fade from it’s initial color to the color specified as the polygon is drawn
- set_pos()
    - Takes in a tuple with two floats, the first value is the x coordinate, the second value is the y coordinate
    - changes where the turtle starts drawing the polygon from
- set_speed()
    - Takes in an integer, representing how fast the polygon is drawn
    - 1 is the slowest, higher numbers increase speed
    - 0 is the fastest
- render()
    - Takes no arguments
    - draws the polygon according to the specifications given above
- clear()
    - Erases the polygon once it has been drawn

class doublepoly()

methods:
- set_color()
    - Takes in a tuple with three floats, ranging from 0-1
    - each value represents the proportion of red, green, and blue
    - Changes the color of the outline of the polygon to be drawn
- set_bg()
    - Takes in a tuple with three floats, each value represents the proportion of red, green, and blue
    - Changes the color of the background
- set_width()
    - Takes in an integer, representing the thickness of the outline of the polygon to be drawn
    - negative value throws an error
- set_pos()
    - Takes in a tuple with three floats, the first value is the x coordinate, the second value is the y coordinate
    - changes where the turtle starts drawing the polygon from
- set_speed()
    - Takes in an integer, representing how fast the polygon is drawn
    - 1 is the slowest, higher numbers increase speed
    - 0 is the fastest
- set_loops()
    - Takes in an integer, representing how many times the full cycle of colours should repeat
    - 0 means loop infinitely
- set_fade()
    - Takes in a list of tuples, each containing three floats, ranging from 0-1
    - each value represents the proportion of red, green, and blue
    - The color of the outline of the polygons to be drawn will fade through all the colors in the list, starting from the initial color
- set_faces_inner()
    - Takes in an integer, representing the number of faces of the polygons drawn in the inner loop
- set_faces_outer()
    - Takes in an integer, representing the number of faces of the polygons drawn in the outer loop
- set_face_len_inner()
    - Takes in an integer, representing the length of the faces of the polygons drawn in the inner loop
- set_face_len_outer()
    - Takes in an integer, representing the length of the faces of the polygons drawn in the outer loop
- render()
    - Takes no arguments
    - draws the polygon according to the specifications given above
- clear()
    - Erases the polygon once it has been drawn

functions

- done()
    - ends the program, keeping the drawn content on the screen