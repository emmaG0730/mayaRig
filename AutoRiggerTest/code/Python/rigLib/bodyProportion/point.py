import maya.cmds as mc
from ..base import module
from ..base import project

pathSet = project.listDirection()

bodyCurvePath = pathSet[0]  
pointPath = pathSet[1]

class Pointer():

	def __init__(self):

		self.pointNameDict = {}
		self.cvPositionDict = {}
		self.topPointList = []

		mc.file(bodyCurvePath, i = 1)
		mc.file(pointPath, i = 1) 

		baseGrp  = module.Base()
		bodyCurves = project.bodyCurves
		armJntName = project.armJntName
		legJntName = project.legJntName


		for partCurve_index in range(len(bodyCurves)):
			bodyCurve = str(mc.ls(bodyCurves[partCurve_index])[0]) 
			partCurveCVs = mc.ls( bodyCurve + '.cv[*]', fl = 1 )			

			clusterGrp = mc.group(n = bodyCurve, em = 1)	

			self.pointNameDict[bodyCurve] = []
			self.cvPositionDict[bodyCurve] = []

			currentCurvePositionList = []

			parentBool = True
			clusterList = []

			
			for partCV_index in range(len( partCurveCVs )):
			
				cvPos = mc.xform(partCurveCVs[partCV_index], q = 1, t = 1, ws = 1)
				currentCurvePositionList.append(cvPos)

				cluster = mc.cluster( partCurveCVs[partCV_index], n = bodyCurve + 'Cluster%d' % ( partCV_index + 1 ) )[1]
				clusterList.append(cluster)
				jointPointer = mc.duplicate('pointer')


				if 'arm' in bodyCurve: #'arm_R_'
					renamedPo = mc.rename(jointPointer, armJntName[partCV_index] + '_' + bodyCurve.split('_')[1] + '_' + 'Pointer')
					self.pointNameDict[bodyCurve].append(renamedPo)
				

				elif 'leg' in bodyCurve:
					renamedPo = mc.rename(jointPointer, legJntName[partCV_index] + '_' + bodyCurve.split('_')[1] + '_' + 'Pointer')
					self.pointNameDict[bodyCurve].append(renamedPo)

				else:
					renamedPo = mc.rename(jointPointer, bodyCurve + '%d_Pointer' % ( partCV_index + 1 ))
					self.pointNameDict[bodyCurve].append(renamedPo)
					
				if parentBool == False:
					mc.parent(self.pointNameDict[bodyCurve][partCV_index], self.pointNameDict[bodyCurve][partCV_index - 1],  relative=True )


				mc.delete(mc.pointConstraint(cluster, renamedPo, mo = 0))
				mc.parentConstraint(renamedPo, cluster, mo = 1)
				mc.hide(cluster) 
				mc.parent(cluster,baseGrp.curveGrp)

				parentBool = False
				
				
			self.topPointList.append(self.pointNameDict[bodyCurve][0])
						
			mc.parent(clusterGrp, baseGrp.locatorGrp)

			self.cvPositionDict[bodyCurve] = currentCurvePositionList
		
		print 'topPointList : ' + str(self.topPointList)
		print 'pointNameDict : ' + str(self.pointNameDict)
		print 'cvPositionDict : ' + str(self.cvPositionDict) 

		
		

		mc.parent('bodyCurve','pointer',baseGrp.curveGrp)
		mc.hide('pointer')
		mc.setAttr('bodyCurve.template', 1)
		mc.setAttr('bodyCurve.it', 0)
		mc.parent(self.topPointList, baseGrp.pointGrp)

		for axis in ['x','y', 'z']: 
			mc.connectAttr( 'global1_ctl.pointerScale', 'builder_grp.s' + axis)


		for each in ['thumb_R_1_Pointer', 'index_R_1_Pointer', 'middle_R_1_Pointer', 'ring_R_1_Pointer', 'pinky_R_1_Pointer']:
			mc.parent(each, 'wrist_R_Pointer')











