import maya.cmds as mc
from ..utils import rename

from ..base import module
'''
create control joints for geo ,include IK FK
'''


def setCtrlJoints(jointName, ctrlType = '', scale = 1.0):

    #clear selection 
    mc.select(clear = 1)

    newJoints = mc.duplicate(jointName, rc = 1)
    mc.delete(newJoints[3:])

    #get the first 3 joints after duplicated
    ctrlJoints = newJoints[:3]


    ctrlJointsNewName = []

    #rename them
    for joint in ctrlJoints:

        print joint

        ctrlJointName = rename.insertLetters(joint[:-1], 2, ctrlType)

        mc.rename(joint, ctrlJointName)
        mc.joint(ctrlJointName ,e = 1, rad = scale )
        
        ctrlJointsNewName.append(ctrlJointName)

    if ctrlType == 'IK':
        mc.ikHandle(n = rename.removeSuffix(jointName) + '_ikHandle' , 
                        sj = ctrlJointsNewName[0] , ee = ctrlJointsNewName[2] )


    mc.parent(ctrlJointsNewName[0], 'ctrlJoints_grp')


