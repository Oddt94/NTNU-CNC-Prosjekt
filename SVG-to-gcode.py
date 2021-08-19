from svg_to_gcode.svg_parser import parse_file
from svg_to_gcode.compiler import Compiler, interfaces
from svg_to_gcode import TOLERANCES

TOLERANCES['approximation'] = 0.1

# initializes the g code generator using the idle speed, the work speed and if enabled the z movement
gcode_compiler = Compiler(interfaces.Gcode, movement_speed=1000, cutting_speed=300, pass_depth=0)
curves = parse_file("test3.svg")

gcode_compiler.append_curves(curves)
gcode_compiler.compile_to_file("drawing.gcode", passes=2)