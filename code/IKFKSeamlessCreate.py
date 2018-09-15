import maya.cmds as mc
#import functools

def createUI():	
	ArmWin = 'AdvancedArmCreation'
	if mc.window(ArmWin,q=True,exists = True):
		mc.deleteUI(ArmWin)
	win = mc.window(ArmWin,t = 'ArmTwist',wh =(300,100),s = False,resizeToFitChildren = True)
	mc.rowColumnLayout(numberOfColumns =2,cw = [(1,100),(2,200)],columnOffset=[(1,'right',10)])
	mc.text( label='JointAmount' )
	inputValue = mc.intField(value= True)
	mc.button( label='GenerateArm', c = armGeneration)	
	mc.showWindow(win)
createUI()

#inputAmount = 
def armGeneration(inputValue):
	#input = mc.intField(inputValue,q= True,value= True)
	#print input
	for each in range(5):
		mc.joint( p = (each,0,0))
		mc.joint( n = 'advanced_' + str(each+1) + '_JNT' , e= True,rad = 0.5,oj='xyz',sao  ='yup')
		

	mc.curve(n='advancedCurve1',p = [(0,0,0),(4,0,0)],d =1)
	mc.ikHandle( sj='advanced_1_JNT', ee='advanced_5_JNT', c ='advancedCurve1' , p=2, w=.5,ccv = False,scv = False,
					sol = 'ikSplineSolver',tws ="Linaer",roc = True,pcv=False)
	
	mc.spaceLocator(n = 'Start')
	mc.move(0,1,0)
	mc.spaceLocator(n = 'End')
	mc.move(4,1,0)
	
	mc.select('ikHandle1')
	mc.setAttr ("ikHandle1.dTwistControlEnable" ,1)
	mc.setAttr ("ikHandle1.dWorldUpType", 2)
	mc.connectAttr ('Start.xformMatrix', 'ikHandle1.dWorldUpMatrix')
	mc.connectAttr ('End.xformMatrix' ,'ikHandle1.dWorldUpMatrixEnd')

	mc.joint(n = 'joint1Con',p = (0,0,0))
	mc.joint(n = 'joint2Con',p = (4,0,0))
	
	#create cluster
	degree = mc.getAttr( 'advancedCurve1.degree' )
	span = mc.getAttr( 'advancedCurve1.spans' )
	CVAmount = degree + span
	for eachCV in range(CVAmount):
		mc.select('advancedCurve1.cv[' + str(eachCV) + ']')
		mc.cluster(en = 1)
	
	mc.parent('Start','joint1Con')
	mc.parent('End','joint2Con')
	mc.parentConstraint('joint1Con','cluster1Handle')
	mc.parentConstraint('joint2Con','cluster2Handle')

createUI()

