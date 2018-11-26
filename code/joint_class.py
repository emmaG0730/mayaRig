import maya.cmds as mc

class Joint(object):
	
	def __init__(self,name = 'joint'):
		self.name = name
		
	def set_name(self,name):
		if name:
			self.name = mc.rename(self.name , name)
			
	def get_translation(self):
		return mc.xform(self.name,q = True,t = True)
		
	def set_translation(self,x = None,y = None,z = None):
		for name in ('x','y','z'):
			val = locals()[name]
			if val is not None:
				opts = {name:True,'objectSpace':True,'obsolute':True}
				mc.move(val,self.name,**opts)
	
	