import maya.cmds as mc

head= 2

def createLoc():
	mc.spaceLocator(n = 'FootLoc')
	mc.scale(0.6,0.6,0.6)
	mc.color(rgb=(0,0,1))
	
	mc.spaceLocator(n = 'AnkleLoc')
	mc.move(0,head*0.5,0)
	mc.scale(0.2,0.2,0.2)
	mc.color(rgb=(0.5,0,0))
	
	mc.spaceLocator(n = 'KneeLoc')
	mc.move(0,head*2,0)
	mc.scale(0.3,0.3,0.3)
	mc.color(rgb=(0.5,0.2,0))
	
	mc.spaceLocator(n = 'PelvisLoc')
	mc.move(0,head*4,0)
	mc.scale(0.4,0.4,0.4)
	mc.color(rgb=(0.5,0.2,0.5))
	
	mc.spaceLocator(n = 'NeckLoc')
	mc.move(0,head*6.5,0)
	mc.scale(0.2,0.2,0.2)
	mc.color(rgb=(0,0.2,0.5))
	
	mc.spaceLocator(n = 'ShoulderLeftLoc')
	mc.move(head,head*6.5,0)
	mc.scale(0.2,0.2,0.2)
	mc.color(rgb=(0,0.2,0.5))
	
	
	mc.spaceLocator(n = 'ElbowLeftLoc')
	mc.move(head*2.5,head*6.5,0)
	mc.scale(0.2,0.2,0.2)
	mc.color(rgb=(0,0.2,0.5))
	
	mc.spaceLocator(n = 'WristLeftLoc')
	mc.move(head*3.7,head*6.5,0)
	mc.scale(0.2,0.2,0.2)
	mc.color(rgb=(0,0.2,0.5))
	
	mc.spaceLocator(n = 'IndexLoc3')
	mc.move(head*4.4,head*6.5,0)
	mc.scale(0.1,0.1,0.1)
	mc.color(rgb=(0,0.2,0.5))
	
	mc.spaceLocator(n = 'IndexLoc0')
	fingerEnd = mc.getAttr('IndexLoc3.tx')
	wrist = mc.getAttr('WristLeftLoc.tx')
	halfhand = wrist+(fingerEnd - wrist)*0.5
	mc.move(halfhand,head*6.5,0)
	mc.scale(0.05,0.05,0.05)
	
	mc.spaceLocator(n = 'IndexLoc1')
	fingerEnd = mc.getAttr('IndexLoc3.tx')
	middlefingerRoot = mc.getAttr('IndexLoc0.tx')
	halfmiddleFinger = middlefingerRoot + (fingerEnd - middlefingerRoot)*0.5
	mc.move(halfmiddleFinger,head*6.5,0)
	mc.scale(0.05,0.05,0.05)
	
	mc.spaceLocator(n = 'IndexLoc2')
	fingerEnd = mc.getAttr('IndexLoc3.tx')
	IndexLoc1 = mc.getAttr('IndexLoc1.tx')
	halfmiddleSecondFinger = IndexLoc1 + (fingerEnd - IndexLoc1)*0.5
	mc.move(halfmiddleSecondFinger,head*6.5,0)
	mc.scale(0.05,0.05,0.05)
	
	mc.select('IndexLoc0','IndexLoc1','IndexLoc2','IndexLoc3')
	mc.move(0,0,0.2,r = True)
	
	mc.spaceLocator(n = 'ShoulderRightLoc')
	mc.move(-head,head*6.5,0)
	mc.scale(0.2,0.2,0.2)
	mc.color(rgb=(0,0.2,0.5))
	
	
	mc.spaceLocator(n = 'HeadLoc')
	mc.move(0,head*7,0)
	mc.scale(0.5,0.5,0.5)
	mc.color(rgb=(0,0.2,0.5))
	
	mc.spaceLocator(n = 'HeadEndLoc')
	mc.move(0,head*8,0)
	mc.scale(0.7,0.7,0.7)
	mc.color(rgb=(0,0,2))
	
	#other fingers besides index
	for i in range(3):
		mc.select('IndexLoc0','IndexLoc1','IndexLoc2','IndexLoc3')
		mc.duplicate()
		mc.move(0,0,-0.2*(i+1),r = True)
	
	for j in range(4):
		mc.rename('IndexLoc' + str(j+4),'MiddleLoc' + str(j))
	for j in range(4,8):
		mc.rename('IndexLoc' + str(j+4),'RingLoc' + str(j-4))
	for j in range(8,12):
		mc.rename('IndexLoc' + str(j+4),'PinkieLoc' + str(j-8))
	#thumb
	mc.select('IndexLoc0','IndexLoc1','IndexLoc2')
	mc.duplicate()
	mc.move(0,0,0.2,r = True)
	for j in range(3):
		mc.rename('IndexLoc' + str(j+4),'ThumbLoc' + str(j))
	
createLoc()

	

#fingers joints
FingerList = []
for each in ('Pinkie','Ring','Middle','Index'):
	for i in range(4):
		mc.select(each+'Loc'+str(i))
		LT = mc.xform(q  =True,t = True,ws = True)
		FingerList.append(LT)
				
	mc.select(clear=True)
	mc.joint( n = each+'0',p=(FingerList[0][0],FingerList[0][1],FingerList[0][2]))
	for i in range(1,4):
		mc.joint(n = each+str(i),p = (FingerList[i][0],FingerList[i][1],FingerList[i][2]), rad = 0.2)
		mc.joint(each+str(i-1),e= True, zso = True,oj='xyz',sao  ='yup', rad = 0.2)
	FingerList=[]
#Thumb
for i in range(3):
	mc.select('ThumbLoc'+str(i))
	ThumbLT = mc.xform(q  =True,t = True,ws = True)
	FingerList.append(ThumbLT)
			
mc.select(clear=True)
mc.joint( n = 'Thumb0',p=(FingerList[0][0],FingerList[0][1],FingerList[0][2]))
for i in range(1,3):
	mc.joint(n = 'Thumb'+str(i),p = (FingerList[i][0],FingerList[i][1],FingerList[i][2]), rad = 0.2)
	mc.joint('Thumb'+str(i-1),e= True, zso = True,oj='xyz',sao  ='yup', rad = 0.2)
FingerList=[]


#create IK FK SKIN joints (arm)
ArmLocList = []
ArmDic = {0:'shoulder',1:'Elbow',2:'Wrist'}

for each in ('Shoulder','Elbow','Wrist'):
	mc.select(each + 'LeftLoc')
	ArmT = mc.xform(q = True,t = True,ws = True)
	ArmLocList.append(ArmT)
	
mc.select(clear=True)
for JNT in ('_FK_JNT','_IK_JNT','_SkinJNT'):
	mc.select(clear=True)
	mc.joint( n = ArmDic[0]+JNT,p = (ArmLocList[0][0],ArmLocList[0][1],ArmLocList[0][2]), rad = 0.4)
	for i in range(1,3):
		mc.joint( n = ArmDic[i]+JNT,p = (ArmLocList[i][0],ArmLocList[i][1],ArmLocList[i][2]))
		mc.joint(ArmDic[i-1]+JNT,e= True, zso = True,oj='xyz',sao  ='yup', rad = 0.4)
		
	mc.select(ArmDic[0]+JNT , ArmDic[1]+JNT ,ArmDic[2]+JNT )
	mc.createDisplayLayer(noRecurse=True,n = JNT + '_Layer')
for i in range(3):	
	mc.parentConstraint(ArmDic[i]+'_FK_JNT',ArmDic[i]+'_IK_JNT', ArmDic[i]+'_SkinJNT')

mc.select(ArmDic[1] + '_IK_JNT')
mc.joint(e= True,spa = True,ch = True)
mc.ikHandle( sj=ArmDic[0]+'_IK_JNT', ee=ArmDic[2]+'_IK_JNT',sol = 'ikRPsolver')
mc.rename('ikHandle1','ArmIKhandle')







	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	










































