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

			topPositionList = self.pPDict[key]
	

			#mc.joint(n = rename.removeSuffix(value[0]) + '_JNT',  p = self.pPDict[key][0])
			for i in range(len(value)):#4

				Pos = mc.xform(value[i], q = 1, t = 1, ws = 1)

				Pos1 = self.pPDict[key][i]

				if Pos == Pos1:

					mc.joint( n = rename.removeSuffix(str(value[i])) + '_JNT', p = (topPositionList[i][0],topPositionList[i][1],topPositionList[i][2]))

				else:
					mc.joint( n = rename.removeSuffix(value[i]) + '_JNT', p = (Pos[0],Pos[1],Pos[2]))

				mc.joint(rename.removeSuffix(value[i]) + '_JNT', e= True, zso = True, oj='xyz', sao  ='xup', roo = 'zxy')

			mc.parent(rename.removeSuffix(value[0]) + '_JNT' , tempGrp)

		topJoints = mc.listRelatives(tempGrp,c = 1)
		
		for each in topJoints:
			if 'R' in each :
				mc.select(each)
				mc.mirrorJoint(mirrorYZ = True,mirrorBehavior = True,searchReplace = ('R', 'L'))

		for p in mc.ls(type = 'transform'):
			if 'Pointer' in p:
				mc.hide(p)




