import maya.cmds as mc

class ArmCreation(object):

	def __init__(self):
		self.ArmWin = 'AdvancedArmCreation'
		self.title =  'ArmTwist'
		self.size = (300,100)			
		
	def printOut(self, *args, **kwargs):
		jointAmounts = mc.intSliderGrp(self.slider,q=1,v=1)
		return jointAmounts
		
	def createUI(self):			
		if mc.window(self.ArmWin,q=True,exists = True):
			mc.deleteUI(self.ArmWin)
		self.win = mc.window(self.ArmWin, t = self.title,wh =self.size,s = False,resizeToFitChildren = True)
		self.layout = mc.columnLayout(adj = True)		
		self.slider = mc.intSliderGrp(l = 'JointAmount',min= 1,max = 10,field= True)
		mc.button(label='GenerateArm',c =self.printOut)	
		#amount = self.printOut()
		#print amount
		mc.showWindow(self.win)	

		
a= ArmCreation()
a. createUI()
