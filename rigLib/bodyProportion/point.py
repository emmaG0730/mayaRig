import maya.cmds as mc
from ..base import module

bodyCurvePath = 'C:\\AutoRiggerTest\\asset\\body_curve.ma'
pointPath = 'C:\\AutoRiggerTest\\asset\\pointer.ma'


class Pointer():

	def __init__(self):

		self.pointerList = []
		self.pointNameDict = {}
		self.cvPositionDict = {}

		mc.file(bodyCurvePath, i = 1)
		mc.file(pointPath, i = 1) 

		baseGrp  = module.Base()

		self.pointNameDict = {}

		#pointNameDict['arm_R_'] = []

		bodyCurves = ['arm_R_','arm_L_','leg_R_','leg_L_','head_','spine_',
					'thumb_L_','index_L_','middle_L_','ring_L_','pinky_L_',
					'thumb_R_','index_R_','middle_R_','ring_R_','pinky_R_']

		armJntName = ['clavicle','shoulder','elbow','wrist']
		legJntName = ['thigh','knee','ankle','ball','toe']

		'''
		{'arm_R_': ['clavicle_R','shoulder_R','elbow_R','wrist_R'], 'arm_L_' : ['clavicle_L','shoulder_L','elbow_L','wrist_L'], 
		'leg_R_' : ['thigh_R','knee_R','ankle_R','ball_R','toe_R'], 'leg_L_' : ['thigh_L','knee_L','ankle_L','ball_L','toe_L'],
		'head_' : ['head_1','head_2', 'head_3', 'head_4'] , 'thumb_L_' : ['thumb_L_1','thumb_L_2','thumb_L_3','thumb_L_4']}
		'''

		curvesPositionList = []

		for partCurve_index in range(len(bodyCurves)):
			bodyCurve = str(mc.ls(bodyCurves[partCurve_index])[0]) 
			partCurveCVs = mc.ls( bodyCurve + '.cv[*]', fl = 1 )	
			clusterGrp = mc.group(n = bodyCurve, em = 1)	
			self.pointNameDict[bodyCurve] = []


			currentCurvePositionList = []

			for partCV_index in range(len( partCurveCVs )):

				cvPos = mc.xform(partCurveCVs[partCV_index], q = 1, t = 1, ws = 1)
				currentCurvePositionList.append(cvPos)

				cluster = mc.cluster( partCurveCVs[partCV_index], n = bodyCurve + 'Cluster%d' % ( partCV_index + 1 ) )[1]
				jointPointer = mc.duplicate('pointer')



				if 'arm' in bodyCurve:
					renamedPo = mc.rename(jointPointer, armJntName[partCV_index] + '_' + bodyCurve.split('_')[1] + '_' + 'Pointer')
					self.pointNameDict[bodyCurve].append(renamedPo)
				

				elif 'leg' in bodyCurve:
					renamedPo = mc.rename(jointPointer, legJntName[partCV_index] + '_' + bodyCurve.split('_')[1] + '_' + 'Pointer')
					self.pointNameDict[bodyCurve].append(renamedPo)

				else:
					renamedPo = mc.rename(jointPointer, bodyCurve + '%d_Pointer' % ( partCV_index + 1 ))
					self.pointNameDict[bodyCurve].append(renamedPo)

				


				mc.delete(mc.pointConstraint(cluster, renamedPo))
				mc.parent(cluster ,renamedPo)
				mc.hide(cluster) 
				mc.parent(renamedPo, clusterGrp)


			mc.parent(clusterGrp, baseGrp.locatorGrp)

			self.cvPositionDict[bodyCurve] = []

			self.cvPositionDict[bodyCurve] = currentCurvePositionList

		print self.cvPositionDict
		print self.pointNameDict

		mc.parent('bodyCurve','pointer',baseGrp.curveGrp)
		mc.hide('pointer')
		mc.setAttr('bodyCurve.template', 1)
		mc.setAttr('bodyCurve.it', 0)

		for axis in ['x','y', 'z']: 
			mc.connectAttr( 'global1_ctl.pointerScale', 'builder_grp.s' + axis)

		mc.connectAttr( 'global1_ctl.pointerScale', 'global1_ctl.sx')







