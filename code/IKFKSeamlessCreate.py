import maya.cmds as mc

class ArmCreation(object):
	
	def __init__(self,jointAmounts):
		self.ArmWin = 'AdvancedArmCreation'
		self.title =  'ArmTwist'
		self.jointAmounts = jointAmounts
		self.slider = mc.intSliderGrp(l = 'JointAmount',min= 1,max = 10,field= True)
		
	def createUI(self):	
		
		if mc.window(ArmWin,q=True,exists = True):
			mc.deleteUI(ArmWin)
		win = mc.window(self.ArmWin, t = self.title,wh =(300,100),s = False,resizeToFitChildren = True)
		mc.columnLayout(adj = True)
		#num = mc.intSliderGrp(l = 'JointAmount',min= 1,max = 10,field= True)			
		def printOut():
			jointAmounts = mc.intSliderGrp(self.slider,q= True,v=True)
			print jointAmounts
		mc.button(label='GenerateArm', c = 'printOut()')	
		mc.showWindow(win)	
		
	'''def printOut():
		jointAmounts= mc.intSliderGrp(num,q= True,v=True)
		print jointAmounts'''
				
	def armGeneration(self,jointAmounts):
		curveName = 'advancedCurve1'
		for each in range(jointAmounts):
			mc.joint( p = (each,0,0))
			mc.joint( n = 'advanced_' + str(each+1) + '_JNT' , e= True,rad = 0.5,oj='xyz',sao  ='yup')
		mc.curve(n=curveName,p = [(0,0,0),(jointAmounts-1,0,0)],d =1)
		mc.ikHandle( sj='advanced_1_JNT', ee='advanced_'+jointAmounts+'_JNT', c ='advancedCurve1' , p=2, w=.5,ccv = False,scv = False,
						sol = 'ikSplineSolver',tws ="Linear",roc = True,pcv=False)
		
		start = mc.spaceLocator(n = 'Start')
		mc.move(0, 1, 0)
		end = mc.spaceLocator(n = 'End')
		mc.move(jointAmounts-1, 1, 0)
	
		mc.select('ikHandle1')
		mc.setAttr ("ikHandle1.dTwistControlEnable" ,1)
		mc.setAttr ("ikHandle1.dWorldUpType", 2)
		mc.connectAttr ('Start.xformMatrix', 'ikHandle1.dWorldUpMatrix')
		mc.connectAttr ('End.xformMatrix' ,'ikHandle1.dWorldUpMatrixEnd')
		
		mc.select( clear=True )
		mc.joint(n = 'joint1Con',p = (0,0,0))
		mc.joint(n = 'joint2Con',p = (jointAmounts-1,0,0))
		
		#create cluster
		degree = mc.getAttr( 'advancedCurve1.degree' )
		span = mc.getAttr( 'advancedCurve1.spans' )
		CVAmount = degree + span
		for eachCV in range(CVAmount):
			mc.select('advancedCurve1.cv[' + str(eachCV) + ']')
			mc.cluster(en = 1)
				
		#mc.parentConstraint('joint1Con','Start',mo = True)
		mc.parentConstraint('joint2Con','End',mo = True)
		mc.cycleCheck(e= False)
		mc.parentConstraint('joint1Con','cluster1Handle')
		mc.parentConstraint('joint2Con','cluster2Handle')
		
		#ignore X Axis of Twisting
		mc.select( clear=True )
		mc.joint(n = 'joint1Aim',p = (0,0,0),rad = 0.7)
		mc.parentConstraint('joint1Aim','Start',mo = True)
		mc.connectAttr('joint1Con.rotateZ','joint1Aim.rotateZ')
		mc.connectAttr('joint1Con.rotateY','joint1Aim.rotateY')
		
		#stretch joint
		mc.select(curveName)
		mc.arclen(curveName,ch = True)
		mc.delete( all=True, e=True )
		for each in range(jointAmounts):		
			mc.expression(o='advanced_' + str(each+1) + '_JNT',s = 'scaleX=curveInfo1.arcLength/'+'jointAmounts-1')
a = ArmCreation()
a.createUI()
