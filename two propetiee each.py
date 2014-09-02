__author__ = 'sandile'
from pylab import *

from geo_formulae import *

# make functions able to operate on vectors
v_triangle_area = np.vectorize(triangle_area)
v_circumference = np.vectorize(circumference)
v_volume_sphere = np.vectorize(volume_sphere)
v_area_circle = np.vectorize(area_circle)
v_volume_cylinder = np.vectorize(volume_cylinder)
v_arc_length = np.vectorize(arc_length)
v_volume_cuboid = np.vectorize(volume_cuboid)
v_surface_area_cuboid = np.vectorize(surface_area_cuboid)
v_area_parallelogram = np.vectorize(area_parallelogram)
v_volume_cone = np.vectorize(volume_cone)

def triangle_area_plot_props(start, end):
    """
    Plot the area of a triangle by varying the base length, with base side from start to end,
    the height is kept constant at 4
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
    """
    height = 4
    S = np.linspace(start, end)  # our side lengths
    A = v_triangle_area(S, height)  # the areas
    plot(S, A, '-r', label="Area")
    xlabel('side length')
    ylabel('geo values')
    title('Square Geo Properties')
    legend(loc='upper right')
    show()
    pass

if __name__ == "__main__":
    triangle_area_plot_props(0, 10)




def circumference_plot_props(start, end):
    """
    Plot the distance around a circle by varying the radius length, with radius from start to end.
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
    """
    S = np.linspace(start, end)  # the radius length
    A = v_circumference(S)  # the distances around
    plot(S, A, '-r', label="circumference")
    xlabel('radius length')
    ylabel('geo values')
    title('circumference Geo Properties')
    legend(loc='upper right')
    show()
    pass

if __name__ == "__main__":
    circumference_plot_props(0,10)


def volume_sphere_plot_props(start, end):
    """
    Plot the volume of a sphere by varying the radius, with radius from start to end.
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
    """
    S = np.linspace(start, end)  # our side lengths
    A = v_volume_sphere(S)  # the volume of the ephere
    plot(S, A, '-r', label="volume of sphere")
    xlabel('radius length')
    ylabel('geo values')
    title('volume_sphere Geo Properties')
    legend(loc='upper right')
    show()
    pass

if __name__ == "__main__":
    volume_sphere_plot_props(0, 10)


def area_circle_plot_props(start, end):
    """
    Plot the area of a circle by varying the radius length, with radius from start to end.
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
    """
    S = np.linspace(start, end)  # the radius of the circle
    A = v_area_circle(S)  # the areas
    plot(S, A, '-b', label="Area")
    xlabel('radius length')
    ylabel('geo values')
    title('circle_area Geo Properties')
    legend(loc='upper right')
    show()
    pass

if __name__ == "__main__":
    area_circle_plot_props(0, 10)

def volume_cylinder_plot_props(start, end):
    """
    Plot the volume of a cylinder by varying the radius length, with radius from start to end,
    the height is kept constant at 8
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
    """
    height = 8
    S = np.linspace(start, end)  # the radius of the circular part of the cylinder.
    A = v_volume_cylinder(S, height)  # the volumes
    plot(S, A, '-b', label="volume")
    xlabel('radius length')
    ylabel('geo values')
    title('volume_cylinder Geo Properties')
    legend(loc='upper right')
    show()
    pass

if __name__ == "__main__":
    volume_cylinder_plot_props(0, 10)

def arc_length_plot_props(start, end):
    """
    Plot the arc length of an arc by varying the radius, with the radius from start to end.
    in this particular case we fix the angle at 90 degrees
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
    """
    S = np.linspace(start, end)  # the length of the radius
    A = v_arc_length(S,90)  # the arc length
    plot(S, A, '-g', label="arc_length")
    xlabel('radius length')
    ylabel('geo values')
    title('arc length Geo Properties')
    legend(loc='upper right')
    show()
    pass

if __name__ == "__main__":
    arc_length_plot_props(0, 10)

def volume_cuboid_plot_props(start, end):
    """
    Plot the volume of a cuboid by varying the base length, with base side from start to end,
    the height and breath is kept constant at 4 and 8 respectively
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
    """
    S = np.linspace(start, end)  # our side lengths
    A = v_volume_cuboid(S, 4, 8)  # the areas
    plot(S, A, '-r', label="volume of cuboid")
    xlabel('side length')
    ylabel('geo values')
    title('volume_cuboid Geo Properties')
    legend(loc='upper right')
    show()
    pass

if __name__ == "__main__":
    volume_cuboid_plot_props(0, 10)

def surface_area_cuboid_plot_props(start, end):
    """
    Plot the surface area of a cuboid by varying the base length, with base side from start to end,
    the height and breath is kept constant at 4 and 8 respectively.
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
    """
    height = 4
    breath = 8
    S = np.linspace(start, end)  # our side lengths
    A = v_surface_area_cuboid(S, height, breath)  # the surface areas
    plot(S, A, '-r', label="surface_area_cuboid")
    xlabel('side length')
    ylabel('geo values')
    title('surface area of cuboid Geo Properties')
    legend(loc='upper right')
    show()
    pass

if __name__ == "__main__":
    surface_area_cuboid_plot_props(0, 10)



def area_parallelogram_plot_props(start, end):
    """
    Plot the surface area of a parallelogram by varying the base length, with base side from start to end,
    the height is kept constant at 4
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
    """
    height = 4
    S = np.linspace(start, end)  # our side lengths
    A = v_area_parallelogram(S, height)  # the surface areas
    plot(S, A, '-r', label="surface_area_parallelogram")
    xlabel('side length')
    ylabel('geo values')
    title('surface area of a parallelogram Geo Properties')
    legend(loc='upper right')
    show()
    pass

if __name__ == "__main__":
    area_parallelogram_plot_props(0, 10)



def volume_cone_plot_props(start, end):
    """
    Plot the volume of a cone by varying the height, with height from start to end,
    the radius is kept constant at 6
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
    """
    radius = 6
    S = np.linspace(start, end)  # our side lengths
    A = v_volume_cone(S,radius)  # the surface areas
    plot(S, A, '-r', label="volume_cone")
    xlabel('height length')
    ylabel('geo values')
    title('volume cone Geo Properties')
    legend(loc='upper right')
    show()
    pass

if __name__ == "__main__":
    volume_cone_plot_props(0, 10)
