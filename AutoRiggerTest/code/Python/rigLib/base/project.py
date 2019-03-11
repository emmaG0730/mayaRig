"""
main project file with central variables
"""

import os

def listDirection():

    relativeDir = __file__

    dirList = relativeDir.split('\\')[:-5]

    headDir =  '\\'.join(dirList)

    bodyCurvePath = headDir + '\\asset\\body_curve.ma'
    pointPath = headDir + '\\asset\\pointer.ma'

    return bodyCurvePath, pointPath

bodyCurves = ['arm_R_','leg_R_','head_','spine_','thumb_R_','index_R_','middle_R_','ring_R_','pinky_R_']

armJntName = ['clavicle','shoulder','elbow','wrist']
legJntName = ['thigh','knee','ankle','ball','toe']