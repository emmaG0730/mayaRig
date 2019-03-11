import maya.cmds as mc
from joint_class import Joint 

class JointChain(Joint):
	
	def __init__(self,name,**kwargs):
		
		Joint.__init__(self,name)
		
		kwargs['name'] = name
		kwargs['absolute'] = True
		parts = mc.joint(**kwargs)
		self.name = parts
		
	def create_joint_chain(self,nums,ik_type):
		'''
		This function create only one joint chain used to be IKFK and Skinned joints
		''' 
		joint_pos = [0,0,0]
		mc.select(clear = True)
		start_joint = mc.joint(n = self.name +'_JNT_0',p = joint_pos, rad = 0.4)		
		print start_joint
		for i in range(1,nums + 1):			
			mc.joint(n = self.name + '_JNT_' + str(i),p = (joint_pos[0],joint_pos[1] + i * 3,joint_pos[2]), rad = 0.4)
			mc.joint(self.name + '_JNT_' + str(i - 1),e= True, zso = True,oj='xyz',sao  ='yup',roo = 'zxy')

		end_joint = self.name + '_JNT_' + str(nums)
		ikhandle_type = 'ik' + ik_type + 'solver'
		mc.ikHandle( sj = start_joint, ee = end_joint,sol = ikhandle_type)
		
	def create_cluster(self):
		'''
		For joint chain which use spline Ik ,like character spine
		'''
		pass
		
	def skin_cluster(self):
		'''
		Cluster skinned on control joint
		'''
		pass
		
	def joint_stretch(self):
		'''
		Stretch the joint chain
		'''
		pass
	
	def elbow_lock(self):
		'''
		Lock elbow or knee
		'''
		pass
		
class Controller():
	def __init__(self,size,shape):
		self._size = size
		
		
	def create_controller(self,body_part):
		'''
		Create controllers for the whole body part 
		'''
		pass
		
	def add_attribute(self,controller_name,attr_name,attr_type):
		'''
		Add attributes on customezed controllers
		'''
		pass
	
	def change_color(self,color_name):
		'''
		Change Whole body part controller color,use string
		'''
		pass
	
		 
		