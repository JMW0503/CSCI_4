


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


ListOfPoints = []
with open("points.txt", 'r') as pointsFile:
    for line in pointsFile:
        coordinates = line.split(',')
        coordinates[0]
        coordinates[1]
        
print(coordinates)

#         ListOfPoints.append(newPoint)





# len(ListOfPoint)
# ListOfPoint.append(Point(1, 2), Point(3, 4))