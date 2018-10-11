import maya.cmds as mc

#create advance twist joints
mc.select( clear=True )
curveName = 'advancedCurve1'
for each in range(5):
	mc.joint( p = (each,0,0))
	mc.joint( n = 'advanced_' + str(each+1) + '_JNT' , e= True,rad = 0.5,oj='xyz',sao  ='yup')
mc.curve(n=curveName,p = [(0,0,0),(5-1,0,0)],d =1)
mc.ikHandle( sj='advanced_1_JNT', ee='advanced_'+str(5)+'_JNT', c ='advancedCurve1' , p=2, w=.5,ccv = False,scv = False,
				sol = 'ikSplineSolver',tws ="Linear",roc = True,pcv=False)
mc.rename('ikHandle1','TwistIKhandle')
start = mc.spaceLocator(n = 'Start')
mc.move(0, 1, 0)
end = mc.spaceLocator(n = 'End')
mc.move(5-1, 1, 0)

mc.select('TwistIKhandle')
mc.setAttr ("TwistIKhandle.dTwistControlEnable" ,1)
mc.setAttr ("TwistIKhandle.dWorldUpType", 2)
mc.connectAttr ('Start.xformMatrix', 'TwistIKhandle.dWorldUpMatrix')
mc.connectAttr ('End.xformMatrix' ,'TwistIKhandle.dWorldUpMatrixEnd')

mc.select( clear=True )
mc.joint(n = 'joint1Con',p = (0,0,0))
mc.joint(n = 'joint2Con',p = (5-1,0,0))

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
mc.parent('joint1Aim','joint1Con')

#stretch joint
mc.select(curveName)
mc.setAttr(curveName + '.inheritsTransform',0)
mc.arclen(curveName,ch = True)
for each in range(5):		
	mc.expression(o='advanced_' + str(each+1) + '_JNT',s = 'scaleX=curveInfo1.arcLength/4')


#group all(
mc.group('advanced_1_JNT','advancedCurve1','TwistIKhandle','Start','End','joint1Con',
			'cluster1Handle','cluster2Handle',n = 'AdvancedTwistGrp')






















		