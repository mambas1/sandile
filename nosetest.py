__author__ = 'sandile'
from geom_formulae import*
from nose.tools import *


@raises(TypeError)
def triangle_area_other():
    triangle_area("a string", 3) or triangle_area(2, "a string")


@raises(ValueError)
def triangle_area_other():
    triangle_area(-2, 3) or triangle_area(2, -3)

@raises(AttributeError)
def triangle_area_other():
    triangle_area(None, 3) or triangle_area(2, None)

@raises(TypeError)
def circumference_other():
    circumference("a string")

@raises(ValueError)
def circumference_other():
    circumference(-7)

@raises(AttributeError)
def circumference_other():
    triangle_area(None)

@raises(TypeError)
def area_circle_other():
    area_circle("a string")

@raises(ValueError)
def area_circle_other():
    area_circle(-7)

@raises(AttributeError)
def area_circle_other():
    area_circle(None)

@raises(TypeError)
def volume_cylinder_other():
    volume_cylinder("a string", 4) or volume_cylinder(3, "a String")

@raises(ValueError)
def volume_cylinder_other():
    volume_cylinder(-2, 3) or volume_cylinder(2, -3)

@raises(AttributeError)
def volume_cylinder_other():
    volume_cylinder(None, 3) or volume_cylinder(2, None)


@raises(TypeError)
def arc_length_other():
    arc_length("a string", 90) or arc_length(7, "a string")

@raises(ValueError)
def arc_length_other():
    arc_length(-2, 90) or arc_length(2, -90)

@raises(AttributeError)
def arc_length_other():
    arc_length(None, 90) or arc_length(2, None)

@raises(TypeError)
def volume_cuboid_other():
    volume_cuboid("a string", 3, 4) or volume_cuboid(2, "a string", 4) or volume_cuboid(2, 3, "a string")

@raises(ValueError)
def volume_cuboid_other():
    volume_cuboid(-2, 3, 4) or triangle_area(2, -3, 4) or volume_cuboid(2, 3, -4)

@raises(AttributeError)
def volume_cuboid_other():
    volume_cuboid(None, 3, 4) or volume_cuboid(2, None, 4) or volume_cuboid(2, 3, None)

@raises(TypeError)
def surface_area_cuboid_other():
    surface_area_cuboid("a string", 3, 4) or surface_area_cuboid(2, "a string", 4)\
        or surface_area_cuboid(2, 3, "a string")

@raises(ValueError)
def surface_area_cuboid_other():
    surface_area_cuboid(-2, 3, 4) or surface_area_cuboid(2, -3, 4) or surface_area_cuboid(2, 3, -4)

@raises(AttributeError)
def surface_area_cuboid_other():
    surface_area_cuboid(None, 3, 4) or surface_area_cuboid(2, None, 4) or surface_area_cuboid(2, 3, None)

@raises(TypeError)
def area_parallelogram_other():
    area_parallelogram("a string", 4) or area_parallelogram(3, "a string")

@raises(ValueError)
def area_parallelogram_other():
    area_parallelogram(-3, 4) or area_parallelogram(3, -4)

@raises(AttributeError)
def arae_parallelogram_other():
    area_parallelogram(None, 4) or area_parallelogram(3, None)

@raises(TypeError)
def volume_cone_other():
    volume_cone("a string")

@raises(ValueError)
def volume_cone_other():
    volume_cone(-7)

@raises(AttributeError)
def volume_cone_other():
    volume_cone(None)

@raises(TypeError)
def volume_right_pyramid_other():
    volume_right_pyramid("a string", 4, 3) or volume_right_pyramid(2, "a string", 3) or \
        volume_right_pyramid(2, 4, "a string")

@raises(ValueError)
def volume_right_pyramid_other():
    volume_right_pyramid(-2, 4, 3) or volume_right_pyramid(2, -4, 3) or volume_right_pyramid(2, 4, -3)
