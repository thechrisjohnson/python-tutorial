class Point:
    __match_args__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")


def where_is_two(points):
    match points:
        case []:
            print("No points")
        case [Point(0, 0)]:
            print("The origin")
        case [Point(x, y)]:
            print(f"Single point {x}, {y}")
        case [Point(0, y1), Point(0, y2)]:
            print(f"Two on the Y axis at {y1}, {y2}")
        case _:
            print("Something else")

def on_diagonal(point):
    match point:
        case Point(x, y) if x == y:
            print(f"Y=X at {x}")
        case Point(x, y):
            print(f"Not on the diagonal")

one = Point(x=0, y=0)
two = Point(x=0, y=1)
three = Point(x=1, y=0)
four = Point(x=1, y=1)

where_is(two)
where_is(one)
where_is(four)
where_is(three)

where_is_two([one, two])
where_is_two([])
where_is_two([three])
where_is_two([four])

on_diagonal(one)
on_diagonal(two)
on_diagonal(three)
on_diagonal(four)
