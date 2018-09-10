file -f -new;
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// untitled // 
doOpenFile ("F:/GitHub/tools/mayaRig/armPractise2_IKFKSeamless.ma");
file -f -options "v=0;"  -ignoreVersion  -typ "mayaAscii" -o "F:/GitHub/tools/mayaRig/armPractise2_IKFKSeamless.ma";addRecentFile("F:/GitHub/tools/mayaRig/armPractise2_IKFKSeamless.ma", "mayaAscii");
closeAllNodeEditors;
closeHypershade;
updateRenderOverride;
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
// File read in  0.2 seconds.
optionVar -sv colorManagementColorPickerColorSpaceSelection "Rendering Space";
optionVar -iv colorManagementColorPickerColorMgtEnabled 1;
commandPort -securityWarning -name commandportDefault;
// Error: line 1: Could not open command port commandportDefault because that name is in use. // 
// AbcBullet v1.0 using Alembic 1.5.4 (built May  8 2014 13:47:10)
// BifrostMain plug-in loaded (built Feb 26 2015 18:01:51)
// XMD Maya Import (C) NaturalMotion 2016 - build 5.0.2.0 - [Mar 21 2016:16:39:43]
// XMD Maya Exporter (C) NaturalMotion 2016 - build 5.0.2.0 - [Mar 21 2016:16:39:43]
// cgfxShader 4.5 for Maya 2016.0 (Feb 26 2015)
// AbcExport v1.0 using Alembic 1.5.4 (built May  8 2014 13:47:10)
// AbcImport v1.0 using Alembic 1.5.4 (built May  8 2014 13:47:10)
updateRendererUI;
select -r Switch ;
select -r FK1_Ctrl ;
rotate -r -os -fo 0 -53.663271 0 ;
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
select -r locator1 ;
doDelete;
select -r IKhand ;
move -r 0 1.315063 0 ;
move -r 0 0 1.575509 ;
move -r 0 3.316322 2.174119 ;
rotate -r -os -fo -45.528081 0 0 ;
select -r Pole ;
move -r 0 0 0.846362 ;
move -r 0 2.964097 0.835796 ;
select -r IK1_joint ;
select -r IK1_joint ;
select -r IK1_joint ;
select -r FK1_joint ;
select -r Switch ;
setAttr "Switch.IK_FK" 0;
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
    mc.select('FK1_joint')
    mc.xform(ws=True,ro=(IK1_joint_ro[0],IK1_joint_ro[1],IK1_joint_ro[2]))
    
    
select -r FK1_Ctrl ;
// Undo: select -r FK1_Ctrl  // 
// Undo: cmdScrollFieldExecuter -e -executeAll scriptEditorPanel1Window|TearOffPane|scriptEditorPanel1|formLayout87|formLayout89|paneLayout2|paneLayout3|tabLayout2|formLayout92|cmdScrollFieldExecuter3 // 
select -r FK1_Ctrl ;
select -r FK1_Ctrl ;
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
    
    
// Undo: cmdScrollFieldExecuter -e -executeAll scriptEditorPanel1Window|TearOffPane|scriptEditorPanel1|formLayout87|formLayout89|paneLayout2|paneLayout3|tabLayout2|formLayout92|cmdScrollFieldExecuter3 // 
select -r FK2_Ctrl ;
select -r IK3_joint ;
select -r FK3_Ctrl ;
select -cl  ;
select -r Switch ;
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
select -r IKhand ;
select -r fakePole ;
move -r 0 0 0.431143 ;
// Undo: move -r 0 0 0.431143  // 
select -r Pole ;
select -r fakePole ;
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
