__author__ = 'sandile'
from numpy import*


def triangle_area(base, height):
    """
    calculates the area of a right angled triangle.
    :param base: the length of the base.
    :param height: the length of the height.
    :return: area of a triangle(units^2 from base and or height).
    >>>triangle_area(2,3)
    3
    """
    return (1/2)*base*height


def area_triangle(a, b, theta):
    """
    this too calculates the area of a triangle using two sides of the triangle and the angle the two lines form.
    :param a: one side of the triangle.
    :param b:another side of the triangle.
    :param theta: the interior angle formed by the two lines measured in degrees.
    :return: the area of the triangle, (units are units of side a*units of side b).
    >>>area_triangle(2, 3, 90)
    3
    """
    return a*b*sin(math.radians(theta))/2


def circumference(r):
    """
    calculates the distance around a circle called circumference using the radius of the circle.
    :param r: radius of the circle.
    :return:the distance around a circle(units are the same as those of radius).
    >>>circumference(7)
    44
    """
    return 2*(22/7)*r


def circum_ference(d):
    """
    it also calculates the circumference using the diameter.
    :param d: diameter of the circle.
    :return: returns the circumference using units of the diameter.
    >>>circum_ference(14)
    44
    """
    return 22*d/7


def volume_sphere(r):
    """
    calculates the volume of a sphere.
    :param r: is the radius of the sphere.
    :return:volume of the sphere in units^3 of the radius.
    >>>volume_sphere(2)
    33.524 (rounded to nearest 3 decimal places).
    """
    return 4*22*r*r*r/21


def area_circle(r):
    """
    calculates the area of a circle given the radius.
    :param r: is the radius of the circle.
    :return:area of the circle in units^2 of the radius.
    >>>area_circle(7)
    154
    """
    return (22/7)*r*r


def volume_cylinder(r, h):
    """
    calculates the volume of a cylinder.
    :param r: the radius of the circular part of the cylinder.
    :param h: is the perpendicular distance to the circular part from the bottom to the top of the cylinder.
    :return:volume of the cylinder (units of the radius*units of the height).
    >>>volume_cylinder(7,2)
    308
    """
    return (22/7)*r*r*h


def arc_length(r, theta):
    """
    calculates the area of an arc, when the radius of the arc and the angle subtended by the arc is known.
    :param r: the radius of the arc.
    :param theta: angle subtended by the arc.
    :return: the length of the arc in units of the radius.
    >>>arc_length(7,90)
    11
    """
    return 11*theta*r/630


def volume_cuboid(l, b, h):
    """
    calculates the volume of a cuboid
    :param l: the length which is the distance of one of the edges of the cuboid.
    :param b: length of the breath of the cuboid.
    :param h: height of the cuboid.
    :return: the volume of the cuboid,in units of (length units*breath units*height unit).
    >>>volume_cuboid(2,3,4)
    24
    """
    return l*b*h


def surface_area_cuboid(l, b, h):
    """
    calculates the surface area of a cuboid using the three sides of the cube.
    :param l: length of the cuboid.
    :param b: breath of the cuboid.
    :param h: height of the cuboid.
    :return: volume of the cuboid in units of length units*base units*height units.
    >>>surface_area_cuboid(2,3,4)
    52
    """
    return 2*(l*(b+h)+b*h)


def area_parallelogram(h, b):
    """
    calculates the area of a parallelogram
    :param h: height that is perpendicular to the base of the parallelogram
    :param b: base of the parallelogram
    :return:area of a parallelogram in height units*length units
    >>>area_parallelogram(2,4)
    8
    """
    return b*h


def volume_cone(r, h):
    """
    calculates the volume of a cone
    :param r: the radius of the circular part of the cone
    :param h: is the perpendicular height from the center of circle making the cone to the peak of the  cone.
    >>>volume_cone(7,3)
    77
    :return:the volume of the cone in height units*radius units*radius units
    """
    return (22/7)*r*r*h/3


def volume_right_pyramid(l, w, h):
    """
    calculates the volume of a square based pyramid
    :param l: the base length
    :param w: the base width
    :param h: the pyramid height
    :return: the volume of the pyramid in base length units*base width units*pyramid height units
    >>>volume_right_pyramid(2,3,4)
    24
    """
    return l*w*h/3
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