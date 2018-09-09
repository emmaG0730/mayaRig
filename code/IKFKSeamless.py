import maya.cmds as mc
ikfkSwitch = mc.getAttr('Switch.IK_FK')
if ikfkSwitch == 1:
	mc.select('FK3_joint')
	wp= mc.xform(q=True,ws=True,t=True)
	wr= mc.xform(q=True,ws=True,ro=True)
	
	mc.select('IKhand')
	mc.xform(ws=True,t=(wp[0],wp[1],wp[2]))
	mc.xform(ws=True,ro=(wr[0],wr[1],wr[2]))
	
	mc.select('fakePole')
	fpt=mc.xform(q=True,ws=True,t=True)
	fpr=mc.xform(q=True,ws=True,ro=True)
	
	mc.select('Pole')
	mc.xform(ws=True,t=(fpt[0],fpt[1],fpt[2]))
	mc.xform(ws=True,ro=(fpr[0],fpr[1],fpr[2]))