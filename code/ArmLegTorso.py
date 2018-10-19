import maya.cmds as mc
#create IK FK SKIN joints (arm)

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
	mc.joint(GeoDic[i-1]+'_JNT',e= True, zso = True,oj='xyz',sao  ='yup')
	if i == 2 or i == 7 or i == 15:
		mc.setAttr(GeoDic[i]+'_JNT' + '.jointOrientZ',0)
		mc.setAttr(GeoDic[i]+'_JNT' + '.jointOrientY',0)
		mc.setAttr(GeoDic[i]+'_JNT' + '.jointOrientX',0)
		mc.select(clear=True)
		
mc.select(GeoDic[1] + '_JNT')
mc.joint(e= True , spa = True,ch = True)
mc.ikHandle( sj=GeoDic[0]+'_JNT', ee=GeoDic[2]+'_JNT',sol = 'ikRPsolver')
mc.rename('ikHandle1','WristIKhandle')		

mc.select(GeoDic[4] + '_JNT')
mc.joint(e= True , spa = True,ch = True)
mc.ikHandle( sj=GeoDic[3]+'_JNT', ee=GeoDic[5]+'_JNT',sol = 'ikRPsolver')
mc.rename('ikHandle1','AnkleIKhandle')

#mc.select(GeoDic[4] + '_JNT')
#mc.joint(e= True , spa = True,ch = True)
mc.ikHandle( sj=GeoDic[5]+'_JNT', ee=GeoDic[6]+'_JNT',sol = 'ikSCsolver')
mc.rename('ikHandle1','FootIKhandle')
mc.ikHandle( sj=GeoDic[6]+'_JNT', ee=GeoDic[7]+'_JNT',sol = 'ikSCsolver')
mc.rename('ikHandle1','ToeIKhandle')


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


#fingers joints
FingerList = []
for each in ('Pinkie','Ring','Middle','Index'):
	for i in range(4):
		mc.select(each+'LeftLoc'+str(i))
		LT = mc.xform(q  =True,t = True,ws = True)
		FingerList.append(LT)				
	mc.select(clear=True)
	mc.joint( n = each+'Left0',p=(FingerList[0][0],FingerList[0][1],FingerList[0][2]), rad = 0.1)
	for i in range(1,4):
		mc.joint(n = each+'Left'+str(i),p = (FingerList[i][0],FingerList[i][1],FingerList[i][2]), rad = 0.1)
		mc.joint(each+'Left'+ str(i-1),e= True, zso = True,oj='xyz',sao  ='yup')
	FingerList=[]
	
#Thumb
for i in range(3):
	mc.select('ThumbLeftLoc'+str(i))
	ThumbLT = mc.xform(q  =True,t = True,ws = True)
	FingerList.append(ThumbLT)
mc.select(clear=True)
mc.joint( n = 'ThumbLeft0',p=(FingerList[0][0],FingerList[0][1],FingerList[0][2]), rad = 0.1)
for i in range(1,3):
	mc.joint(n = 'ThumbLeft'+str(i),p = (FingerList[i][0],FingerList[i][1],FingerList[i][2]), rad = 0.1)
	mc.joint('ThumbLeft'+str(i-1),e= True, zso = True,oj='xyz',sao  ='yup')
FingerList=[]

#create hand
mc.delete(mc.duplicate('WristLeft_JNT',rc = True)[1:])
mc.rename('WristLeft_JNT1','L_hand')
mc.parent('L_hand',w = True)

for each in ('ThumbLeft0','PinkieLeft0','RingLeft0','MiddleLeft0','IndexLeft0'):	
	mc.parent(each,'L_hand')
mc.pointConstraint('WristLeft_JNT','L_hand')
mc.orientConstraint('WristLeft_JNT','L_hand')


#torso splineIK ,didn't finished
influences = ['Root_JNT', 'Spine3_JNT']

mc.rename('curve1','spine_curve')
mc.ikHandle(sj=influences[0], ee=influences[1] , sol = 'ikSplineSolver',ccv = False,c = 'spine_curve',roc = True)
scls = mc.skinCluster(influences,'spine_curve', name='spine_skinCluster', toSelectedBones=True, 
							bindMethod=1, skinMethod=0, normalizeWeights=1)[0]

	
#hide body locators
mc.ls(sl = True,type = 'locator')

	
	
	
	
	
	
	
	
	
	










































