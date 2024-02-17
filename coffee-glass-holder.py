from ocp_vscode import show, show_object, reset_show, set_port, set_defaults, get_defaults
set_port(3939)
from build123d import *

# parameters

hole_diam = 31
hole_depth = 25
holes_in_a_row = 6
row_count = 2
dist_h = 5
dist_v = 1

hole_dist = hole_diam + dist_h
length = holes_in_a_row*hole_dist + dist_h
width = dist_h + row_count * (dist_h + hole_diam)
height = hole_depth + dist_v

with BuildPart() as holder:
    # basic holder without holes
    Box(length=length, width=width, height=height)
    # select top face plane
    top_face = holder.faces().sort_by(Axis.Z).last
    with BuildSketch(top_face) as holes_sketch:
        with GridLocations(hole_dist, hole_dist, holes_in_a_row, row_count) as loc:
            Circle(radius=hole_diam/2.0)
    extrude(amount=-hole_depth, mode=Mode.SUBTRACT)
    fillet(holder.edges().filter_by(Axis.Z), 5.0)
    chamfer(holder.edges().group_by(Axis.Z)[-1], 1.0)
    chamfer(holder.edges().group_by(Axis.Z)[0], 1.0)

show_object(holder)

# export as STEP

holder.part.export_step("coffee-glass-holder.step")
