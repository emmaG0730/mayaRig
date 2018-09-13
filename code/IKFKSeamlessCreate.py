import maya.cmds as mc


#inputAmount = 
for each in range(5):
	mc.joint( p = (each,0,0))
	mc.joint(n = 'advanced_' + str(each+1) + '_JNT' , e= True,rad = 0.5,oj='xyz',sao  ='yup')
	
#startPosition = (0,0,0)
#endPosition = (0,0,4)

mc.curve(n='advancedCurve1',p = [(0,0,0),(0,0,4)],d =1)
mc.ikHandle( sj='advanced_1_JNT', ee='advanced_5_JNT', c ='advancedCurve1' ,ccv = False,scv = False,
				fj = True,sol = 'ikSplineSolver',tws ="easeIn",roc = True)

mc.spaceLocator(n = 'Start')
mc.move(0,1,0)
mc.spaceLocator(n = 'End')
mc.move(04,1,0)

#mc.move(0,1,0,loc1[0]+".scalePivot",loc1[0]+".rotatePivot")
#mc.move(4,1,0,loc2[0]+".scalePivot",loc2[0]+".rotatePivot")

mc.select('ikHandle1')
mc.setAttr ("ikHandle1.dTwistControlEnable" ,1)
mc.setAttr ("ikHandle1.dWorldUpType", 2)
mc.setAttr ("ikHandle1.dWorldUpObject", 'Start|StartShape')
mc.setAttr ("ikHandle1.dWorldUpObject2", 'End|EndShape')

mc.joint(n = 'joint1Con',p = (0,0,0))
mc.joint(n = 'joint2Con',p = (4,0,0))

mc.parent('Start','joint1Con')
mc.parent('End','joint2Con')

degree = mc.getAttr( 'advancedCurve1.degree' )
span = mc.getAttr( 'advancedCurve1.spans' )
CVAmount = degree + span
for eachCV in range(CVAmount):
	mc.select('advancedCurve1.cv[' + str(eachCV) + ']')
	mc.cluster(en = 1)

