import json
import maya.cmds  as mc

with open('controller_data.json') as jf:
	controller_data = json.load(jf)
#print controller_data

		
all_controllers =  mc.ls(type = "transform")
for ctrl_current in all_controllers:
	if 'CTRL' in ctrl_current:
		print controller_data[ctrl_current]
		for key,value in controller_data[ctrl_current].items():
			print key,value
			mc.setAttr(ctrl_current + '.' + key ,value)
		
		#mc.setAttr(ctrl_current_scene + '.inheritsTransform', 0)
		#mc.xform(ctrl_current_scene,t=(controller_data[ctrl_current_scene][0],controller_data[ctrl_current_scene][1],controller_data[ctrl_current_scene][2]))	