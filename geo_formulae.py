__author__ = 'sandile'
from numpy import*
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
def circumference(r):
    """
    calculates the distance around a circle called circumference
    :param r: radius of the circle
    :return:the distance around a circle(units are the same as radius
    >>>circumference(7)
    22
    """
    return 2*pi*r
    print(circumference(7))
def volume_sphere(r):
    """
    calculates the volume of a sphere
    :param r: is the radius of the sphere
    :return:volume of the sphere in units^3 of the radius
    >>>volume_sphere(2)
    33.524 (rounded to nearest 3 decimal places)
    """
    return (4/3)*(pi*r^3)
def area_circle(r):
    """
    calculates the area of a circle
    :param r: r is the radius of the circle
    :return:area of the circle in units^2 of the radius
    >>>area_circle(7)
    154
    """
    return pi*r*r
def volume_cylinder(r,h):
    """
    calculates the volume of a cylinder
    :param r: the radius of the circular part of the cylinder
    :param h: is the perpendicular distance to thr circular part from the bottom to the top of the cylinder
    :return:volume of the cylinder in units^2 of the radius*units of the height
    >>>volume_cylinder(7,2)
    304
    """
    return pi*r*r*h
