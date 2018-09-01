# -*- coding: utf-8 -*-
"""
Script for drawing a 3D lens in blender
"""

import bpy


# Define radius1, radius2, center thickness (ct), and semi-aperture
r1 = 3
r2 = 2
ct = .5
semi_aper = .8


#calclulate sphere center separation to get the correct ct
separation = r1 + r2 - ct 
        
#add first sphere
bpy.ops.mesh.primitive_uv_sphere_add(size=r1,location=(0,0,0))
sphere1 = bpy.context.active_object  #most recently added object is current
bpy.context.active_object.name = 'sphere1'

#add second sphere
bpy.ops.mesh.primitive_uv_sphere_add(size=r2, location = (0,0,separation))
sphere2 = bpy.context.active_object
bpy.context.active_object.name = 'sphere2'

#CSG Intersect - Sphere1 and Sphere 2
mod1 = sphere1.modifiers.new('CSG1','BOOLEAN')
mod1.show_in_editmode = False
mod1.object = sphere2
mod1.operation = 'INTERSECT'

bpy.context.scene.objects.active = sphere1
bpy.ops.object.modifier_apply(apply_as='DATA',modifier='CSG1')

#bpy.ops.object.delete()


#add a cylinder.  Ct*1.1 for padding
bpy.ops.mesh.primitive_cylinder_add(radius=semi_aper,depth=ct*1.1,location=(0,0,r1-(ct/2)))
cyl = bpy.context.active_object
bpy.context.active_object.name = 'cyl'

mod2 = cyl.modifiers.new('CSG2','BOOLEAN')
mod2.show_in_editmode = False
mod2.object = sphere1
mod2.operation = 'INTERSECT'

bpy.context.scene.objects.active = cyl
bpy.ops.object.modifier_apply(apply_as='DATA',modifier='CSG2')

bpy.data.objects['sphere1'].select = True
bpy.data.objects['sphere2'].select = True
bpy.data.objects['cyl'].select = False
#bpy.context.scene.objects.active =  #doesn't work
bpy.ops.object.delete()








        