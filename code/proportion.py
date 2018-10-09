import maya.cmds as mc

def createLoc():
	head= 2
	mc.spaceLocator(n = 'FootLeftLoc')
	mc.scale(0.6,0.6,0.6)
	mc.move(1,0,0)
	mc.color(rgb=(0,0,1))
	
	mc.spaceLocator(n = 'AnkleLeftLoc')
	mc.move(1,head*0.5,0)
	mc.scale(0.2,0.2,0.2)
	mc.color(rgb=(0.5,0,0))
	
	mc.spaceLocator(n = 'KneeLeftLoc')
	mc.move(1,head*2,0)
	mc.scale(0.3,0.3,0.3)
	mc.color(rgb=(0.5,0.2,0))
	
	mc.spaceLocator(n = 'ThighLeftLoc')
	mc.move(1,head*4,0)
	mc.scale(0.4,0.4,0.4)
	mc.color(rgb=(0.5,0.2,0.5))
	
	mc.spaceLocator(n = 'NeckLoc')
	mc.move(0,head*6.5,0)
	mc.scale(0.2,0.2,0.2)
	mc.color(rgb=(0,0.2,0.5))
	
	mc.spaceLocator(n = 'RootLoc')
	mc.move(0,head*4,0)
	mc.scale(0.2,0.2,0.2)
	mc.color(rgb=(0,0.2,0.5))
	
	mc.spaceLocator(n = 'Spine0Loc')
	mc.move(0,head*4.5,0)
	mc.scale(0.2,0.2,0.2)
	mc.color(rgb=(0,0.2,0.5))
	
	mc.spaceLocator(n = 'Spine1Loc')
	mc.move(0,head*5.0,0)
	mc.scale(0.2,0.2,0.2)
	mc.color(rgb=(0,0.2,0.5))
	
	mc.spaceLocator(n = 'Spine2Loc')
	mc.move(0,head*5.5,0)
	mc.scale(0.2,0.2,0.2)
	mc.color(rgb=(0,0.2,0.5))
	
	mc.spaceLocator(n = 'Spine3Loc')
	mc.move(0,head*6,0)
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
	
	mc.spaceLocator(n = 'IndexLeftLoc3')
	mc.move(head*4.4,head*6.5,0)
	mc.scale(0.1,0.1,0.1)
	mc.color(rgb=(0,0.2,0.5))
	
	mc.spaceLocator(n = 'IndexLeftLoc0')
	fingerEnd = mc.getAttr('IndexLeftLoc3.tx')
	wrist = mc.getAttr('WristLeftLoc.tx')
	halfhand = wrist+(fingerEnd - wrist)*0.5
	mc.move(halfhand,head*6.5,0)
	mc.scale(0.05,0.05,0.05)
	
	mc.spaceLocator(n = 'IndexLeftLoc1')
	fingerEnd = mc.getAttr('IndexLeftLoc3.tx')
	middlefingerRoot = mc.getAttr('IndexLeftLoc0.tx')
	
	halfmiddleFinger = middlefingerRoot + (fingerEnd - middlefingerRoot)*0.5
	mc.move(halfmiddleFinger,head*6.5,0)
	mc.scale(0.05,0.05,0.05)
	
	mc.spaceLocator(n = 'IndexLeftLoc2')
	fingerEnd = mc.getAttr('IndexLeftLoc3.tx')
	IndexLeftLoc1 = mc.getAttr('IndexLeftLoc1.tx')
	halfmiddleSecondFinger = IndexLeftLoc1 + (fingerEnd - IndexLeftLoc1)*0.5
	mc.move(halfmiddleSecondFinger,head*6.5,0)
	mc.scale(0.05,0.05,0.05)
			
	mc.select('IndexLeftLoc0','IndexLeftLoc1','IndexLeftLoc2','IndexLeftLoc3')
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
		mc.select('IndexLeftLoc0','IndexLeftLoc1','IndexLeftLoc2','IndexLeftLoc3')
		mc.duplicate()
		mc.move(0,0,-0.2*(i+1),r = True)

	for j in range(4):
		mc.rename('IndexLeftLoc' + str(j+4),'MiddleLeftLoc' + str(j))
	for j in range(4,8):
		mc.rename('IndexLeftLoc' + str(j+4),'RingLeftLoc' + str(j-4))
	for j in range(8,12):
		mc.rename('IndexLeftLoc' + str(j+4),'PinkieLeftLoc' + str(j-8))
	
	#thumb
	mc.select('IndexLeftLoc0','IndexLeftLoc1','IndexLeftLoc2')
	mc.duplicate()
	mc.move(0,0,0.2,r = True)
	for j in range(3):
		mc.rename('IndexLeftLoc' + str(j+4),'ThumbLeftLoc' + str(j))	
	for i in range(1,3):
		mc.parent('ThumbLeftLoc' +  str(3-i),'ThumbLeftLoc' +  str(2-i) )
	
	for each in ('PinkieLeft','RingLeft','MiddleLeft','IndexLeft'):
		for i in range(1,4):
			mc.parent(each + 'Loc' +  str(4-i),each + 'Loc' +  str(3-i) )

		
createLoc()







































