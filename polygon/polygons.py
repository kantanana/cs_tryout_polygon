import turtle

class polygon:

    def __init__(self):
        
        self.face_len = 40
        self.faces = 6
        self.bgcolor = (0,0,0)
        self.width = 5
        self.color = (1,1,1)
        self.fade = None
        self.pos = (0,0)
        self.speed = 5
        self.t = turtle.Turtle()

    def set_color(self, color):
        self.color = color

    def set_faces(self, faces):
        self.faces = faces

    def set_bg(self, bg):
        self.bgcolor = bg

    def set_width(self, width):
        self.width = width

    def set_face_len(self, length):
        self.face_len = length

    def set_fade(self, fade):
        self.fade = fade

    def set_pos(self, pos):
        self.pos = pos

    def set_speed(self, speed):
        self.speed = speed

    def render(self):

        t = self.t
        
        turtle.tracer(self.speed, 0)
        turtle.bgcolor(self.bgcolor)
        
        t.ht()

        t.penup()
        t.forward(self.pos[0])
        t.left(90)
        t.forward(self.pos[1])
        t.right(90)
        t.pendown()
        
        t.width(self.width)
        t.color(self.color)

        if self.fade != None:
            old = list(self.color)
            new = self.fade
            rstep = (new[0] - old[0])/self.faces
            gstep = (new[1] - old[1])/self.faces
            bstep = (new[2] - old[2])/self.faces

        turn = 360/self.faces
        for a in range(self.faces):

            t.forward(self.face_len)
            t.left(turn)

            if self.fade != None:
                old[0] += rstep
                old[1] += gstep
                old[2] += bstep
                t.color(old)

        turtle.update()
                
    def clear(self):
        self.t.reset()

class doublepoly:

    def __init__(self):
        
        self.face_len_inner = 10
        self.face_len_outer = 10
        self.faces_inner = 32
        self.faces_outer = 32
        self.bgcolor = (0,0,0)
        self.width = 5
        self.color = (1,1,1)
        self.fade = None
        self.pos = (0,0)
        self.speed = 5
        self.loops = 1
        
        self.one = turtle.Turtle()
        self.two = turtle.Turtle()

    def set_color(self, color):
        self.color = color

    def set_faces_inner(self, faces):
        self.faces_inner = faces

    def set_faces_outer(self, faces):
        self.faces_outer = faces

    def set_bg(self, bg):
        self.bgcolor = bg

    def set_width(self, width):
        self.width = width

    def set_face_len_inner(self, length):
        self.face_len_inner = length

    def set_face_len_outer(self, length):
        self.face_len_outer = length

    def set_fade(self, fade):
        self.fade = fade

    def set_pos(self, pos):
        self.pos = pos

    def set_speed(self, speed):
        self.speed = speed

    def set_fade(self, fade):
        self.fade = fade

    def set_loops(self, loops):
        self.loops = loops

    def clear(self):
        self.t.reset()

    def render(self):

        one = self.one
        two = self.two

        turtle.tracer(self.speed, 0)
        turtle.bgcolor(self.bgcolor)

        one.ht()
        two.ht()

        one.penup()
        one.forward(self.pos[0])
        one.left(90)
        one.forward(self.pos[1])
        one.right(90)
        one.pendown()

        two.penup()
        two.forward(self.pos[0])
        two.left(90)
        two.forward(self.pos[1])
        two.right(90)
        two.pendown()

        one.width(self.width)
        two.width(self.width)

        if self.loops != 0:
            counter = 0

        cont = True

        while cont:

            if self.loops != 0:
                if counter == self.loops - 1:
                    cont = False
                else:
                    counter += 1

            one.color(self.color)

            if self.fade != None:
                colors = [self.color] + self.fade
                index = 0
            else:
                two.color(self.color)

            cycle = True

            while cycle:

                if self.fade != None:

                    if index == len(colors) - 1:
                        index = 0
                        cycle = False
                    else:
                        index += 1

                    new = list(colors[index])
                    old = list(colors[index-1])
                    current = list(colors[index-1])

                    rstep = (new[0] - old[0])/(self.faces_outer*2)
                    gstep = (new[1] - old[1])/(self.faces_outer*2)
                    bstep = (new[2] - old[2])/(self.faces_outer*2)

                for outer_one in range(self.faces_outer):

                    one.forward(self.face_len_inner/2)
                    turn = 360/self.faces_inner
                    
                    for inner_one in range(self.faces_inner - 1):

                        one.right(turn)
                        one.forward(self.face_len_inner)

                    one.right(turn)
                    one.forward(self.face_len_inner/2)

                    turn = 360/self.faces_outer

                    one.forward(self.face_len_outer/2)
                    one.left(turn)
                    one.forward(self.face_len_outer/2)

                    turtle.update()

                    if self.fade != None:

                        current[0] += rstep
                        current[1] += gstep
                        current[2] += bstep

                        one.color(tuple(current))
                    
                two.clear()

                if self.fade != None:
                    two.color(tuple(current))
                else:
                    break

                for outer_two in range(self.faces_outer):

                    two.forward(self.face_len_inner/2)
                    turn = 360/self.faces_inner

                    for inner_two in range(self.faces_inner - 1):

                        two.right(turn)
                        two.forward(self.face_len_inner)

                    two.right(turn)
                    two.forward(self.face_len_inner/2)

                    turn = 360/self.faces_outer

                    two.forward(self.face_len_outer/2)
                    two.left(turn)
                    two.forward(self.face_len_outer/2)

                    turtle.update()

                    if self.fade != None:

                        current[0] += rstep
                        current[1] += gstep
                        current[2] += bstep

                        two.color(tuple(current))

                one.clear()

                if self.fade != None:
                    one.color(tuple(current))

def done():
    turtle.done()
