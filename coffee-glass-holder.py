from ocp_vscode import show, show_object, reset_show, set_port, set_defaults, get_defaults
set_port(3939)
from build123d import *


hole_diam = 31
hole_depth = 25
num_per_row = 6
num_of_rows = 2
dist_h = 5
dist_v = 1

length = num_per_row*(hole_diam + dist_h) + dist_h
width = dist_h + num_of_rows * (dist_h + hole_diam)
height = hole_depth + dist_v


box = Box(length=length, width=width, height=height, align=Align.MIN)

plane = Plane( box.faces().sort_by(Axis.Z).last )

sketch = Sketch() + [
    plane * loc * Circle(radius=hole_diam/2.0)
    for loc in GridLocations(hole_diam + dist_h, hole_diam + dist_h, num_per_row, num_of_rows)
]

box -= extrude(sketch, -hole_depth)

chw = 0.6
box = chamfer(box.edges().group_by(Axis.Z)[-1], length=chw)
box = chamfer(box.edges().group_by(Axis.Z)[0], length=chw)
box = chamfer(box.edges().filter_by(Axis.Z), length=chw)

show_object(box)

box .export_step("box.step")
