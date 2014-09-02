__author__ = 'sandile'
from numpy import*


def triangle_area(base, height):
    """
    calculates the area of a right angled triangle.
    :param base: the length of the base.
    :param height: the length of the height.
    :return: area of a triangle(units^2 from base and or height).
    >>> triangle_area(2, 3)
    3.0
    """
    return (1/2)*base*height


def area_triangle(side1, side2, theta):
    """
    this too calculates the area of a triangle using two sides of the triangle and the angle the two lines form.
    :param side1: length of one side of the triangle.
    :param side2: length of another side of the triangle.
    :param theta: the interior angle formed by the two lines measured in degrees.
    :return: the area of the triangle, (units are units of side1*units of side2).
    >>> area_triangle(2, 3, 90)
    3.0
    """
    return side1*side2*sin(math.radians(theta))/2


def circumference(radius):
    """
    calculates the distance around a circle called circumference using the radius of the circle.
    :param radius: radius length.
    :return:the distance around a circle(units are the same as those of radius).
    >>> circumference(7)
    44.0
    """
    return 2*(22/7)*radius


def circum_ference(diameter):
    """
    it also calculates the circumference using the diameter.
    :param diameter: diameter length of the circle.
    :return: returns the circumference using units of the diameter's length.
    >>> circum_ference(14)
    44.0
    """
    return 22*diameter/7


def volume_sphere(radius):
    """
    calculates the volume of a sphere.
    :param radius: is the radius length of the sphere.
    :return:volume of the sphere in units^3 of the radius.
    >>> volume_sphere(2)
    33.523809523809526
    """
    return 4*22*radius*radius*radius/21


def area_circle(radius):
    """
    calculates the area of a circle given the radius length.
    :param radius: is the radius length of the circle.
    :return:area of the circle in units^2 of the radius.
    >>> area_circle(7)
    154.0
    """
    return (22/7)*radius*radius


def volume_cylinder(radius, height):
    """
    calculates the volume of a cylinder.
    :param radius: the radius length of the circular part of the cylinder.
    :param height: is the perpendicular distance to the circular part from the bottom to the top of the cylinder.
    :return:volume of the cylinder (units of the radius*units of the height).
    >>> volume_cylinder(7,2)
    308.0
    """
    return (22/7)*radius*radius*height


def arc_length(radius, theta):
    """
    calculates the area of an arc, when the radius of the arc and the angle subtended by the arc is known.
    :param radius: the radius length of the arc.
    :param theta: angle subtended by the arc in degrees.
    :return: the length of the arc in units of the radius.
    >>> arc_length(7, 90)
    11.0
    """
    return 11*theta*radius/630


def volume_cuboid(length, breath, height):
    """
    calculates the volume of a cuboid
    :param length: the length which is the distance of one of the edges of the cuboid.
    :param breath: length of the breath of the cuboid.
    :param height: height of the cuboid.
    :return: the volume of the cuboid,in units of (length units*breath units*height unit).
    >>> volume_cuboid(2,3,4)
    24
    """
    return length*breath*height


def surface_area_cuboid(length, breath, height):
    """
    calculates the surface area of a cuboid using the three sides of the cube.
    :param length: length of the cuboid.
    :param breath: breath of the cuboid.
    :param height: height of the cuboid.
    :return: volume of the cuboid in units of length units*base units*height units.
    >>> surface_area_cuboid(2,3,4)
    52
    """
    return 2*(length*(breath+height)+breath*height)


def area_parallelogram(height, breath):
    """
    calculates the area of a parallelogram.
    :param height: length of the height that is perpendicular to the base of the parallelogram.
    :param breath: length of the base of the parallelogram.
    :return:area of a parallelogram in units of height units*length units.
    >>> area_parallelogram(2,4)
    8
    """
    return breath*height


def volume_cone(radius, height):
    """
    calculates the volume of a cone.
    :param radius: the radius length of the circular part of the cone.
    :param height: is the perpendicular height
    :return the volume of the cone ( in unit **3)
    >>> volume_cone(7, 3)
    154.0
    """
    return (22/7)*radius*radius*height/3


def volume_right_pyramid(length, width, height):
    """
    calculates the volume of a square based pyramid.
    :param length: the base length.
    :param width: the base width.
    :param height: the pyramid height.
    :return: the volume of the pyramid in base length units*base width units*pyramid height units.
    >>> volume_right_pyramid(2,3,4)
    8.0
    """
    return length*width*height/3
if __name__ == "__main__":
    print("area:",
          triangle_area(2, 3))
    print("area_triangle:",
          area_triangle(2, 3, 90))
    print("circumference:",
          circumference(7))
    print("circum_ference:",
          circum_ference(14))
    print("volume_sphere:",
          volume_sphere(2))
    print("area_circle:",
          area_circle(7))
    print("volume_cylinder:",
          volume_cylinder(7, 2))
    print("arc_length:",
          arc_length(7, 90))
    print("volume_cuboid:",
          volume_cuboid(2, 3, 4))
    print("surface_area_cuboid:",
          surface_area_cuboid(2, 3, 4))
    print("area_parallelogram:",
          area_parallelogram(2, 4))
    print("volume_cone:",
          volume_cone(7, 3))
    print("volume_right_pyramid:",
          volume_right_pyramid(2,3,4))