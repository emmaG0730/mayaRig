"""
main project file with central variables
"""


def listDirection():

    relativeDir = __file__

    print 'relativeDir : ' + str(relativeDir)

    dirList = relativeDir.split('\\')[:-5]

    headDir =  '\\'.join(dirList)

    return headDir



bodyCurvePath = listDirection() + '\\asset\\body_curve.ma'
pointPath = listDirection() + '\\asset\\pointer.ma'
poleCtrl = listDirection() + '\\asset\\poleControl.ma'



bodyCurves = ['arm_R_','leg_R_','head_','spine_','thumb_R_','index_R_','middle_R_','ring_R_','pinky_R_']

armJntName = ['clavicle','shoulder','elbow','wrist']
legJntName = ['thigh','knee','ankle','ball','toe']