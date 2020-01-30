# cat = "forward 100"
# dog = cat.split()
# mouse = dog[1]
# mouse = int(dog[1]) + int(dog[1])
# print(mouse)


line = "forward 100"
line_pieces = line.split()
direction = line_pieces[0]
distance = int(line_pieces[1])
print(direction)
print(distance)