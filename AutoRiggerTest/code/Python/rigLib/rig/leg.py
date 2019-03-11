import maya.cmds as mc

def createFkJoints():
    mc.select(clear = 1)
    mc.duplicate('thigh_R_JNT', n = 'thigh_R_Fk_JNT')
    mc.parent('thigh_R_Fk_JNT',  w = 1)