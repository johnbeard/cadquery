#File: Ex001_Simple_Block
#To use this example file, you need to first follow the "Using CadQuery From Inside FreeCAD"
#instructions here: https://github.com/dcowden/cadquery#installing----using-cadquery-from-inside-freecad

#You run this example by typing the following in the FreeCAD python console, making sure to change
#the path to this example, and the name of the example appropriately.
#import sys
#sys.path.append('/home/user/Downloads/cadquery/examples/FreeCAD')
#import Ex001_Simple_Block

#If you need to reload the part after making a change, you can use the following lines within the FreeCAD console.
#reload(Ex001_Simple_Block)

#You'll need to delete the original shape that was created, and the new shape should be named sequentially (Shape001, etc).

#You can also tie these blocks of code to macros, buttons, and keybindings in FreeCAD for quicker access.
#You can get a more in-depth explantion of this example at http://parametricparts.com/docs/quickstart.html

import cadquery
import Part

#The dimensions of the box. These can be modified rather than changing the box's code directly.
length = 100.0
height = 100.0
thickness = 20.0

#Create a 3D box based 
bb = cadquery.Workplane("XY").box(length, height, thickness)

#Get a cadquery solid object
solid = bb.val()

#Use the wrapped property of a cadquery primitive to get a FreeCAD solid
Part.show(solid.wrapped)

#Would like to zoom to fit the part here, but FreeCAD doesn't seem to have that scripting functionality