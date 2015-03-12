import unittest


class Point:

    def __init__(self, x, y):
        """
        :param int x: X coordinate for the point
        :param int y: Y coordinate for the point
        """
        self.x = x
        self.y = y


class Rectangle:

    def __init__(self, top_left, bottom_right):
        """
        :param Point top_left: The top left point of the rectangle
        :param Point bottom_right: The bottom right point of the rectangle
        """
        self.top_left = top_left
        self.bottom_right = bottom_right

    def intersects(self, other):
        """
        :param Rectangle other: The other rectangle to check if it intersects
        :return: bool
        """

        # Check if the rectangles are next to each other
        if self.bottom_right.x < other.top_left.x or other.bottom_right.x < self.top_left.x:
            return False

        # Check if the rectangles are on top of each other
        if self.bottom_right.y < other.top_left.y or other.bottom_right.y < self.top_left.y:
            return False

        # The rectangles must be overlapping
        return True


class TestIntersections(unittest.TestCase):

    def setUp(self):
        pass

    def test_no_intersection(self):
        """
        Tests two rectangles that do not intersect
        """
        rect1 = Rectangle(top_left=Point(10, 10), bottom_right=Point(20, 20))
        rect2 = Rectangle(top_left=Point(30, 30), bottom_right=Point(40, 40))

        self.assertFalse(rect1.intersects(rect2))
        self.assertFalse(rect2.intersects(rect1))

    def test_corner_intersection(self):
        """
        Tests two rectangles that intersect with overlapping corners
        """
        rect1 = Rectangle(top_left=Point(0, 0), bottom_right=Point(10, 10))
        rect2 = Rectangle(top_left=Point(5, 5), bottom_right=Point(15, 15))

        self.assertTrue(rect1.intersects(rect2))
        self.assertTrue(rect2.intersects(rect1))

    def test_inside_intersection(self):
        """
        Tests two rectangles that intersect by being within each other
        """
        rect1 = Rectangle(top_left=Point(0, 0), bottom_right=Point(10, 10))
        rect2 = Rectangle(top_left=Point(2, 2), bottom_right=Point(8, 8))

        self.assertTrue(rect1.intersects(rect2))
        self.assertTrue(rect2.intersects(rect1))

    def test_cross_intersection(self):
        """
        Tests two rectangles that intersect in a cross pattern
        """
        rect1 = Rectangle(top_left=Point(0, 10), bottom_right=Point(30, 20))
        rect2 = Rectangle(top_left=Point(10, 0), bottom_right=Point(20, 30))

        self.assertTrue(rect1.intersects(rect2))
        self.assertTrue(rect2.intersects(rect1))

    def test_same_rectangles_intersection(self):
        """
        Tests two rectangles that are exactly on top of each other
        """
        rect1 = Rectangle(top_left=Point(0, 0), bottom_right=Point(10, 10))
        rect2 = Rectangle(top_left=Point(0, 0), bottom_right=Point(10, 10))

        self.assertTrue(rect1.intersects(rect2))
        self.assertTrue(rect2.intersects(rect1))

    def test_single_point_intersection(self):
        """
        Tests where one of the rectangles is a single point
        """
        rect1 = Rectangle(top_left=Point(0, 0), bottom_right=Point(10, 10))
        rect2 = Rectangle(top_left=Point(0, 0), bottom_right=Point(0, 0))

        self.assertTrue(rect1.intersects(rect2))
        self.assertTrue(rect2.intersects(rect1))