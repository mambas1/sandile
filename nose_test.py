__author__ = 'sandile'
from geo_formulae import *
from nose.tools import *

eps = 1e-6
def test_triangle_area_float():
    assert 12 - eps < triangle_area(6, 4) < 12 + eps

@raises(TypeError)
def triangle_area_other():
    triangle_area("a string")

eps = 1e-6
def test_circumference_float():
    assert 44 - eps < circumference(7) < 44 + eps

@raises(TypeError)
def circumference_other():
    triangle_area("a string")

eps = 1e-6
def test_area_circle_int():
    assert 154 - eps < area_circle(7) < 154 + eps

@raises(TypeError)
def area_circle_other():
    area_circle("a string")

eps = 1e-6
def test_volume_cylinder_float():
    assert 308 - eps < volume_cylinder(7,2) < 308 + eps

@raises(TypeError)
def volume_cylinder_other():
    volume_cylinder("a string")


eps = 1e-6
def test_arc_length_float():
    assert 11 - eps < arc_length(7, 90) < 11 + eps

@raises(TypeError)
def arc_length_other():
    arc_length("a string")


eps = 1e-6
def test_volume_cuboid_float():
    assert 24 - eps < volume_cuboid(2, 3, 4) < 24 + eps

@raises(TypeError)
def volume_cuboid_other():
    volume_cuboid("a string")


eps = 1e-6
def test_surface_area_cuboid_float():
    assert 52 - eps < surface_area_cuboid(2, 3, 4) < 52 + eps

@raises(TypeError)
def surface_area_cuboid_other():
    surface_area_cuboid("a string")


eps = 1e-6
def area_parallelogram_float():
    assert 6 - eps < area_parallelogram(2, 3) < 6 + eps

@raises(TypeError)
def area_parallelogram_other():
    area_parallelogram("a string")


eps = 1e-6
def test_volume_cone_float():
    assert 154 - eps < volume_cone(7, 3) < 154 + eps

@raises(TypeError)
def volume_cone_other():
    volume_cone("a string")


eps = 1e-6
def test_volume_right_pyramid_float():
    assert 8 - eps < volume_right_pyramid(2, 3, 4) < 8 + eps

@raises(TypeError)
def volume_right_pyramid_other():
    volume_right_pyramid("a string")