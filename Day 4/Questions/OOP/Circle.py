import math


class Circle:
    """
    A class to represent a circle and perform basic geometric calculations.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initialize a Circle object with a given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius
        print("Circle object created")

    def cal_area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle using the formula πr².
        """
        return math.pi * self.radius**2
