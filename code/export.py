import maya.cmds as mc
import json

ctrl_attr = {}
attr_value = {}
d3 = {}

controllers =  mc.ls(type = "transform")
for ctrl in controllers:
	if 'CTRL' in ctrl:
		mc.select(ctrl)
		attrs = cmds.listAttr(k=True,u=True)
		#print ctrl
		#print attrs
		ctrl_attr[ctrl] = attrs

		if attrs != None:
			for attr in attrs:
				try:
					value = mc.getAttr(ctrl + '.' + attr)						
					print value
					print attr
					#attr_value[attr] = value
				except:
					pass

						
print ctrl_attr
print attr_value


for key,value in ctrl_attr.items():						
	print ctrl_attr[key]
with open('controller_data.json','w') as outfile:
	json.dump(ctrl_attr,outfile,indent = 4)
	
	
