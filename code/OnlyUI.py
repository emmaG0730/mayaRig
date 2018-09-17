import maya.cmds as mc

class ArmCreation(object):
	#jointAmounts = 0
	def __init__(self):
		self.ArmWin = 'AdvancedArmCreation'
		self.title =  'ArmTwist'
		self.size = (300,100)			
		
	def printOut(self):
		self.slider = mc.intSliderGrp(l = 'JointAmount',min= 1,max = 10,field= True)
		self.jointAmounts = mc.intSliderGrp(self.slider,q= True,v=True)
		print self.jointAmounts
		
	def createUI(self):			
		if mc.window(self.ArmWin,q=True,exists = True):
			mc.deleteUI(self.ArmWin)
		self.win = mc.window(self.ArmWin, t = self.title,wh =self.size,s = False,resizeToFitChildren = True)
		self.layout = mc.columnLayout(adj = True)		
		self.slider = mc.intSliderGrp(l = 'JointAmount',min= 1,max = 10,field= True)
		mc.button(label='GenerateArm',c ='printOut()')	
		mc.showWindow()	
		
a= ArmCreation()
a.createUI()
