import maya.cmds as mc
#import body_proportion
#body_proportion.createLoc()	


#fingers joints
FingerList = []
for each in ('Pinkie','Ring','Middle','Index'):
	for i in range(4):
		mc.select(each+'Loc'+str(i))
		LT = mc.xform(q  =True,t = True,ws = True)
		FingerList.append(LT)
				
	mc.select(clear=True)
	mc.joint( n = each+'0',p=(FingerList[0][0],FingerList[0][1],FingerList[0][2]), rad = 0.2)
	for i in range(1,4):
		mc.joint(n = each+str(i),p = (FingerList[i][0],FingerList[i][1],FingerList[i][2]), rad = 0.2)
		mc.joint(each+str(i-1),e= True, zso = True,oj='xyz',sao  ='yup')
	FingerList=[]
#Thumb
for i in range(3):
	mc.select('ThumbLoc'+str(i))
	ThumbLT = mc.xform(q  =True,t = True,ws = True)
	FingerList.append(ThumbLT)
			
mc.select(clear=True)
mc.joint( n = 'Thumb0',p=(FingerList[0][0],FingerList[0][1],FingerList[0][2]), rad = 0.2)
for i in range(1,3):
	mc.joint(n = 'Thumb'+str(i),p = (FingerList[i][0],FingerList[i][1],FingerList[i][2]), rad = 0.2)
	mc.joint('Thumb'+str(i-1),e= True, zso = True,oj='xyz',sao  ='yup')
FingerList=[]


#create IK FK SKIN joints (arm)
GeoLocList = []
GeoDic = {0:'Shoulder',1:'Elbow',2:'Wrist',3:'Thigh',4:'Knee',5:'Ankle',6:'Foot'}

for each in (GeoDic[0],GeoDic[1],GeoDic[2],GeoDic[3],GeoDic[4],GeoDic[5],GeoDic[6]):
	mc.select(each + 'LeftLoc')
	GeoT = mc.xform(q = True,t = True,ws = True)
	GeoLocList.append(GeoT)
	
count = 1
clearSelect = True	
mc.select(clear=True)
for JNT in ('_FK_JNT','_IK_JNT','_SkinJNT'):
	mc.select(clear=True)
	mc.joint( n = GeoDic[0]+JNT,p = (GeoLocList[0][0],GeoLocList[0][1],GeoLocList[0][2]), rad = 0.4)
	for i in range(1,7):
		mc.joint( n = GeoDic[i]+JNT,p = (GeoLocList[i][0],GeoLocList[i][1],GeoLocList[i][2]), rad = 0.4)
		mc.joint(GeoDic[i-1]+JNT,e= True, zso = True,oj='xyz',sao  ='yup')
		if i=3:
			mc.select(clear=True)
		
	mc.select(GeoDic[0]+JNT , GeoDic[1]+JNT ,GeoDic[2]+JNT )
	mc.createDisplayLayer(noRecurse=True,n = JNT + '_Layer')

		
for i in range(3):	
	mc.parentConstraint(GeoDic[i]+'_FK_JNT',GeoDic[i]+'_IK_JNT', GeoDic[i]+'_SkinJNT')

mc.select(GeoDic[1] + '_IK_JNT')
mc.joint(e= True,spa = True,ch = True)
mc.ikHandle( sj=GeoDic[0]+'_IK_JNT', ee=GeoDic[2]+'_IK_JNT',sol = 'ikRPsolver')
mc.rename('ikHandle1','ArmIKhandle')


#create hand
mc.select(clear=True)
wirstT = mc.xform('Wrist_SkinJNT',q = True,t = True,ws = True)
mc.joint( p = (wirstT[0],wirstT[1],wirstT[2]))
mc.joint(n = 'LeftHand',e= True, zso = True,oj='xyz',sao  ='yup', rad = 0.3)
for each in ('Thumb0','Pinkie0','Ring0','Middle0','Index0'):	
	mc.parent(each,'LeftHand')
for each in ('Wrist_FK_JNT','Wrist_FK_JNT','Wrist_FK_JNT'):  
	mc.pointConstraint(each ,'LeftHand')
	mc.orientConstraint(each ,'LeftHand')


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	










































