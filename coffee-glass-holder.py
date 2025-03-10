from ocp_vscode import show, show_object, reset_show, set_port, set_defaults, get_defaults
set_port(3939)
from build123d import *

# parameters

hole_diam = 31
hole_depth = 25
holes_in_a_row = 4
row_count = 2
dist_h = 5
dist_v = 1

hole_dist = hole_diam + dist_h
length = holes_in_a_row*hole_dist + dist_h
width = dist_h + row_count * (dist_h + hole_diam)
height = hole_depth + dist_v

# basic box without holes

box = Box(length=length, width=width, height=height)

# select top face plane

plane = Plane( box.faces().sort_by(Axis.Z).last )

sketch = Sketch() + [
    plane * loc * Circle(radius=hole_diam/2.0)
    for loc in GridLocations(hole_dist, hole_dist, holes_in_a_row, row_count)
]

# extrude holes

box -= extrude(sketch, -hole_depth)

# chamfer all edges

box = chamfer(box.edges(), length=0.6)

show_object(box)

# export as STEP

export_step(box, "coffee-glass-holder.step")
