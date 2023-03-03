# import math
import math


class Point:
    def __init__(self, x=0, y=0):

        self.x=x
        self.y=y
    def __str__(self):
        return f'{self.x}, {self.y}'

    def colculate_distance(self, other_point):
        # print(self.x) #
        # print(other_point.x)
        print(math.sqrt((self.x-other_point.x)**2 * (self.y-other_point.y)**2 ))

        # self.

        # distance = math.sqrt(((x2-x1)**2)*(y2-y1)**2))

p1=Point(5, 10)
p2=Point(4, 7)

p2.colculate_distance(p1)
# p2.colculate_distance(p2)

