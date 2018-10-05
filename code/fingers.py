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
	
createLoc()








#create IK FK SKIN joints (arm)
shoulderLT = mc.getAttr('ShoulderLeftLoc.t')[0]
elbowLT = mc.getAttr('ElbowLeftLoc.t')[0]
wristLT = mc.getAttr('WristLeftLoc.t')[0]
mc.select( clear=True )		
shouder_FK = mc.joint(n = 'shoulder_FK_JNT')
mc.joint(shouder_FK,e = True,p = (shoulderLT[0],shoulderLT[1],shoulderLT[2]), rad = 0.5,oj='xyz',sao  ='yup')
elbow_FK = mc.joint(n = 'elbow_FK_JNT')
mc.joint(elbow_FK,e = True,p = (elbowLT[0],elbowLT[1],elbowLT[2]), rad = 0.5,oj='xyz',sao  ='yup')
wrist_FK = mc.joint(n = 'wrist_FK_JNT')
mc.joint(wrist_FK,e = True,p = (wristLT[0],wristLT[1],wristLT[2]), rad = 0.5,oj='xyz',sao  ='yup')
mc.select(shouder_FK,elbow_FK,wrist_FK)
mc.createDisplayLayer(noRecurse=True,n = 'FK_Layer')
mc.setAttr('FK_Layer.color', 13)

mc.select( clear=True )
shouder_IK = mc.joint(n = 'shoulder_IK_JNT')
mc.joint(shouder_IK,p = (shoulderLT[0],shoulderLT[1],shoulderLT[2]),e =True, rad = 0.5,oj='xyz',sao  ='yup')
elbow_IK = mc.joint(n = 'elbow_IK_JNT')
mc.joint(elbow_IK,p = (elbowLT[0],elbowLT[1],elbowLT[2]),e =True,rad = 0.5,oj='xyz',sao  ='yup')
wrist_IK = mc.joint(n = 'wrist_IK_JNT')
mc.joint(wrist_IK,p = (wristLT[0],wristLT[1],wristLT[2]),e =True, rad = 0.5,oj='xyz',sao  ='yup')
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
mc.joint(shouder_SKIN,e = True,p = (shoulderLT[0],shoulderLT[1],shoulderLT[2]), rad = 0.5,oj='xyz',sao  ='yup')
elbow_SKIN = mc.joint(n = 'elbow_SKIN_JNT',p = (4,0,0), rad = 0.5,oj='xyz',sao  ='yup')
mc.joint(elbow_SKIN,e = True,p = (elbowLT[0],elbowLT[1],elbowLT[2]), rad = 0.5,oj='xyz',sao  ='yup')
wrist_SKIN = mc.joint(n = 'wrist_SKIN_JNT',p = (8,0,0), rad = 0.5,oj='xyz',sao  ='yup')
mc.joint(wrist_SKIN,e = True,p = (wristLT[0],wristLT[1],wristLT[2]), rad = 0.5,oj='xyz',sao  ='yup')
mc.select(shouder_SKIN,elbow_SKIN,wrist_SKIN)
mc.createDisplayLayer(noRecurse=True,n = 'SKIN_Layer')

mc.parentConstraint('shoulder_FK_JNT','shoulder_IK_JNT', 'shoulder_SKIN_JNT')
mc.parentConstraint('elbow_FK_JNT','elbow_IK_JNT','elbow_SKIN_JNT')
mc.parentConstraint('wrist_FK_JNT','wrist_IK_JNT','wrist_SKIN_JNT')

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
	




	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	










































