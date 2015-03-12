import unittest


class Point:

    def __init__(self, x, y):
        """
        :param int x: X coordinate for the point
        :param int y: Y coordinate for the point
        """
        self.x = x
        self.y = y

    def __lt__(self, other):
        """
        :param Point other: The other point to compare to
        :return: bool
        """
        return self.x < other.x and self.y < other.y

    def __gt__(self, other):
        """
        :param Point other: The other point to compare to
        :return: bool
        """
        return self.x > other.x and self.y > other.y


class Rectangle:

    def __init__(self, top_left, top_right, bottom_left, bottom_right):
        """
        :param Point top_left: The top left point of the rectangle
        :param Point top_right: The top right point of the rectangle
        :param Point bottom_left: The bottom left point of the rectangle
        :param Point bottom_right: The bottom right point of the rectangle
        """
        self.top_left = top_left
        self.top_right = top_right
        self.bottom_left = bottom_left
        self.bottom_right = bottom_right

    def intersects(self, other):
        """
        :param Rectangle other: The other rectangle to check if it intersects
        :return: bool
        """
        if self.top_left > other.top_left:
            rect1 = self
            rect2 = other
        else:
            rect1 = other
            rect2 = self

        for point in rect1.points():
            if (point > rect2.top_left) and (point < rect2.bottom_right):
                return True

        return False

    def points(self):
        """
        :return: list
        """
        return [self.top_left, self.top_right, self.bottom_left, self.bottom_right]

class TestIntersections(unittest.TestCase):

    def setUp(self):
        pass

    def test_no_intersection(self):
        """
        Tests two rectangles that do not intersect
        """
        rect1 = Rectangle(top_left=Point(0, 0), top_right=Point(10, 0),
                          bottom_left=Point(0, 10), bottom_right=Point(10, 10))
        rect2 = Rectangle(top_left=Point(20, 20), top_right=Point(30, 20),
                          bottom_left=Point(20, 30), bottom_right=Point(30, 30))

        self.assertFalse(rect1.intersects(rect2))
        self.assertFalse(rect2.intersects(rect1))

    def test_corner_intersection(self):
        """
        Tests two rectangles that intersect with overlapping corners
        """
        rect1 = Rectangle(top_left=Point(0, 0), top_right=Point(10, 0),
                          bottom_left=Point(0, 10), bottom_right=Point(10, 10))
        rect2 = Rectangle(top_left=Point(5, 5), top_right=Point(15, 5),
                          bottom_left=Point(5, 15), bottom_right=Point(15, 15))

        self.assertTrue(rect1.intersects(rect2))
        self.assertTrue(rect2.intersects(rect1))

    def test_inside_intersection(self):
        """
        Tests two rectangles that intersect by being within each other
        """
        rect1 = Rectangle(top_left=Point(0, 0), top_right=Point(10, 0),
                          bottom_left=Point(0, 10), bottom_right=Point(10, 10))
        rect2 = Rectangle(top_left=Point(2, 2), top_right=Point(8, 2),
                          bottom_left=Point(2, 8), bottom_right=Point(8, 8))

        self.assertTrue(rect1.intersects(rect2))
        self.assertTrue(rect2.intersects(rect1))

    def test_cross_intersection(self):
        """
        Tests two rectangles that intersect in a cross pattern
        """
        rect1 = Rectangle(top_left=Point(0, 10), top_right=Point(30, 10),
                          bottom_left=Point(0, 20), bottom_right=Point(30, 20))
        rect2 = Rectangle(top_left=Point(10, 0), top_right=Point(20, 0),
                          bottom_left=Point(10, 30), bottom_right=Point(20, 30))

        self.assertTrue(rect1.intersects(rect2))
        self.assertTrue(rect2.intersects(rect1))