import maya.cmds as mc

def jointHierarchy(topJnt, withEndJnt = True):
    '''
    create a joint chain
    '''

    jointChain = mc.listRelatives(topJnt, type = 'joint', ad = 1)
    jointChain.append(topJnt)
    jointChain.reverse()

    wholeChain = jointChain[:]
    if not withEndJnt:
        wholeChain = [j for j in jointChain if mc.listRelatives(j, type = 'joint', ch = 1)]

    return wholeChain

