import maya.cmds as mc

class Joint(object):
	def __init__(self,name):
		self.name = name
		
	def set_name(self,name):
		if name:
			self.name = mc.rename(self.name , name)
			
	def get_translation(self):
		return mc.xform(self.name,ws = True,q = True,t = True)
		 
	def set_translation(self,x = None,y = None,z = None):
		for name in ('x','y','z'):
			val = locals()[name]
			if val is not None:
				opts = {name:True,'objectSpace':True,'absolute':True}
				mc.move(val,self.name,**opts)
	
	def get_rotation(self):
		return mc.xform(self.name,ws = True,q = True,ro = True)
		
	def set_rotation(self,x = None,y = None,z = None):
		for name in ('x','y','z'):
			val = locals()[name]
			if val is not None:
				opts = {name:True,'objectSpace':True,'absolute':True}
				mc.rotate(val,self.name,**opts)
				
	def get_scale(self):
		return mc.xform(self.name,ws = True,q = True,scale = True)
		
	def set_rotation(self,x = None,y = None,z = None):
		for name in ('x','y','z'):
			val = locals()[name]
			if val is not None:
				opts = {name:True,'objectSpace':True,'absolute':True}
				mc.scale(val,self.name,**opts)
