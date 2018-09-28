import maya.cmds as mc
import os
#mc.select( all=True )
#mc.delete()
class ArmCreation(object):
	use= None
	@classmethod	
	def showUI(cls,uiFile):
		win = cls(uiFile)
		win.create()
		return win
				
	def __init__(self, filePath,*args):
		"""Initialize data attributes"""
		ArmCreation.use = self
		self.window = 'arm'
		self.inputField = 'input'
		self.uiFile = filePath
        
	def create(self, verbose=False):   	
		if mc.window(self.window, exists=True):
		    mc.deleteUI(self.window)
		self.window = mc.loadUI(uiFile=self.uiFile,verbose=verbose)
		mc.showWindow(self.window)
	def createArm():
		print 'A arm!'
win=ArmCreation(os.getcwd(),'arm.ui')
win.create(verbose=False)

print os.getcwd()



















