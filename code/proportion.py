import maya.cmds as mc

head= 2
'''
foot_ankle = head*0.5
ankle_knee= head*1.5
knee_pelvis = head*2
pelvis_bellybutton= foot_ankle
bellybutton_neck = knee_pelvis
pelvis_neck = head*2.5
neck_head= foot_ankle
head=head
'''
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
	
	
	mc.spaceLocator(n = 'ElbowLoc')
	mc.move(head*2.5,head*6.5,0)
	mc.scale(0.2,0.2,0.2)
	mc.color(rgb=(0,0.2,0.5))
	
	mc.spaceLocator(n = 'WristLoc')
	mc.move(head*3.7,head*6.5,0)
	mc.scale(0.2,0.2,0.2)
	mc.color(rgb=(0,0.2,0.5))
	
	mc.spaceLocator(n = 'MiddleFingerEndLoc')
	mc.move(head*4.4,head*6.5,0)
	mc.scale(0.1,0.1,0.1)
	mc.color(rgb=(0,0.2,0.5))
	
	mc.spaceLocator(n = 'MiddlefingerRootLoc')
	fingerEnd = mc.getAttr('MiddleFingerEndLoc.tx')
	wrist = mc.getAttr('WristLoc.tx')
	halfhand = wrist+(fingerEnd - wrist)*0.5
	mc.move(halfhand,head*6.5,0)
	mc.scale(0.05,0.05,0.05)
	
	mc.spaceLocator(n = 'MiddleFingerMidLoc')
	fingerEnd = mc.getAttr('MiddleFingerEndLoc.tx')
	middlefingerRoot = mc.getAttr('MiddlefingerRootLoc.tx')
	halfmiddleFinger = middlefingerRoot + (fingerEnd - middlefingerRoot)*0.5
	mc.move(halfmiddleFinger,head*6.5,0)
	mc.scale(0.05,0.05,0.05)
	
	mc.spaceLocator(n = 'MiddleFingerSecondLoc')
	fingerEnd = mc.getAttr('MiddleFingerEndLoc.tx')
	middleFingerMidLoc = mc.getAttr('MiddleFingerMidLoc.tx')
	halfmiddleSecondFinger = middleFingerMidLoc + (fingerEnd - middleFingerMidLoc)*0.5
	mc.move(halfmiddleSecondFinger,head*6.5,0)
	mc.scale(0.05,0.05,0.05)
	
	
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
	
createLoc()
































































