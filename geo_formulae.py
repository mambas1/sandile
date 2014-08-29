__author__ = 'sandile'
from numbers import Number
def triangle_area(base,height):
    """
    calculates the area of a right angled triangle.
    :param base: the length of the base.
    :param height: the length of the height.
    :return:returns area of a triangle(units^2 from base and or height)
    >>>triangle_area(2,3)
    3
    """
    return (1/2)*base*height
print(triangle_area(2,3))