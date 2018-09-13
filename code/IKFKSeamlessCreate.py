import maya.cmds as mc
import functools

def createUI(armGeneration):	
	ArmWin = 'AdvancedArmCreation'
	if mc.window(ArmWin,q=True,exists = True):
		mc.deleteUI(ArmWin)
	win = mc.window(ArmWin,t = 'ArmTwist',wh =(1000,500))
	mc.columnLayout( adjustableColumn=True )
	inputValue = mc.intField(value= True)
	mc.button( label='GenerateArm', c = functools.partial(armGeneration,inputValue))
	mc.text( label='JointAmount' )
	mc.showWindow(win)



#inputAmount = 
def armGeneration(inputValue):
	input = mc.intField(inputValue,q= True,value= True)
	print input
	for each in range(input):
		mc.joint( p = (each,0,0))
		mc.joint(n = 'advanced_' + str(each+1) + '_JNT' , e= True,rad = 0.5,oj='xyz',sao  ='yup')
		
	#startPosition = (0,0,0)
	#endPosition = (0,0,4)
	
	mc.curve(n='advancedCurve1',p = [(0,0,0),(0,0,input-1)],d =1)
	mc.ikHandle( sj='advanced_1_JNT', ee='advanced_5_JNT', c ='advancedCurve1' ,ccv = False,scv = False,
					fj = True,sol = 'ikSplineSolver',tws ="easeIn",roc = True)
	
	mc.spaceLocator(n = 'Start')
	mc.move(0,1,0)
	mc.spaceLocator(n = 'End')
	mc.move(input-1,1,0)
	
	mc.select('ikHandle1')
	mc.setAttr ("ikHandle1.dTwistControlEnable" ,1)
	mc.setAttr ("ikHandle1.dWorldUpType", 2)
	#mc.setAttr ("ikHandle1.dWorldUpObject", 'Start|StartShape')
	#mc.setAttr ("ikHandle1.dWorldUpObject2", 'End|EndShape')
	
	mc.joint(n = 'joint1Con',p = (0,0,0))
	mc.joint(n = 'joint2Con',p = (input-1,0,0))
	
	degree = mc.getAttr( 'advancedCurve1.degree' )
	span = mc.getAttr( 'advancedCurve1.spans' )
	CVAmount = degree + span
	for eachCV in range(CVAmount):
		mc.select('advancedCurve1.cv[' + str(eachCV) + ']')
		mc.cluster(en = 1)
	
	mc.parent('Start','cluster1Handle','joint1Con')
	mc.parent('End','cluster'+str(CVAmount)+'Handle','joint2Con')

createUI(armGeneration)

