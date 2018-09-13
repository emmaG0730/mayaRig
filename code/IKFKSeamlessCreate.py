import maya.cmds as mc

for each in range(5):
	jj = mc.joint(p = (0,0,each),rad = 0.5,sao = 'yup')
	mc.rename(jj,'advanced_' + str(each+1) + '_JNT')
mc.curve(n='advancedCurve1',p = [(0,0,0),(0,0,4)],d =1)
mc.ikHandle( sj='advanced_1_JNT', ee='advanced_5_JNT', c ='advancedCurve1' ,ccv = False,scv = False,fj = True,sol = 'ikSplineSolver')

mc.spaceLocator(p = (0,1,0))
mc.spaceLocator(p=(0,1,5-1))

mc.joint(p = (0,0,0))
mc.joint(p=(0,0,5-1))

mc.select('ikHandle1')
mc.setAttr ("ikHandle1.dTwistControlEnable" ,1)
mc.setAttr ("ikHandle1.dWorldUpType", 4)
mc.pickWalk( d  = 'down')


degree = mc.getAttr( 'advancedCurve1.degree' )
span = mc.getAttr( 'advancedCurve1.spans' )
CVAmount = degree + span
print CVAmount
for eachCV in range(CVAmount):
	mc.select('advancedCurve1.cv[' + str(eachCV) + ']')
	mc.cluster(en = 1)

