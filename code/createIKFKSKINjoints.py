import maya.cmds as mc

mc.select( all=True )
mc.delete()

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

mc.select('ikHandle1')
mc.setAttr ("ikHandle1.dTwistControlEnable" ,1)
mc.setAttr ("ikHandle1.dWorldUpType", 2)
mc.connectAttr ('Start.xformMatrix', 'ikHandle1.dWorldUpMatrix')
mc.connectAttr ('End.xformMatrix' ,'ikHandle1.dWorldUpMatrixEnd')

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
mc.arclen(curveName,ch = True)
for each in range(5):		
	mc.expression(o='advanced_' + str(each+1) + '_JNT',s = 'scaleX=curveInfo1.arcLength/4')

#create IK FK SKIN joints
mc.select( clear=True )		
shouder_FK = mc.joint(n = 'shoulder_FK_JNT')
mc.joint(shouder_FK,e = True,p = (0,0,5), rad = 0.5,oj='xyz',sao  ='yup')
elbow_FK = mc.joint(n = 'elbow_FK_JNT')
mc.joint(elbow_FK,e = True,p = (4,0,5), rad = 0.5,oj='xyz',sao  ='yup')
wrist_FK = mc.joint(n = 'wrist_FK_JNT')
mc.joint(wrist_FK,e = True,p = (8,0,5), rad = 0.5,oj='xyz',sao  ='yup')
mc.select(shouder_FK,elbow_FK,wrist_FK)
mc.createDisplayLayer(noRecurse=True,n = 'FK_Layer')
mc.setAttr('FK_Layer.color', 13)

mc.select( clear=True )
shouder_IK = mc.joint(n = 'shoulder_IK_JNT')
mc.joint(shouder_IK,p = (0,0,5),e =True, rad = 0.5,oj='xyz',sao  ='yup')
elbow_IK = mc.joint(n = 'elbow_IK_JNT')
mc.joint(elbow_IK,p = (4,0,5),e =True,rad = 0.5,oj='xyz',sao  ='yup')
wrist_IK = mc.joint(n = 'wrist_IK_JNT')
mc.joint(wrist_IK,p = (8,0,5),e =True, rad = 0.5,oj='xyz',sao  ='yup')
mc.rotate(0,'-30deg',0,'elbow_IK_JNT')
mc.select(elbow_IK)
mc.joint(e= True,spa = True,ch = True)
mc.ikHandle( sj='shoulder_IK_JNT', ee='wrist_IK_JNT',sol = 'ikRPsolver')
mc.rename('ikHandle1','ArmIKhandle')
mc.rotate(0,0,0,'elbow_IK_JNT')
mc.select(shouder_IK,elbow_IK,wrist_IK)
mc.createDisplayLayer(noRecurse=True,n = 'IK_Layer')
mc.setAttr('IK_Layer.color', 6)

mc.select(clear=True)
shouder_SKIN = mc.joint(n = 'shoulder_SKIN_JNT')
mc.joint(shouder_SKIN,e = True,p = (0,0,5), rad = 0.5,oj='xyz',sao  ='yup')
elbow_SKIN = mc.joint(n = 'elbow_SKIN_JNT',p = (4,0,0), rad = 0.5,oj='xyz',sao  ='yup')
mc.joint(elbow_SKIN,e = True,p = (4,0,5), rad = 0.5,oj='xyz',sao  ='yup')
wrist_SKIN = mc.joint(n = 'wrist_SKIN_JNT',p = (8,0,0), rad = 0.5,oj='xyz',sao  ='yup')
mc.joint(wrist_SKIN,e = True,p = (8,0,5), rad = 0.5,oj='xyz',sao  ='yup')
mc.select(shouder_SKIN,elbow_SKIN,wrist_SKIN)
mc.createDisplayLayer(noRecurse=True,n = 'SKIN_Layer')

mc.parentConstraint('shoulder_FK_JNT','shoulder_IK_JNT', 'shoulder_SKIN_JNT')
mc.parentConstraint('elbow_FK_JNT','elbow_IK_JNT','elbow_SKIN_JNT')
mc.parentConstraint('wrist_FK_JNT','wrist_IK_JNT','wrist_SKIN_JNT')

#attach advaneced twist to base arm joints and constraint
mc.select(shouder_SKIN)
shouderSkinTransform = mc.xform(q=True,ws=True,t=True)
twistJNT_S = mc.select('joint1Con')
mc.xform(ws=True,t=(shouderSkinTransform[0],shouderSkinTransform[1],shouderSkinTransform[2]))
mc.parentConstraint(shouder_SKIN,'joint1Con')


mc.select(elbow_SKIN)
elbowSkinTransform = mc.xform(q=True,ws=True,t=True)
mc.select('joint2Con')
mc.xform(ws=True,t=(elbowSkinTransform[0],elbowSkinTransform[1],elbowSkinTransform[2]))
mc.parentConstraint(elbow_SKIN,'joint2Con')

#create FK controller and constraint
for i in ('shoulder','elbow','wrist'):
	mc.circle(n = 'FK_' + i +'_CON',c = (0,0,0),r =1)
	mc.group('FK_'+ i +'_CON',name ='FK_'+ i +'_CON_grp' )
	mc.parentConstraint(i + '_FK_JNT','FK_'+ i +'_CON_grp',mo = False)
	mc.setAttr('FK_' + i + '_CON.rotateY', 90)
	mc.makeIdentity('FK_' + i + '_CON',apply = True)
	mc.delete('FK_' + i + '_CON_grp_parentConstraint1')
	mc.parentConstraint('FK_' + i + '_CON',i + '_FK_JNT')
mc.parent('FK_wrist_CON_grp','FK_elbow_CON')
mc.parent('FK_elbow_CON_grp','FK_shoulder_CON')
	
#import IK controller
mc.file('F:\\GitHub\\tools\\mayaRig\\squreAndCubeIcon.ma',i = True)
mc.select('FK_wrist_CON')
FKWristCON = mc.xform(q=True,ws=True,t=True)
mc.select('controller')
mc.rename('controller','IK_Wrist_CON')
mc.group('IK_Wrist_CON',n = 'IK_Wrist_CON_grp')
#mc.makeIdentity('IK_Wrist_CON',apply = True)
mc.xform(ws=True,t=(FKWristCON[0],FKWristCON[1],FKWristCON[2]))
mc.parent('ArmIKhandle','IK_Wrist_CON')








		