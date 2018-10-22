import maya.cmds as mc

#create FK controller and constraint
for i in ('Shoulder','Elbow','Wrist'):
	mc.circle(n = 'FK_Left' + i +'_CON',c = (0,0,0),r =1)
	mc.group('FK_Left'+ i +'_CON',name ='FK_Left'+ i +'_CON_grp' )
	mc.parentConstraint(i + 'Left_FK_JNT','FK_Left'+ i +'_CON_grp',mo = False)
	mc.setAttr('FK_Left' + i + '_CON.rotateY', 90)
	mc.makeIdentity('FK_Left' + i + '_CON',apply = True)
	mc.delete('FK_Left' + i + '_CON_grp_parentConstraint1')
	mc.parentConstraint('FK_Left' + i + '_CON',i + 'Left_FK_JNT')
mc.parent('FK_LeftWrist_CON_grp','FK_LeftElbow_CON')
mc.parent('FK_LeftElbow_CON_grp','FK_LeftShoulder_CON')
for j in ('tx','ty','tz','rx','rz','sx','sy','sz'):
	mc.setAttr('FK_LeftElbow_CON.'+j,l = True,k =False)

#create IK controller and IKFK switcher
mc.file('F:\\GitHub\\tools\\mayaRig\\squreAndCubeIcon.ma',i = True)
mc.select('FK_LeftWrist_CON')
FKWristCON_t = mc.xform(q=True,ws=True,t=True)
FKWristCON_r = mc.xform(q=True,ws=True,ro=True)
mc.select('controller')
mc.rename('controller','IK_LeftWrist_CON')
mc.scale(1,0.5,1.2)
mc.group('IK_LeftWrist_CON',n = 'IK_LeftWrist_CON_grp')
mc.xform(ws=True,t=(FKWristCON_t[0],FKWristCON_t[1],FKWristCON_t[2]))
mc.xform(ws=True,ro=(FKWristCON_r[0],FKWristCON_r[1],FKWristCON_r[2]))
mc.parent('ArmIKhandle','IK_LeftWrist_CON') 

mc.file('F:\\GitHub\\tools\\mayaRig\\squreAndCubeIcon.ma',i = True)
mc.select('controller')
mc.rename('controller','IKFKSwitch')
mc.group('IKFKSwitch',n = 'IKFKSwitch_grp')
mc.scale(0.6,0.02,0.6)
mc.xform(ws=True,t=(FKWristCON_t[0],FKWristCON_t[1]+0.5,FKWristCON_t[2]))
mc.xform(ws=True,ro=(FKWristCON_r[0],FKWristCON_r[1]+0.5,FKWristCON_r[2]))
mc.parent('IKFKSwitch_grp','WristLeft_SkinJNT')
mc.select('IKFKSwitch')
mc.addAttr(ln = 'IKFKTrigger',at= 'enum',en = 'IK:FK',k=True)

#create pole/fake pole controller
mc.file('F:\\GitHub\\tools\\mayaRig\\squreAndCubeIcon.ma',i = True)
for each in ('Pole_CON','FakePole_CON'):	
	mc.select('ElbowLeft_FK_JNT')
	FKElbow_t = mc.xform(q=True,ws=True,t=True)
	FKElbow_r = mc.xform(q=True,ws=True,ro=True)
	mc.select('controller')
	mc.duplicate()
	mc.rename('controller1',each)
	mc.group(each,n = each+'_grp')
	mc.scale(0.4,0.4,0.4)
	mc.xform(ws=True,t=(FKElbow_t[0],FKElbow_t[1],FKElbow_t[2]-2))
	mc.xform(ws=True,ro=(FKElbow_r[0],FKElbow_r[1],FKElbow_r[2]-2))
mc.poleVectorConstraint('Pole_CON','ArmIKhandle') 
mc.parent('FakePole_CON_grp','FK_LeftElbow_CON')

################################################################################

triggerState = mc.getAttr("IKFKSwitch.IKFKTrigger")
if triggerState == 1:
	mc.setAttr ("Elbow_SKIN_JNT_parentConstraint1.Elbow_IK_JNTW1" ,0)
	mc.setAttr ("Elbow_SKIN_JNT_parentConstraint1.Elbow_FK_JNTW0" ,1)
	mc.setAttr ("Shoulder_SKIN_JNT_parentConstraint1.Shoulder_IK_JNTW1" ,0)
	mc.setAttr ("Shoulder_SKIN_JNT_parentConstraint1.Shoulder_FK_JNTW0" ,1)	
	mc.setAttr ("Wrist_SKIN_JNT_parentConstraint1.Wrist_IK_JNTW1" ,0)
	mc.setAttr ("Wrist_SKIN_JNT_parentConstraint1.Wrist_FK_JNTW0" ,1)
	'''
	mc.setAttr('FK_Shoulder_CON.visibility',1)
	mc.setAttr('FK_Elbow_CON.visibility',1)
	mc.setAttr('FK_Wrist_CON.visibility',1)
	mc.setAttr('IK_Wrist_CON.visibility',0)
	mc.setAttr('Pole_CON.visibility',0)
	'''
	mc.select('Shoulder_IK_JNT')
	Shoulder_IK_RO = mc.xform(q=True,ws=True,ro=True)
	mc.select('FK_Shoulder_CON')
	mc.xform(ws=True,ro=(Shoulder_IK_RO[0],Shoulder_IK_RO[1],Shoulder_IK_RO[2]))

	mc.select('Elbow_IK_JNT')
	Elbow_IK_RO = mc.xform(q=True,ws=True,ro=True)
	mc.select('FK_Elbow_CON')
	mc.xform(ws=True,ro=(Elbow_IK_RO[0],Elbow_IK_RO[1],Elbow_IK_RO[2]))
    
	mc.select('Wrist_IK_JNT')
	Wrist_IK_RO = mc.xform(q=True,ws=True,ro=True)
	Wrist_IK_T = mc.xform(q=True,ws=True,t=True)
	mc.select('FK_Wrist_CON')
	mc.xform(ws=True,ro=(Wrist_IK_RO[0],Wrist_IK_RO[1],Wrist_IK_RO[2]))
	mc.xform(ws=True,t=(Wrist_IK_T[0],Wrist_IK_T[1],Wrist_IK_T[2]))
    
	mc.select('Pole_CON')
	Pole_CON_T = mc.xform(q=True,ws=True,t=True)
	#Pole_CON_RO = mc.xform(q=True,ws=True,ro=True)
    
	mc.select('fkPole')
	mc.xform(ws=True,t=(Pole_CON_T[0],Pole_CON_T[1],Pole_CON_T[2]))
	#mc.xform(ws=True,ro=(Pole_CON_RO[0],Pole_CON_RO[1],Pole_CON_RO[2]))

	
elif triggerState == 0:
	mc.setAttr ("Elbow_SKIN_JNT_parentConstraint1.Elbow_IK_JNTW1" ,1)
	mc.setAttr ("Elbow_SKIN_JNT_parentConstraint1.Elbow_FK_JNTW0" ,0)
	mc.setAttr ("Shoulder_SKIN_JNT_parentConstraint1.Shoulder_IK_JNTW1" ,1)
	mc.setAttr ("Shoulder_SKIN_JNT_parentConstraint1.Shoulder_FK_JNTW0" ,0)	
	mc.setAttr ("Wrist_SKIN_JNT_parentConstraint1.Wrist_IK_JNTW1" ,1)
	mc.setAttr ("Wrist_SKIN_JNT_parentConstraint1.Wrist_FK_JNTW0" ,0)	
	'''
	mc.setAttr('FK_Shoulder_CON.visibility',0)
	mc.setAttr('FK_Elbow_CON.visibility',0)
	mc.setAttr('FK_Wrist_CON.visibility',0)
	mc.setAttr('IK_Wrist_CON.visibility',1)
	mc.setAttr('Pole_CON.visibility',1)
	'''
	
	mc.select('FK_Wrist_CON')
	FK_WristP= mc.xform(q=True,ws=True,t=True)
	FK_WristRO= mc.xform(q=True,ws=True,ro=True)	
	mc.select('IK_Wrist_CON')
	mc.xform(ws=True,t=(FK_WristP[0],FK_WristP[1],FK_WristP[2]))
	mc.xform(ws=True,ro=(FK_WristRO[0],FK_WristRO[1],FK_WristRO[2]))	
	mc.select('fkPole')
	fkPoleT=mc.xform(q=True,ws=True,t=True)
	fkPoleRO=mc.xform(q=True,ws=True,ro=True)	
	mc.select('Pole_CON')
	mc.xform(ws=True,t=(fkPoleT[0],fkPoleT[1],fkPoleT[2]))
	mc.xform(ws=True,ro=(fkPoleRO[0],fkPoleRO[1],fkPoleRO[2]))

###################################################################################





























		