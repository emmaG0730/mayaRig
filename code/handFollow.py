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
	
elif handFollowHip == 1:
	mc.select('hip')
	hipT = mc.xform(q=True,ws =True,t=True)
	hipRo = mc.xform(q=True,ws =True,ro=True)
	mc.setAttr('hand_ctrl_parentConstraint1.hipW1',1)
	mc.setAttr('hand_ctrl_parentConstraint1.headW0', 0)
	
	mc.select('hand')
	print handT[0],handT[1],handT[2]
	mc.xform(ws=True,t=(hipT[0],hipT[1],hipT[2]))
	mc.xform(ws=True,ro=(hipRo[0],hipRo[1],hipRo[2]))