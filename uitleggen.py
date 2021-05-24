# Different Rectangle.
class Point:
    def __init__(self, x=0.0, y=0.0, name=''):
        self.x = x
        self.y = y
        self.name = name

    def __gt__(self, other):
        if isinstance(other, Point):
            if self.x > other.x and self.y > other.y:
                return True
            else:
                return False
        elif isinstance(other, int):
            if self.x > other and self.y > other:
                return True
            else:
                return False
        else:
            raise NotImplementedError

    def __lt__(self, other):
        if isinstance(other, Point):
            if self.x < other.x and self.y < other.y:
                return True
            else:
                return False
        elif isinstance(other, int):
            if self.x < other and self.y < other:
                return True
            else:
                return False
        else:
            raise NotImplementedError

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

    def __add__(self, add):
        if isinstance(add, Point):
            new_x = self.x + add.x
            new_y = self.y + add.y
        elif isinstance(add, int):
            new_x = self.x + add
            new_y = self.y + add
        else:
            raise NotImplementedError
        return Point(new_x, new_y)


class Rectangle:
    def __init__(self, top_left, lower_right):
        self.top_left = top_left
        self.lower_right = lower_right

    @property
    def height(self):
        return abs(self.lower_right.y - self.top_left.y)

    @property
    def width(self):
        return abs(self.lower_right.x - self.top_left.x)


a = Point(2, 1)
b = Point(3, 1)
if a == b:
    print("Party we did it the same")
elif a > b:
    print("A is meer dan B")
elif a + 4 > b:
    print('A is meer dan B')
