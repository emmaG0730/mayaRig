import maya.cmds as mc
from joint_class import Joint 

class JointChain(Joint):
	
	def __init__(self,name = 'joint'):
		Joint.__init__(self)
		parts = mc.joint(name = name,r = 1.0)
		self.name = parts[0]
	
	def set_position(pos):#pos = list()
		self.joint_pos_list = pos
	
