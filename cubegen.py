import bpy
from bpy import context
from math import sin, cos, radians

testobj = bpy.ops.mesh.primitive_cube_add

#Get the cursor location in the scenes
cursor = context.scene.cursor_location

#Increase the radial distance the cube through the loop
radialdist = 6.0

#initilize variables
xsize = 1.0
ysize = 1.0
zsize = 1.0
theta = 0.0
twopi_over_8 = 6.28 / 8.0

while theta < 6.28:
        x = cursor.x + radialdist * cos(theta)
        y = cursor.y + radialdist * sin(theta)
        z = cursor.z
        testobj(location=(x, y, z))
        
        #resizes gen obj
        bpy.ops.transform.resize(value = (3.2, 3.1, 3.1))

#Increment the radian angle of measure
        theta += twopi_over_8

# py script will gen 8 cubes with its origins on every 45th angle of an unit circle 

# start the drawing angle back at the center for each arm
theta = 0.0

# start the radial distance back at the center for each arm
radialdist = 1.0