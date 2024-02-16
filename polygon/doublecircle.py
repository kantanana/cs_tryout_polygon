import polygons as poly

p = poly.doublepoly()

p.set_color((1,0.59,0.59))
p.set_fade([(1,0.8,0.59),(1,1,0.59),(0.59,1,0.59),(0.59,1,1),(0.59,0.59,1),(1,0.59,1)])

p.set_pos((0,-50))

p.set_loops(1)

p.set_speed(0)

p.set_face_len_inner(20)
p.set_face_len_outer(20)

p.set_faces_inner(32)
p.set_faces_outer(32)

p.set_width(8)

p.render()
poly.done()

