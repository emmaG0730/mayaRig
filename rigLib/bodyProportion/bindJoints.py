import maya.cmds as mc

from . import point


armJntName = ['clavicle','shoulder','elbow','wrist']
legJntName = ['thigh','knee','ankle','ball','toe']


class BindJoints():

	def __init__(self):

		pL = point.Pointer()
		pList =  pL.pointerList
		pDict = pL.cvPositionDict 




		for curve, cvPositions in pDict.items():
			if 'arm' in cur
			mc.select(clear=True)
			mc.joint( n = GeoDic[0]+'_JNT',p = (position[0][0][0],position[0][0][1],position[0][0][2]), rad = 0.4)
			for i in range(1,17):
				mc.joint( n = GeoDic[i]+'_JNT',p = (GeoLocList[i][0],GeoLocList[i][1],GeoLocList[i][2]), rad = 0.4)
				mc.joint(GeoDic[i-1]+'_JNT',e= True, zso = True,oj='xyz',sao  ='yup',roo = 'zxy')




			mc.select(pointer)
			pointPos = mc.xform(q = 1,t = 1,ws = 1)
			mc.joint(n = str(pointer.split('_')[:2]) + 'B_jnt', p = (pointPos[0],pointPos[1],pointPos[2]))

