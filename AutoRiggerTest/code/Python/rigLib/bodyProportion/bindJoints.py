import maya.cmds as mc
from . import point
from ..base import project
from ..utils import rename


curveName = project.bodyCurves

'''
def BindJoints():

	#initialize point Pointer class
	pointInstance = point.Pointer()

	#find top point and its position

	pPDict = pointInstance.cvPositionDict
	pNDict = pointInstance.pointNameDict
	#tPList = pointInstance.topPointList


	tempGrp = mc.group(n = 'temp_grp', em = 1)


	#query every point position and name create joints
	for key, value in pNDict.items():

		mc.select(clear=True)
		topNameList = pNDict[key]
		topPositionList = pPDict[key]

		mc.joint(n = rename.removeSuffix(topNameList[0]) + '_JNT',  p = pPDict[key][0])
		for i in range(1, len(topNameList)):#4
			mc.joint( n = rename.removeSuffix(topNameList[i]) + '_JNT', p = (topPositionList[i][0],topPositionList[i][1],topPositionList[i][2]))
			mc.joint(rename.removeSuffix(topNameList[i-1]) + '_JNT', e= True, zso = True, oj='xyz', sao  ='xup', roo = 'zxy')

		mc.parent(rename.removeSuffix(topNameList[0]) + '_JNT' , tempGrp)

	topJoints = mc.listRelatives(tempGrp,c = 1)
	
	for each in topJoints:
		if 'R' in each :
			mc.select(each)
			mc.mirrorJoint(mirrorYZ = True,mirrorBehavior = True,searchReplace = ('R', 'L'))

	for p in mc.ls(type = 'transform'):
		if 'Pointer' in p:
			mc.hide(p)



	mc.parent('clavicle_R_JNT', 'spine_5_JNT')	
	mc.parent('clavicle_L_JNT', 'spine_5_JNT')
	mc.parent('head_1_JNT', 'spine_5_JNT')	

	mc.parent('thigh_R_JNT', 'spine_1_JNT')
	mc.parent('thigh_L_JNT', 'spine_1_JNT')

	mc.parent('thumb_R_1_JNT', 'wrist_R_JNT')
	mc.parent('index_R_1_JNT', 'wrist_R_JNT')
	mc.parent('middle_R_1_JNT', 'wrist_R_JNT')
	mc.parent('ring_R_1_JNT', 'wrist_R_JNT')
	mc.parent('pinky_R_1_JNT', 'wrist_R_JNT')

	mc.parent('thumb_L_1_JNT', 'wrist_L_JNT')
	mc.parent('index_L_1_JNT', 'wrist_L_JNT')
	mc.parent('middle_L_1_JNT', 'wrist_L_JNT')
	mc.parent('ring_L_1_JNT', 'wrist_L_JNT')
	mc.parent('pinky_L_1_JNT', 'wrist_L_JNT')

for partCurve_index in range(len(bodyCurves)):

	partCurveCVs = mc.ls( bodyCurve + '.cv[*]', fl = 1 )	

	for partCV_index in range(len( partCurveCVs )):


'''


class BindJoints():

	def __init__(self):

		#initialize point Pointer class
		self.pointInstance = point.Pointer()

		#find point name and position
		self.pPDict = self.pointInstance.cvPositionDict
		self.pNDict = self.pointInstance.pointNameDict

		

	def _createJoints(self):

		#creat an empty temp group
		tempGrp = mc.group(n = 'temp_grp', em = 1)

		#query every point position and name create joints
		for key, value in self.pNDict.items():

			mc.select(clear=True)

			topPointPos = mc.xform(value[0], q = 1, t = 1, ws = 1)

			print topPointPos

			mc.joint(n = rename.removeSuffix(value[0]) + '_JNT',  p = (topPointPos[0], topPointPos[1], topPointPos[2]))

			for i in range(1, len(value)):#4

				Pos = mc.xform(value[i], q = 1, t = 1, ws = 1)

				mc.joint( n = rename.removeSuffix(value[i]) + '_JNT', p = (Pos[0],Pos[1],Pos[2]))

				mc.joint(rename.removeSuffix(value[i - 1]) + '_JNT', e= True, ch = 1, zso = True, oj = 'xyz', sao  = 'yup', roo = 'zxy')

			mc.parent(rename.removeSuffix(value[0]) + '_JNT' , tempGrp)

			for axis in ['X','Y','Z']:

				mc.setAttr( rename.removeSuffix(value[-1]) + '_JNT.jointOrient' + axis, 0)
			

		mc.parent('knee_R_JNT', 'ankle_R_JNT', 'spine_3_JNT' ,'spine_4_JNT' ,'head_3_JNT', w = 1)

		mc.setAttr('thigh_R_JNT.jointOrientX', 90)
		mc.setAttr('knee_R_JNT.jointOrientX', 90)
		mc.setAttr('spine_3_JNT.jointOrientX', -90)
		mc.setAttr('spine_4_JNT.jointOrientX', -90)
		mc.setAttr('head_3_JNT.jointOrientX', -90)

		mc.parent('head_3_JNT' , 'head_2_JNT')
		mc.parent('spine_3_JNT' , 'spine_2_JNT')
		mc.parent('spine_4_JNT' , 'spine_3_JNT')
		mc.parent('knee_R_JNT' , 'thigh_R_JNT')
		mc.parent('ankle_R_JNT' , 'knee_R_JNT')
		
		topJoints = mc.listRelatives(tempGrp, c = 1)
			
		for each in topJoints:
			if 'R' in each :
				mc.select(each)
				mc.mirrorJoint(mirrorYZ = True,mirrorBehavior = True,searchReplace = ('R', 'L'))

		for p in mc.ls(type = 'transform'):
			if 'Pointer' in p:
				mc.hide(p)

		mc.parent('clavicle_R_JNT', 'spine_5_JNT')	
		mc.parent('clavicle_L_JNT', 'spine_5_JNT')
		mc.parent('head_1_JNT', 'spine_5_JNT')	

		mc.parent('thigh_R_JNT', 'spine_1_JNT')
		mc.parent('thigh_L_JNT', 'spine_1_JNT')

		mc.parent('thumb_R_1_JNT', 'wrist_R_JNT')
		mc.parent('index_R_1_JNT', 'wrist_R_JNT')
		mc.parent('middle_R_1_JNT', 'wrist_R_JNT')
		mc.parent('ring_R_1_JNT', 'wrist_R_JNT')
		mc.parent('pinky_R_1_JNT', 'wrist_R_JNT')

		mc.parent('thumb_L_1_JNT', 'wrist_L_JNT')
		mc.parent('index_L_1_JNT', 'wrist_L_JNT')
		mc.parent('middle_L_1_JNT', 'wrist_L_JNT')
		mc.parent('ring_L_1_JNT', 'wrist_L_JNT')
		mc.parent('pinky_L_1_JNT', 'wrist_L_JNT')


		mc.select(clear=True)
		mc.joint(n = 'Trajectory_JNT' , p = (0,0,0))
		mc.parent( 'spine_1_JNT' , 'Trajectory_JNT')




