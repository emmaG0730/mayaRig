"""
module for making top rig structure and rig module 
"""

import maya.cmds as mc
from . import control

sceneObjectType = 'rig'



class Base():
    
    """
    class for building top rig structure
    """
    
    def __init__(
                 self,
                 characterName = 'XXX',
                 scale = 1.0,
                 mainCtrlAttachObj = '',
                 charcterHight = 180
                 ):
        
        """
        @param characterName: str, character name
        @param scale: float, general scale of the rig
        @return: None
        """
        
        self.topGrp = mc.group( n = characterName + '_rig_grp', em = 1 )
        self.rigGrp = mc.group( n = 'rig_grp', em = 1, p = self.topGrp )
        self.modelGrp = mc.group( n = 'model_grp', em = 1, p = self.topGrp )
        
        characterNameAt = 'characterName'
        sceneObjectTypeAt = 'sceneObjectType'
        
        for at in [ characterNameAt, sceneObjectTypeAt ]:
            
            mc.addAttr( self.topGrp, ln = at, dt = 'string' )
        
        mc.setAttr( self.topGrp + '.' + characterNameAt, characterName, type = 'string', l = 1 )
        mc.setAttr( self.topGrp + '.' + sceneObjectTypeAt, sceneObjectType, type = 'string', l = 1 )
        
        
        # make global control
        
        global1Ctrl = control.Control( 
                                     prefix = 'global1',
                                     scale = charcterHight / 3,
                                     parent = self.rigGrp,
                                     lockChannels = ['v']
                                     )
        
        global2Ctrl = control.Control( 
                                     prefix = 'global2',
                                     scale = charcterHight / 3.3,
                                     parent = global1Ctrl.C,
                                     lockChannels = ['s', 'v']
                                     )

        mc.addAttr( global1Ctrl.C, ln = 'pointerScale', at = 'float', k = 1,min=0.0, max=100.0, dv = 1.0 )
        mc.setAttr(global1Ctrl.C + '.pointerScale', k = 1)

        self._flattenGlobalCtrlShape( global1Ctrl.C )
        self._flattenGlobalCtrlShape( global2Ctrl.C )
        
        for axis in ['y', 'z']:
            
            mc.connectAttr( global1Ctrl.C + '.sx', global1Ctrl.C + '.s' + axis )
            mc.setAttr( global1Ctrl.C + '.s' + axis, k = 0 )
        
        
        # make more groups
        
        self.jointsGrp = mc.group( n = 'joints_grp', em = 1, p = global2Ctrl.C )
        self.modulesGrp = mc.group( n = 'modules_grp', em = 1, p = global2Ctrl.C )
        
        self.builderGrp = mc.group( n = 'builder_grp', em = 1, p = self.rigGrp )
        self.curveGrp = mc.group( n = 'curves_grp', em = 1, p = self.builderGrp )
        self.pointGrp = mc.group( n = 'points_grp', em = 1, p = self.builderGrp )
        self.locatorGrp = mc.group( n = 'locators_grp', em = 1, p = self.builderGrp )
        self.ctrlJointsGrp = mc.group( n = 'ctrlJoints_grp', em = 1, p = self.builderGrp )

        mc.setAttr( self.builderGrp + '.it', 0, l = 1 )
        

    def _adjustMainCtrlShape( self, ctrl, scale ):
        
        # adjust shape of main control
        
        ctrlShapes = mc.listRelatives( ctrl.C, s = 1, type = 'nurbsCurve' )
        cls = mc.cluster( ctrlShapes )[1]
        mc.setAttr( cls + '.ry', 90 )
        mc.delete( ctrlShapes, ch = 1 )
        
        mc.move( 8 * scale, ctrl.Off, moveY = True, relative = True )
        
        
        
    
    def _flattenGlobalCtrlShape( self, ctrlObject ):
        
        # flatten ctrl object shape
        
        ctrlShapes = mc.listRelatives( ctrlObject, s = 1, type = 'nurbsCurve' )
        cls = mc.cluster( ctrlShapes )[1]
        mc.setAttr( cls + '.rz', 90 )
        mc.delete( ctrlShapes, ch = 1 )

    
        
class Module():
    
    """
    class for building module rig structure
    """
    
    def __init__( 
                 self,
                 prefix = 'new',
                 baseObj = None
                 ):
        
        """
        @param prefix: str, prefix to name new objects
        @param baseObj: instance of base.module.Base class
        @return: None
        """
        
        self.topGrp = mc.group( n = prefix + 'Module_grp', em = 1 )
        
        self.controlsGrp = mc.group( n = prefix + 'Controls_grp', em = 1, p = self.topGrp )
        self.jointsGrp = mc.group( n = prefix + 'Joints_grp', em = 1, p = self.topGrp )
        self.partsGrp = mc.group( n = prefix + 'Parts_grp', em = 1, p = self.topGrp )
        self.partsNoTransGrp = mc.group( n = prefix + 'PartsNoTrans_grp', em = 1, p = self.topGrp )
        
        mc.hide( self.partsGrp, self.partsNoTransGrp )
        
        mc.setAttr( self.partsNoTransGrp + '.it', 0, l = 1 )
        
        # parent module
        
        if baseObj:
            
            mc.parent( self.topGrp, baseObj.modulesGrp )
        
        
        
