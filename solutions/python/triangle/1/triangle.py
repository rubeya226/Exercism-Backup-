# a = sides[0]
# b = sides[1]
# c = sides[2]
def is_triangle(sides):
    return (sides[0] != 0 and sides[1] !=0 and sides[2] != 0) and (sides[0] + sides[1] >= sides[2]) and (sides[1] + sides[2] >= sides[0]) and (sides[0] + sides[2] >= sides[1])

def equilateral(sides):
    return sides[0] == sides[1] == sides[2] and is_triangle(sides)

def isosceles(sides):
    return (sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]) and is_triangle(sides)


def scalene(sides):
    return sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2] and is_triangle(sides)
