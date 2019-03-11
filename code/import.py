import maya.cmds as mc
import os
import json

uiFile = 'R:\JX4_SourceData\Animation\Characters\MaleAdult_maya\Json_pose\Paste.ui'
windowID = 'PasteWindow'

if mc.window(windowID, exists = True):
	mc.deleteUI(windowID)
win = mc.loadUI(f = uiFile )
mc.showWindow(win)
	
def click_button():
	"""Function to execute when Create button is pressed"""
	json_file_name = mc.textField('lineEdit',q=True, text=True)
	json_file = "R:\\JX4_SourceData\Animation\Characters\MaleAdult_maya\Json_pose\\" + json_file_name + '.json'
	with open(json_file) as jf:
		controller_data = json.load(jf)		
	
	print controller_data				
	all_controllers =  mc.ls(type = "transform")
	for ctrl_current in all_controllers:
	    if 'CTRL' in ctrl_current:
	        for key,value in controller_data[ctrl_current].items():
	            print key,value
	            mc.setAttr(ctrl_current + '.' + key ,value)