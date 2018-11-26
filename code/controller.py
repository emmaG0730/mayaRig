import maya.cmds as mc
from proportion import *
createLoc()
from body_joint import *
joint_creation()

#create FK controller and constraint
for i in ('Shoulder','Elbow','Wrist','Thigh','Knee','Ankle','Foot','Toe'):
	mc.circle(n = 'FK_Left' + i +'_CON',c = (0,0,0),r =1)
	mc.group('FK_Left'+ i +'_CON',name ='FK_Left'+ i +'_CON_grp' )
	mc.delete(mc.parentConstraint(i + 'Left_JNT','FK_Left'+ i +'_CON_grp',mo = False))
	mc.setAttr('FK_Left' + i + '_CON.rotateY', 90)
	mc.makeIdentity('FK_Left' + i + '_CON',apply = True)
	mc.parentConstraint('FK_Left' + i + '_CON',i + 'Left_JNT')
mc.parent('FK_LeftWrist_CON_grp','FK_LeftElbow_CON')
mc.parent('FK_LeftElbow_CON_grp','FK_LeftShoulder_CON')
mc.parent('FK_LeftAnkle_CON_grp','FK_LeftKnee_CON')
mc.parent('FK_LeftKnee_CON_grp','FK_LeftThigh_CON')
mc.parent('FK_LeftFoot_CON_grp','FK_LeftKnee_CON')
mc.parent('FK_LeftToe_CON_grp','FK_LeftFoot_CON')

#finger FK contrller
for each in ('Pinkie','Ring','Middle','Index','Thumb'):
	if each == 'Thumb':
		joint_num = 3
	else:
		joint_num = 4
	for i in range(joint_num-1):
		mc.select(each+'Left'+str(i))
		mc.circle(n = 'FK_Left' + each + str(i) + '_CON',c = (0,0,0),r =0.1)
		mc.group('FK_Left' + each + str(i) + '_CON',name ='FK_Left' + each  + str(i) +'_CON_grp' )
		mc.delete(mc.parentConstraint(each+'Left'+str(i),'FK_Left' + each  + str(i) +'_CON_grp',mo = False))
		mc.setAttr('FK_Left' + each + str(i) + '_CON.rotateY', 90)
		mc.makeIdentity('FK_Left' + each + str(i) + '_CON',apply = True)
		mc.parentConstraint('FK_Left' + each + str(i) + '_CON',each+'Left'+str(i))
	i = 0
	while (i < joint_num - 2):	
		mc.parent('FK_Left' + each  + str(joint_num-1-i) + '_CON_grp','FK_Left' + each  + str(joint_num-2-i) + '_CON')
		i += 1	
	mc.parent('FK_Left' + each  + str(i) +'_CON_grp','FK_LeftWrist_CON')
		
#create IK controller 
mc.file('F:\\GitHub\\tools\\mayaRig\\squreAndCubeIcon.ma',i = True)
mc.select('controller')
mc.duplicate()
mc.rename('controller1','IK_LeftWrist_CON')
mc.group('IK_LeftWrist_CON',n = 'IK_LeftWrist_CON_grp' , r = True)
mc.delete(mc.parentConstraint('FK_LeftWrist_CON', 'IK_LeftWrist_CON_grp'))
mc.parent('WristLeftIKhandle','IK_LeftWrist_CON') 
mc.scale(1,0.5,1.2)

#create pole controller
for each in ('Elbow','Knee'):
	mc.delete(mc.duplicate(each + 'Left_JNT',rc = True)[1:])
	mc.rename(each+'Left_JNT1',each+'Pole_CON')
	mc.parent(each+'Pole_CON',w = True)
	joint_t = mc.xform(each+'Left_JNT', t=1, ws=1, q=1)	
	mc.group(each+'Pole_CON',n = each+'Pole_CON_grp')
	if each == 'Elbow':
		mc.move(0,0,-2,each+'Pole_CON_grp',ls = True)
	elif each == 'Knee':
		mc.move(0,0,2,each+'Pole_CON_grp',ls = True)
	pole_t = mc.xform(each+'Pole_CON', t=1, ws=1, q=1)
	#add a line between pole control and elbow
	mc.curve(n=each+'_pole_line',p = [(0,0,0),(1,0,0)],d =1)
	mc.select(each+'_pole_line.cv[0]')
	mc.xform(ws=True,t=(joint_t[0],joint_t[1],joint_t[2]))
	mc.select(each+'_pole_line.cv[1]')
	mc.xform(ws=True,t=(pole_t[0],pole_t[1],pole_t[2]))
	influences = [each+'Pole_CON', each+'Left_JNT']
	mc.skinCluster(influences,each+'_pole_line', name=each+'_skinCluster', toSelectedBones=True,
					bindMethod=1, skinMethod=0, normalizeWeights=1)[0]
	mc.select(each+'_pole_line',each+'Pole_CON')
	mc.setAttr(each+"Pole_CON.overrideEnabled",1)
	mc.setAttr( each+"_pole_line.overrideColor", 0)
	
mc.poleVectorConstraint('ElbowPole_CON','WristLeftIKhandle') 
mc.poleVectorConstraint('KneePole_CON','AnkleLeftIKhandle') 

#Switcher arm
for each in ('Wrist','Foot'):
	mc.duplicate('controller')
	mc.rename('controller1', each + 'IKFKSwitch')
	mc.group(each + 'IKFKSwitch',n = each + 'Switch_grp')
	mc.scale(0.6,0.02,0.6)
	mc.delete(mc.parentConstraint('FK_Left'+each+'_CON', each + 'Switch_grp'))
	mc.parent(each + 'Switch_grp',each + 'Left_JNT')
	mc.move(0,1,0,ls = True)
	mc.select(each + 'IKFKSwitch')
	mc.addAttr(ln = each + 'IKFKTrigger',at= 'enum',en = 'IK:FK',k=True)
	for item in ('tx','ty','tz','rx','ry','rz','sx','sy','sz','visibility'):
		mc.setAttr(each + 'IKFKSwitch.'+item,l = True,k =False)

#foot ik controller -----1
'''
for each in ('Foot','Toe'):
	mc.duplicate('controller')
	mc.rename('controller1','IK_Left'+each+'_CON')
	mc.group('IK_Left'+each+'_CON',n = 'IK_Left'+each+'_CON_grp')
	mc.move(0,-0.5,0.5,'IK_Left'+each+'_CON_grp.scalePivot','IK_Left'+each+'_CON_grp.rotatePivot')
	mc.delete(mc.pointConstraint(each+'Left_JNT','IK_Left'+each+'_CON_grp'))
	mc.scale(1,0.5,1)
mc.select('IK_LeftFoot_CON_grp')
mc.scale(1,0.5,1.4)
Ankle_t = mc.xform('AnkleLeft_JNT', t=1, ws=1, q=1)
mc.move(Ankle_t[0],Ankle_t[1],Ankle_t[2],'IK_LeftFoot_CON.scalePivot','IK_LeftFoot_CON.rotatePivot')
mc.parent('AnkleIKhandle','IK_LeftToe_CON_grp','FootIKhandle','ToeIKhandle','IK_LeftFoot_CON')
'''

#foot ik controller -----2
mc.file('F:\\GitHub\\tools\\mayaRig\\footprint.ma',i = True)
mc.duplicate('footprint',n = 'Footprint_L')
mc.group('Footprint_L',n = 'Footprint_L_grp')
mc.setAttr('Footprint_L_grp.rotateZ',180)
mc.delete(mc.pointConstraint('FootLeft_JNT','Footprint_L_grp'))
ankle_t = mc.xform('AnkleLeft_JNT',q= 1,ws = 1, t= 1)
mc.move(ankle_t[0],ankle_t[1],ankle_t[2],'Footprint_L.scalePivot','Footprint_L.rotatePivot')
mc.parent('AnkleLeftIKhandle','Footprint_L')

#hand controller
###################################################################################################

#one joint chain IKFK switch(ARM)
# From IK to FK
if mc.getAttr("WristIKFKSwitch.WristIKFKTrigger"):             
	mc.delete(mc.orientConstraint("ShoulderLeft_JNT", "FK_LeftShoulder_CON"))
	mc.delete(mc.parentConstraint("WristLeft_JNT", "FK_LeftWrist_CON"))
	mc.setAttr ("WristLeft_JNT_parentConstraint1.FK_LeftWrist_CONW0" ,1)
	mc.setAttr ("ElbowLeft_JNT_parentConstraint1.FK_LeftElbow_CONW0" ,1)
	mc.setAttr ("ShoulderLeft_JNT_parentConstraint1.FK_LeftShoulder_CONW0" ,1)
	mc.setAttr('WristLeftIKhandle.ikBlend', 0)
	for each in ('Pinkie','Ring','Middle','Index','Thumb'):
		mc.parent('FK_Left'+each+'0_CON_grp','FK_LeftWrist_CON')
	 
else:
    # From FK to IK
	mc.delete(mc.parentConstraint("FK_LeftWrist_CON", 'IK_LeftWrist_CON'))
	arm01Vec = [mc.xform("ElbowLeft_JNT", t=1, ws=1, q=1)[i] - mc.xform("ShoulderLeft_JNT", t=1, ws=1, q=1)[i] for i in range(3)]
	arm02Vec = [mc.xform("ElbowLeft_JNT", t=1, ws=1, q=1)[i] - mc.xform("WristLeft_JNT", t=1, ws=1, q=1)[i] for i in range(3)]
	mc.xform("ElbowPole_CON", t=[mc.xform("ElbowLeft_JNT", t=1, q=1, ws=1)[i] + arm01Vec[i] * .75 + arm02Vec[i] * .75 for i in range(3)], ws=1)
	mc.setAttr('WristLeftIKhandle.ikBlend', 1)				
	mc.setAttr ("WristLeft_JNT_parentConstraint1.FK_LeftWrist_CONW0" ,0)
	mc.setAttr ("ElbowLeft_JNT_parentConstraint1.FK_LeftElbow_CONW0" ,0)
	mc.setAttr ("ShoulderLeft_JNT_parentConstraint1.FK_LeftShoulder_CONW0" ,0)
	for each in ('Pinkie','Ring','Middle','Index','Thumb'):
		mc.parent('FK_Left'+each+'0_CON_grp','IK_LeftWrist_CON')
	

######################################################################################################

#one joint chain IKFK switch(LEG)
# From IK to FK
if mc.getAttr("FootIKFKSwitch.FootIKFKTrigger"):             
	mc.delete(mc.orientConstraint("ThighLeft_JNT", "FK_LeftThigh_CON"))
	mc.delete(mc.parentConstraint("AnkleLeft_JNT", "FK_LeftAnkle_CON"))
	mc.setAttr ("ThighLeft_JNT_parentConstraint1.FK_LeftThigh_CONW0" ,1)
	mc.setAttr ("KneeLeft_JNT_parentConstraint1.FK_LeftKnee_CONW0" ,1)
	mc.setAttr ("AnkleLeft_JNT_parentConstraint1.FK_LeftAnkle_CONW0" ,1)
	mc.setAttr('AnkleLeftIKhandle.ikBlend', 0)
	mc.setAttr('FootLeftIKhandle.ikBlend', 0)
	mc.setAttr('ToeLeftIKhandle.ikBlend', 0) 
else:
    # From FK to IK
	mc.delete(mc.pointConstraint("FK_LeftAnkle_CON", 'IK_LeftFoot_CON'))
	arm01Vec = [mc.xform("KneeLeft_JNT", t=1, ws=1, q=1)[i] - mc.xform("ThighLeft_JNT", t=1, ws=1, q=1)[i] for i in range(3)]
	arm02Vec = [mc.xform("KneeLeft_JNT", t=1, ws=1, q=1)[i] - mc.xform("AnkleLeft_JNT", t=1, ws=1, q=1)[i] for i in range(3)]
	mc.xform("KneePole_CON", t=[mc.xform("KneeLeft_JNT", t=1, q=1, ws=1)[i] + arm01Vec[i] * .75 + arm02Vec[i] * .75 for i in range(3)], ws=1)
	mc.setAttr('AnkleLeftIKhandle.ikBlend', 1)
	mc.setAttr('FootLeftIKhandle.ikBlend', 1)
	mc.setAttr('ToeLeftIKhandle.ikBlend', 1)		
	mc.setAttr ("ThighLeft_JNT_parentConstraint1.FK_LeftThigh_CONW0" ,0)
	mc.setAttr ("KneeLeft_JNT_parentConstraint1.FK_LeftKnee_CONW0" ,0)
	mc.setAttr ("AnkleLeft_JNT_parentConstraint1.FK_LeftAnkle_CONW0" ,0)
	
#########################################################################################################
#bodycontroller
mc.circle(n = 'Spine0_con',r = 2)
mc.group('Spine0_con',n = 'Spine0_con_grp')
mc.delete(mc.parentConstraint('Spine0_JNT','Spine0_con_grp'))
mc.scale(0.5,1,1)
mc.makeIdentity('Spine0_con',apply = True)


mc.duplicate('Spine1_con')
mc.rename('Spine1_con','Spine3_con')
mc.group('Spine3_con',n = 'Spine3_con_grp')
mc.delete(mc.parentConstraint('Spine3_JNT','Spine3_con_grp'))

mc.delete(mc.duplicate('Spine3_JNT',rc = True)[1:])
mc.rename('Spine3_JNT1','spine3_con_joint')
mc.parent('spine3_con_joint',w = True)

mc.delete(mc.duplicate('Root_JNT',rc = True)[1:])
mc.rename('Root_JNT1','Root_con_joint')
mc.parent('Root_con_joint',w = True)

mc.parent('spine3_con_joint','Spine3_con')
mc.parent('Root_con_joint','Spine1_con')

#whole body controller
mc.circle(n = 'body_CON',r = 4)
mc.setAttr('body_CON.rotateX',-90)




































































		