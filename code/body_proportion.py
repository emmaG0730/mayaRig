import maya.cmds as mc

def createLoc():
	head= 2
	mc.spaceLocator(n = 'LeftFootLoc')
	mc.scale(0.6,0.6,0.6)
	mc.move(1,0,0)
	mc.color(rgb=(0,0,1))
	
	mc.spaceLocator(n = 'LeftAnkleLoc')
	mc.move(1,head*0.5,0)
	mc.scale(0.2,0.2,0.2)
	mc.color(rgb=(0.5,0,0))
	
	mc.spaceLocator(n = 'LeftKneeLoc')
	mc.move(1,head*2,0)
	mc.scale(0.3,0.3,0.3)
	mc.color(rgb=(0.5,0.2,0))
	
	mc.spaceLocator(n = 'LeftThigh')
	mc.move(1,head*4,0)
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