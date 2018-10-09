import maya.cmds as mc
#create IK FK SKIN joints (arm)
GeoLocList = []
GeoDic = {0:'ShoulderLeft',1:'ElbowLeft',2:'WristLeft',3:'ThighLeft',
			4:'KneeLeft',5:'AnkleLeft',6:'FootLeft',7:'Root',8:'Spine0',9:'Spine1',
			10:'Spine2',11:'Spine3',12:'Neck',13:'Head',14:'HeadEnd'}
for each in (GeoDic[0],GeoDic[1],GeoDic[2],GeoDic[3],GeoDic[4],GeoDic[5],
			GeoDic[6],GeoDic[7],GeoDic[8],GeoDic[9],GeoDic[10],GeoDic[11],GeoDic[12],GeoDic[13],GeoDic[14]):
	mc.select(each + 'Loc')
	GeoT = mc.xform(q = True,t = True,ws = True)
	GeoLocList.append(GeoT)
	
mc.select(clear=True)
for JNT in ('_FK_JNT','_IK_JNT','_SkinJNT'):
	mc.select(clear=True)
	mc.joint( n = GeoDic[0]+JNT,p = (GeoLocList[0][0],GeoLocList[0][1],GeoLocList[0][2]), rad = 0.4)
	for i in range(1,15):
		mc.joint( n = GeoDic[i]+JNT,p = (GeoLocList[i][0],GeoLocList[i][1],GeoLocList[i][2]), rad = 0.4)
		mc.joint(GeoDic[i-1]+JNT,e= True, zso = True,oj='xyz',sao  ='yup')
		if i == 2 or i == 6:
			mc.select(clear=True)		
	mc.select(GeoDic[0]+JNT , GeoDic[1]+JNT ,GeoDic[2]+JNT )
	mc.createDisplayLayer(noRecurse=True,n = JNT + '_Layer')		
for i in range(3):	
	mc.parentConstraint(GeoDic[i]+'_FK_JNT',GeoDic[i]+'_IK_JNT', GeoDic[i]+'_SkinJNT')
mc.select(GeoDic[1] + '_IK_JNT')
mc.joint(e= True , spa = True,ch = True)
mc.ikHandle( sj=GeoDic[0]+'_IK_JNT', ee=GeoDic[2]+'_IK_JNT',sol = 'ikRPsolver')
mc.rename('ikHandle1','ArmIKhandle')

#fingers joints
FingerList = []
for each in ('Pinkie','Ring','Middle','Index'):
	for i in range(4):
		mc.select(each+'LeftLoc'+str(i))
		LT = mc.xform(q  =True,t = True,ws = True)
		FingerList.append(LT)				
	mc.select(clear=True)
	mc.joint( n = each+'Left0',p=(FingerList[0][0],FingerList[0][1],FingerList[0][2]), rad = 0.2)
	for i in range(1,4):
		mc.joint(n = each+'Left'+str(i),p = (FingerList[i][0],FingerList[i][1],FingerList[i][2]), rad = 0.2)
		mc.joint(each+'Left'+ str(i-1),e= True, zso = True,oj='xyz',sao  ='yup')
	FingerList=[]
	
#Thumb
for i in range(3):
	mc.select('ThumbLeftLoc'+str(i))
	ThumbLT = mc.xform(q  =True,t = True,ws = True)
	FingerList.append(ThumbLT)
mc.select(clear=True)
mc.joint( n = 'ThumbLeft0',p=(FingerList[0][0],FingerList[0][1],FingerList[0][2]), rad = 0.2)
for i in range(1,3):
	mc.joint(n = 'ThumbLeft'+str(i),p = (FingerList[i][0],FingerList[i][1],FingerList[i][2]), rad = 0.2)
	mc.joint('ThumbLeft'+str(i-1),e= True, zso = True,oj='xyz',sao  ='yup')
FingerList=[]

#create hand
mc.select(clear=True)
wirstT = mc.xform('Wrist_SkinJNT',q = True,t = True,ws = True)
mc.joint( p = (wirstT[0],wirstT[1],wirstT[2]))
mc.joint(n = 'LeftHand',e= True, zso = True,oj='xyz',sao  ='yup', rad = 0.3)
for each in ('ThumbLeft0','PinkieLeft0','RingLeft0','MiddleLeft0','IndexLeft0'):	
	mc.parent(each,'LeftHand')
for each in ('Wrist_FK_JNT','Wrist_FK_JNT','Wrist_FK_JNT'):  
	mc.pointConstraint(each ,'LeftHand')
	mc.orientConstraint(each ,'LeftHand')
for each in ('shoulder'	
mc.parent(,'Spine3_FK_JNT')
	
	
	
	
	
	
	
	
	
	
	
	
	
	










































