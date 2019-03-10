import maya.cmds as mc
from base import module


def build(chainJnt, chainCurve, prefix = '', baseRig = None, rigScale = 1.0,):
    '''
    @chainJnt : list, list of a joint chain
    @chainCurve : string, the ik chain curve name
    @baseRig : instance of base.module.Base class
    '''

    #make instance of module
    rigModule = module.Base(characterName = 'Test')

    #make chain curve cluster
    chainCurveCVs = mc.ls(chainCurve + '.cv[*]', fl = 1 )
    numChainCV = len(chainCurveCVs)
    chainCurveClusters = []

    #make cluster of that chain curve
    for cvIndex in range(numChainCV):
        clusters = mc.cluster(chainCurveCVs[cvIndex], n = prefix + 'Cluster%d' % (cvIndex + 1))[1]
        chainCurveClusters.append(clusters)

    mc.hide(chainCurveClusters)

    #parent chainCurve
    mc.parent(chainCurve, rigModule.partGrp)

    #make ik handle
    ikChain = mc.ikhandle( n = prefix + '_ikHandle', sol = 'ikSplineSolver',sj = chainJnt[0], ee = chainJnt[-1],
                            c = chainCurve, ccv = 0, parentCurve = 0)[0]

    mc.hide(ikChain)
    mc.parent(ikChain, rigModule.partGrp)

    #make advanced twist
    



