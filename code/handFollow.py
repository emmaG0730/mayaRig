import maya.cmds as mc

handFollowHip = mc.getAttr('hand.follow_hip')
handFollowHead = mc.getAttr('hand.follow_head')

if (handFollowHip == 0 and handFollowHead == 0):
	mc.select('hand')
	handT = mc.xform(q= True,ws =True,t=True)
	handRo = mc.xform(q= True,ws =True,ro=True)
	mc.setAttr('hand_ctrl_parentConstraint1.hipW1', 0)
	mc.setAttr('hand_ctrl_parentConstraint1.headW0', 0)
	print handT[0],handT[1],handT[2]

	mc.xform(ws = True,t= (handT[0],handT[1],handT[2]))
	mc.xform(ws = True,ro =(handRo[0],handRo[1],handRo[2]))
	
elif handFollowHip == 1 and handFollowHead == 0:
	mc.select('hip')
	hipT1 = mc.xform(q=True,ws =True,t=True)
	hipRo = mc.xform(q=True,ws =True,ro=True)
	
	mc.setAttr('hand_ctrl_parentConstraint1.hipW1',1)
	mc.setAttr('hand_ctrl_parentConstraint1.headW0', 0)
	
	mc.select('hand')
	mc.xform(ws=True,t=(hipT[0],hipT[1],hipT[2]))
	mc.xform(ws=True,ro=(hipRo[0],hipRo[1],hipRo[2]))
	
elif handFollowHip == 0 and handFollowHead == 1:
	mc.select('head')
	headT1 = mc.xform(q=True,ws =True,t=True)
	headRo = mc.xform(q=True,ws =True,ro=True)
	
	mc.setAttr('hand_ctrl_parentConstraint1.hipW1',0)
	mc.setAttr('hand_ctrl_parentConstraint1.headW0', 1)
	
	mc.select('hand')
	mc.xform(ws=True,t=(headT1[0],headT1[1],headT1[2]))
	mc.xform(ws=True,ro=(headRo[0],headRo[1],headRo[2]))
	
	
	
	
	
	