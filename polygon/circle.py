import polygons as poly

p = poly.polygon()
p.set_width(10)
p.set_faces(32)
p.set_face_len(20)
p.set_fade((0,1,1))
p.set_pos((0,-100))
p.set_speed(3)

q = poly.polygon()
q.set_width(10)
q.set_faces(32)
q.set_face_len(20)
q.set_color((0,1,1))
q.set_fade((1,1,1))
q.set_pos((0,-100))
q.set_speed(3)

for a in range(10):
    p.render()
    q.clear()
    q.render()
    p.clear()

poly.done()
