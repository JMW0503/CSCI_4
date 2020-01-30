import turtle

skk = turtle.Turtle()

f = open("shapeInstructions1.txt", "r")
lines = f.readlines()
for line in lines:
    line = line.rstrip()
    line_pieces = line.split()
    direction = line_pieces[0]
    distance = int(line_pieces[1])
    if direction == "forward":
        skk.fd(distance)
    if direction == "left":
        skk.lt(distance)
    if direction == "right":
        skk.rt(distance)


