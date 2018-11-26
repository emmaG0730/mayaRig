import maya.cmds as mc
from joint_class import Joint 

class JointChain(Joint):
	
	def __init__(self,name,**kwargs):
		
		Joint.__init__(self,name)
		
		kwargs['name'] = name
		kwargs['absolute'] = True
		parts = mc.joint(**kwargs)
		self.name = parts
		
	def set_joint_chain(self,nums,ik_type):
		joint_pos = [0,0,0]
		mc.select(clear = True)
		start_joint = mc.joint(n = self.name +'_JNT_0',p = joint_pos, rad = 0.4)		
		print start_joint
		for i in range(1,nums + 1):			
			mc.joint(n = self.name + '_JNT_' + str(i),p = (joint_pos[0],joint_pos[1] + i * 3,joint_pos[2]), rad = 0.4)
			mc.joint(self.name + '_JNT_' + str(i - 1),e= True, zso = True,oj='xyz',sao  ='yup',roo = 'zxy')
		#start_joint = self.name + '0'
		end_joint = self.name + '_JNT_' + str(nums)
		ikhandle_type = 'ik' + ik_type + 'solver'
		mc.ikHandle( sj = start_joint, ee = end_joint,sol = ikhandle_type)
		