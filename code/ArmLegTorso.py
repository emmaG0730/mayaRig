import maya.cmds as mc
#create IK FK SKIN joints (arm)
def joint_creation():
	GeoLocList = []
	GeoDic = {0:'ShoulderLeft',1:'ElbowLeft',2:'WristLeft',3:'ThighLeft',
				4:'KneeLeft',5:'AnkleLeft',6:'FootLeft',7:'ToeLeft',8:'Root',9:'Spine0',10:'Spine1',
				11:'Spine2',12:'Spine3',13:'Neck',14:'Head',15:'HeadEnd',16:'Clavicle'}
	for each in (GeoDic[0],GeoDic[1],GeoDic[2],GeoDic[3],GeoDic[4],GeoDic[5],
				GeoDic[6],GeoDic[7],GeoDic[8],GeoDic[9],GeoDic[10],GeoDic[11],GeoDic[12],
				GeoDic[13],GeoDic[14],GeoDic[15],GeoDic[16]):
		mc.select(each + 'Loc')
		GeoT = mc.xform(q = True,t = True,ws = True)
		GeoLocList.append(GeoT)
	mc.select(clear=True)
	
	#new method create torso joints only one joint chain
	mc.select(clear=True)
	mc.joint( n = GeoDic[0]+'_JNT',p = (GeoLocList[0][0],GeoLocList[0][1],GeoLocList[0][2]), rad = 0.4)
	for i in range(1,17):
		mc.joint( n = GeoDic[i]+'_JNT',p = (GeoLocList[i][0],GeoLocList[i][1],GeoLocList[i][2]), rad = 0.4)
		mc.joint(GeoDic[i-1]+'_JNT',e= True, zso = True,oj='xyz',sao  ='yup',roo = 'zxy')
		if i == 2 or i == 7 or i == 15:
			mc.setAttr(GeoDic[i]+'_JNT' + '.jointOrientZ',0)
			mc.setAttr(GeoDic[i]+'_JNT' + '.jointOrientY',0)
			mc.setAttr(GeoDic[i]+'_JNT' + '.jointOrientX',0)
			mc.select(clear=True)
			
	for i in range(5):
		if i == 1 or i == 4:
			mc.select(GeoDic[i] + '_JNT')
			mc.joint(e= True , spa = True,ch = True)
			mc.ikHandle( sj=GeoDic[i-1]+'_JNT', ee=GeoDic[i+1]+'_JNT',sol = 'ikRPsolver')
			mc.rename('ikHandle1',GeoDic[i+1] + 'IKhandle')
	
	for i in range(2):	
		mc.ikHandle( sj=GeoDic[i+5]+'_JNT', ee=GeoDic[i+6]+'_JNT',sol = 'ikSCsolver')
		mc.rename('ikHandle1',GeoDic[i+6] + 'IKhandle')
		
	for item in ('Wrist','Ankle','Foot','Toe'):
		mc.setAttr(item + 'LeftIKhandle.rotateOrder', 2)
		mc.setAttr(item + "LeftIKhandle.rotateY", 0)		
		mc.setAttr(item + "LeftIKhandle.rotateX", 0)
		mc.setAttr(item + "LeftIKhandle.rotateZ", 0)
	#shoulder
	mc.spaceLocator(n = 'Shoulder_orient_loc')
	mc.group('Shoulder_orient_loc' ,n = 'Shoulder_orient_loc_grp')
	mc.delete(mc.pointConstraint('ShoulderLeft_JNT','Shoulder_orient_loc_grp'))	
	mc.parent( GeoDic[0]+'_JNT' , 'Shoulder_orient_loc')
	mc.parent('Shoulder_orient_loc','Clavicle_JNT')
	mc.parent('Clavicle_JNT','Spine3_JNT')
	
	mc.delete(mc.duplicate('Shoulder_orient_loc',rc = True)[1:])
	mc.rename('Shoulder_orient_loc1','Body_orient_loc')
	mc.parent('Body_orient_loc','Root_JNT')
	
	mc.delete(mc.duplicate('Shoulder_orient_loc',rc = True)[1:])
	mc.rename('Shoulder_orient_loc1','Spine_orient_loc')
	mc.parent('Spine_orient_loc','Spine3_JNT')
	
	mc.orientConstraint('Body_orient_loc','Spine_orient_loc','Shoulder_orient_loc')
	
	#create hand
	mc.delete(mc.duplicate('WristLeft_JNT',rc = True)[1:])
	mc.rename('WristLeft_JNT1','L_hand')
	mc.parent('L_hand',w = True)
	
	
	#fingers joints
	FingerList = []
	for each in ('Pinkie','Ring','Middle','Index','Thumb'):
		if each == 'Thumb':
			joint_num = 3
		else:
			joint_num = 4
		for i in range(joint_num):
			mc.select(each+'LeftLoc'+str(i))
			LT = mc.xform(q  =True,t = True,ws = True)
			FingerList.append(LT)				
		mc.select(clear=True)
		mc.joint( n = each+'Left0',p=(FingerList[0][0],FingerList[0][1],FingerList[0][2]), rad = 0.1)
		
		for i in range(1,joint_num):
			#mc.circle(n = each + 'Left'+  str(i-1) + '_CON',c = (0,0,0),r =0.1)		
			mc.joint(n = each+'Left'+str(i),p = (FingerList[i][0],FingerList[i][1],FingerList[i][2]), rad = 0.1)
			mc.joint(each+'Left'+ str(i-1),e= True, zso = True,oj='xyz',sao  ='yup',roo = 'zxy')
			if i == joint_num - 1:
				mc.setAttr(each+'Left'+ str(i) + '.rotateOrder', 2)
				mc.setAttr(each+'Left'+ str(i) + '.jointOrientZ',0)
				mc.setAttr(each+'Left'+ str(i) + '.jointOrientY',0)
				mc.setAttr(each+'Left'+ str(i) + '.jointOrientX',0)
		FingerList=[]
	for each in ('ThumbLeft0','PinkieLeft0','RingLeft0','MiddleLeft0','IndexLeft0'):	
		mc.parent(each,'L_hand')
	mc.pointConstraint('WristLeft_JNT','L_hand')
	mc.orientConstraint('WristLeft_JNT','L_hand')
joint_creation()
'''
#finger iksolver
for each in ('ThumbLeft','IndexLeft','MiddleLeft','RingLeft','PinkieLeft'):
	if each == 'ThumbLeft':
		mc.ikHandle( sj=each+'0', ee=each+'2',sol = 'ikSCsolver')
	else:
		mc.ikHandle( sj=each+'0', ee=each+'3',sol = 'ikSCsolver')
	mc.rename('ikHandle1',each + 'ikHandle')
	mc.setAttr(each + 'ikHandle.rotateOrder', 2)
	
mc.group('ThumbLeftikHandle','IndexLeftikHandle','MiddleLeftikHandle','RingLeftikHandle',
			'PinkieLeftikHandle',n = 'Left_finger_ikHandle_grp')
joint_hand = mc.xform('L_hand', t=1, ws=1, q=1)	
mc.move(joint_hand[0],joint_hand[1],joint_hand[2],'Left_finger_ikHandle_grp.scalePivot',
			'Left_finger_ikHandle_grp.rotatePivot')
			
bend_loc = mc.spaceLocator(n = 'middle_finger_bend_loc')
mc.delete(mc.parentConstraint('MiddleLeft0',bend_loc[0]))
mc.duplicate('middle_finger_bend_loc',n = 'thumb_finger_side_loc')
mc.delete(mc.parentConstraint('ThumbLeft0','thumb_finger_side_loc'))
mc.duplicate('middle_finger_bend_loc',n = 'pinkie_finger_side_loc')
mc.delete(mc.parentConstraint('PinkieLeft0','pinkie_finger_side_loc'))

for each in ('Thumb','Middle','Pinkie'):
	bend_loc = mc.spaceLocator(n = each + '_finger_bend_loc')
	mc.delete(mc.parentConstraint(each + 'Left0',bend_loc[0]))
	
mc.scale(0.1,0.1,0.1,'middle_finger_bend_loc','pinkie_finger_side_loc','thumb_finger_side_loc',
			'ThumbLeftikHandle','IndexLeftikHandle','MiddleLeftikHandle','RingLeftikHandle','PinkieLeftikHandle')
mc.parent('middle_finger_bend_loc','thumb_finger_side_loc')
mc.parent('thumb_finger_side_loc','pinkie_finger_side_loc')

L_hand_copy = mc.duplicate('L_hand',po=True)
mc.rename(L_hand_copy[0],'L_hand_const')
mc.setAttr('L_hand_const.radius',0.2)
mc.parentConstraint('L_hand_const','L_hand')
mc.parent('L_hand_const','finger_bend_loc')

#torso splineIK ,didn't finished
influences = ['Root_JNT', 'Spine3_JNT']

mc.rename('curve1','spine_curve')
mc.ikHandle(sj=influences[0], ee=influences[1] , sol = 'ikSplineSolver',ccv = False,c = 'spine_curve',roc = True)
scls = mc.skinCluster(influences,'spine_curve', name='spine_skinCluster', toSelectedBones=True, 
							bindMethod=1, skinMethod=0, normalizeWeights=1)[0]
	
#hide body locators
mc.ls(sl = True,type = 'locator')

#connect thig to root
mc.parent('ThighLeft_JNT','Root_JNT')	
'''	
	
	
	
	
	
	










































