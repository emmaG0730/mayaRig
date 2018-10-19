
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

ikfkSwitch = mc.getAttr('Switch.IK_FK')
if ikfkSwitch == 1 :
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
elif ikfkSwitch == 0 : 
    mc.select('IK1_joint')
    IK1_joint_ro = mc.xform(q=True,ws=True,ro=True)
    mc.select('FK1_joint')
    mc.xform(ws=True,ro=(IK1_joint_ro[0],IK1_joint_ro[1],IK1_joint_ro[2]))
    
    

import maya.cmds as mc
ikfkSwitch = mc.getAttr('Switch.IK_FK')
if ikfkSwitch == 1 :
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
elif ikfkSwitch == 0 : 
    mc.select('IK1_joint')
    IK1_joint_ro = mc.xform(q=True,ws=True,ro=True)
    mc.select('FK1_Ctrl')
    mc.xform(ws=True,ro=(IK1_joint_ro[0],IK1_joint_ro[1],IK1_joint_ro[2]))
    
    

import maya.cmds as mc
ikfkSwitch = mc.getAttr('Switch.IK_FK')
if ikfkSwitch == 1 :
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
elif ikfkSwitch == 0 : 
    mc.select('IK1_joint')
    IK1_joint_ro = mc.xform(q=True,ws=True,ro=True)
    mc.select('FK1_Ctrl')
    mc.xform(ws=True,ro=(IK1_joint_ro[0],IK1_joint_ro[1],IK1_joint_ro[2]))
    
    mc.select('IK2_joint')
    IK2_joint_ro = mc.xform(q=True,ws=True,ro=True)
    mc.select('FK2_Ctrl')
    mc.xform(ws=True,ro=(IK2_joint_ro[0],IK2_joint_ro[1],IK2_joint_ro[2]))
    
    mc.select('IK3_joint')
    IK3_joint_ro = mc.xform(q=True,ws=True,ro=True)
    mc.select('FK3_Ctrl')
    mc.xform(ws=True,ro=(IK3_joint_ro[0],IK3_joint_ro[1],IK3_joint_ro[2]))

import maya.cmds as mc
ikfkSwitch = mc.getAttr('Switch.IK_FK')
if ikfkSwitch == 1 :
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
elif ikfkSwitch == 0 : 
    mc.select('IK1_joint')
    IK1_joint_ro = mc.xform(q=True,ws=True,ro=True)
    mc.select('FK1_Ctrl')
    mc.xform(ws=True,ro=(IK1_joint_ro[0],IK1_joint_ro[1],IK1_joint_ro[2]))
    
    mc.select('IK2_joint')
    IK2_joint_ro = mc.xform(q=True,ws=True,ro=True)
    mc.select('FK2_Ctrl')
    mc.xform(ws=True,ro=(IK2_joint_ro[0],IK2_joint_ro[1],IK2_joint_ro[2]))
    
    mc.select('IK3_joint')
    IK3_joint_ro = mc.xform(q=True,ws=True,ro=True)
    mc.select('FK3_Ctrl')
    mc.xform(ws=True,ro=(IK3_joint_ro[0],IK3_joint_ro[1],IK3_joint_ro[2]))
    
    mc.select('Pole')
    fakePole_t = mc.xform(q=True,ws=True,t=True)
    fakePole_ro = mc.xform(q=True,ws=True,ro=True)
    
    mc.select('fakePole')
    mc.xform(ws=True,t=(fakePole_t[0],fakePole_t[1],fakePole_t[2]))
    mc.xform(ws=True,ro=(fakePole_ro[0],fakePole_ro[1],fakePole_ro[2]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
select -r IKhand ;
import maya.cmds as mc
ikfkSwitch = mc.getAttr('Switch.IK_FK')
if ikfkSwitch == 1 :
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
elif ikfkSwitch == 0 : 
    mc.select('IK1_joint')
    IK1_joint_ro = mc.xform(q=True,ws=True,ro=True)
    mc.select('FK1_Ctrl')
    mc.xform(ws=True,ro=(IK1_joint_ro[0],IK1_joint_ro[1],IK1_joint_ro[2]))
    
    mc.select('IK2_joint')
    IK2_joint_ro = mc.xform(q=True,ws=True,ro=True)
    mc.select('FK2_Ctrl')
    mc.xform(ws=True,ro=(IK2_joint_ro[0],IK2_joint_ro[1],IK2_joint_ro[2]))
    
    mc.select('IKhand')
    IK3_joint_ro = mc.xform(q=True,ws=True,ro=True)
    mc.select('FK3_Ctrl')
    mc.xform(ws=True,ro=(IK3_joint_ro[0],IK3_joint_ro[1],IK3_joint_ro[2]))
    
    mc.select('Pole')
    fakePole_t = mc.xform(q=True,ws=True,t=True)
    fakePole_ro = mc.xform(q=True,ws=True,ro=True)
    
    mc.select('fakePole')
    mc.xform(ws=True,t=(fakePole_t[0],fakePole_t[1],fakePole_t[2]))
    mc.xform(ws=True,ro=(fakePole_ro[0],fakePole_ro[1],fakePole_ro[2]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
// Undo: cmdScrollFieldExecuter -e -executeAll scriptEditorPanel1Window|TearOffPane|scriptEditorPanel1|formLayout87|formLayout89|paneLayout2|paneLayout3|tabLayout2|formLayout92|cmdScrollFieldExecuter3 // 
select -r FK3_Ctrl ;
import maya.cmds as mc
ikfkSwitch = mc.getAttr('Switch.IK_FK')
if ikfkSwitch == 1 :
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
elif ikfkSwitch == 0 : 
    mc.select('IK1_joint')
    IK1_joint_ro = mc.xform(q=True,ws=True,ro=True)
    mc.select('FK1_Ctrl')
    mc.xform(ws=True,ro=(IK1_joint_ro[0],IK1_joint_ro[1],IK1_joint_ro[2]))
    
    mc.select('IK2_joint')
    IK2_joint_ro = mc.xform(q=True,ws=True,ro=True)
    mc.select('FK2_Ctrl')
    mc.xform(ws=True,ro=(IK2_joint_ro[0],IK2_joint_ro[1],IK2_joint_ro[2]))
    
    mc.select('IKhand')
    IK3_joint_ro = mc.xform(q=True,ws=True,ro=True)
    mc.select('FK3_Ctrl')
    mc.xform(ws=True,ro=(IK3_joint_ro[0],IK3_joint_ro[1],IK3_joint_ro[2]))
    
    mc.select('Pole')
    fakePole_t = mc.xform(q=True,ws=True,t=True)
    fakePole_ro = mc.xform(q=True,ws=True,ro=True)
    
    mc.select('fakePole')
    mc.xform(ws=True,t=(fakePole_t[0],fakePole_t[1],fakePole_t[2]))
    mc.xform(ws=True,ro=(fakePole_ro[0],fakePole_ro[1],fakePole_ro[2]))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
select -r Switch ;
