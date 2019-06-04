from PySide import QtCore
from PySide import QtGui
from shiboken import wrapInstance

import maya.cmds as mc
import maya.OpenMayaUI as omui

dialog = None

def maya_main_window():
	"""
	Return the Maya main window widget as a Python object
	"""
	main_window_ptr = omui.MQtUtil.mainWindow()
	return wrapInstance(long(main_window_ptr), QtGui.QWidget)

characterJointsName = ['b_L_ankle_v1_JNT', 'b_L_axe_v1_JNT', 'b_L_ball_v1_JNT', 'b_L_bladeShell_v1_JNT', 'b_L_blade_v1_JNT', 'b_L_clavicle_v1_JNT', 'b_L_dagger_v1_JNT', 'b_L_elbow_v1_JNT', 'b_L_hip_v1_JNT', 'b_L_index1_v1_JNT', 'b_L_index2_v1_JNT', 'b_L_index3_v1_JNT', 'b_L_knee_v1_JNT', 'b_L_longBow_v1_JNT', 'b_L_lowerArmLowerTwist_v1_JNT', 'b_L_lowerArmUpperTwist_v1_JNT', 'b_L_middle1_v1_JNT', 'b_L_middle2_v1_JNT', 'b_L_middle3_v1_JNT', 'b_L_pinky1_v1_JNT', 'b_L_pinky2_v1_JNT', 'b_L_pinky3_v1_JNT', 'b_L_ring1_v1_JNT', 'b_L_ring2_v1_JNT', 'b_L_ring3_v1_JNT', 'b_L_shield_v1_JNT', 'b_L_shoulderPad_v1_JNT', 'b_L_shoulder_v1_JNT', 'b_L_thumb1_v1_JNT', 'b_L_thumb2_v1_JNT', 'b_L_thumb3_v1_JNT', 'b_L_toe_v1_JNT', 'b_L_upperArmLowerTwist_v1_JNT', 'b_L_upperArmUpperTwist_v1_JNT', 'b_L_upperLegLowerTwist_v1_JNT', 'b_L_upperLegUpperTwist_v1_JNT', 'b_L_wrist_v1_JNT', 'b_M_breath_v1_JNT', 'b_M_head_v1_JNT', 'b_M_neck_v1_JNT', 'b_M_origin_v1_JNT', 'b_M_pelvis_v1_JNT', 'b_M_spine1_v1_JNT', 'b_M_spine2_v1_JNT', 'b_M_spine3_v1_JNT', 'b_M_trajectory_v1_JNT', 'b_R_ankle_v1_JNT', 'b_R_axe_v1_JNT', 'b_R_ball_v1_JNT', 'b_R_bladeShell_v1_JNT', 'b_R_blade_v1_JNT', 'b_R_clavicle_v1_JNT', 'b_R_dagger_v1_JNT', 'b_R_elbow_v1_JNT', 'b_R_hip_v1_JNT', 'b_R_index1_v1_JNT', 'b_R_index2_v1_JNT', 'b_R_index3_v1_JNT', 'b_R_knee_v1_JNT', 'b_R_lowerArmLowerTwist_v1_JNT', 'b_R_lowerArmUpperTwist_v1_JNT', 'b_R_middle1_v1_JNT', 'b_R_middle2_v1_JNT', 'b_R_middle3_v1_JNT', 'b_R_pinky1_v1_JNT', 'b_R_pinky2_v1_JNT', 'b_R_pinky3_v1_JNT', 'b_R_prop1_v1_JNT', 'b_R_quiver_v1_JNT', 'b_R_ring1_v1_JNT', 'b_R_ring2_v1_JNT', 'b_R_ring3_v1_JNT', 'b_R_shoulderPad_v1_JNT', 'b_R_shoulder_v1_JNT', 'b_R_spear_v1_JNT', 'b_R_swordShell_v1_JNT', 'b_R_sword_v1_JNT', 'b_R_thumb1_v1_JNT', 'b_R_thumb2_v1_JNT', 'b_R_thumb3_v1_JNT', 'b_R_toe_v1_JNT', 'b_R_upperArmLowerTwist_v1_JNT', 'b_R_upperArmUpperTwist_v1_JNT', 'b_R_upperLegLowerTwist_v1_JNT', 'b_R_upperLegUpperTwist_v1_JNT', 'b_R_wrist_v1_JNT']

class AccessaryToolWin(QtGui.QDialog):

	def __init__(self, parent = maya_main_window()):
		super(AccessaryToolWin, self).__init__(parent)

		self.setWindowTitle("AccessaryTool")
		self.setMaximumHeight(330)
		self.setMaximumHeight(300)
		self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

		self.create_widgets()
		self.create_layouts()
		self.create_connections()

	def create_widgets(self):

		self.parentJoint_CB = QtGui.QComboBox()
		for eachJoint in characterJointsName:
			self.parentJoint_CB.addItem(eachJoint)

		self.straightOrCircle_CB = QtGui.QComboBox()
		self.straightOrCircle_CB.addItem('StraightLine')
		self.straightOrCircle_CB.addItem('CircleShape')
		self.AccessaryName_lb = QtGui.QLabel("AccessaryName:")
		self.parentJoint_lb = QtGui.QLabel("ParentJoint:")
		self.evenly_RB = QtGui.QRadioButton('evenly')
		self.customize_RB = QtGui.QRadioButton('customize')
		self.jointName_TE = QtGui.QTextEdit()
		self.jointName_TE.setMinimumHeight(49)
		self.parentJoint_CB.setMaximumWidth(520)
		self.addStartLocator_Btn = QtGui.QPushButton("AddStartLocator")
		self.addEndLocator_Btn = QtGui.QPushButton("AddEndLocator")
		self.addLocator_Btn = QtGui.QPushButton("AddLocator")
		self.addLocator_Btn.setEnabled(False)
		self.jointsAmount_GB = QtGui.QGroupBox('JointsAmount')
		self.createAccessary_Btn = QtGui.QPushButton("CreateAccessary")
		self.jointsAmount_HSlider = QtGui.QSlider(QtCore.Qt.Horizontal,self)
		self.jointsAmount_HSlider.setMinimum(2)
		self.jointsAmount_HSlider.setMaximum(30)
		self.jointsAmount_SpinB = QtGui.QSpinBox()
		self.evenly_RB.setChecked(True)



	def create_layouts(self):

		name_layout = QtGui.QHBoxLayout()
		name_layout.addWidget(self.AccessaryName_lb)
		name_layout.addWidget(self.jointName_TE)

		parent_layout = QtGui.QHBoxLayout()
		parent_layout.addWidget(self.parentJoint_lb)
		parent_layout.addWidget(self.parentJoint_CB)

		rb_layout = QtGui.QHBoxLayout()
		rb_layout.addWidget(self.evenly_RB)
		rb_layout.addWidget(self.customize_RB)

		button_layout =  QtGui.QHBoxLayout()
		button_layout.addWidget(self.addStartLocator_Btn)
		button_layout.addWidget(self.addEndLocator_Btn)

		GB_layout = QtGui.QHBoxLayout()
		GB_layout.addWidget(self.jointsAmount_HSlider)
		GB_layout.addWidget(self.jointsAmount_SpinB)

		self.jointsAmount_GB.setLayout(GB_layout)

		main_layout = QtGui.QVBoxLayout(self)
		main_layout.addWidget(self.straightOrCircle_CB)
		main_layout.addLayout(name_layout)
		main_layout.addLayout(parent_layout)
		main_layout.addLayout(rb_layout)
		main_layout.addLayout(button_layout)
		main_layout.addWidget(self.addLocator_Btn)
		main_layout.addWidget(self.jointsAmount_GB)
		main_layout.addWidget(self.createAccessary_Btn)

	def customizeOn(self):
		self.addLocator_Btn.setEnabled(True)	
		self.addStartLocator_Btn.setEnabled(False)
		self.addEndLocator_Btn.setEnabled(False)
		self.jointsAmount_GB.setEnabled(False)	

	def evenlyOn(self):
		self.addLocator_Btn.setEnabled(False)	
		self.addStartLocator_Btn.setEnabled(True)
		self.addEndLocator_Btn.setEnabled(True)
		self.jointsAmount_GB.setEnabled(True)
	

	def setEnableStraightLine(self,index):
		
		self.addLocator_Btn.setEnabled(index)	
		self.addStartLocator_Btn.setEnabled(not(index))
		self.addEndLocator_Btn.setEnabled(not(index))
		
		self.evenly_RB.setEnabled(not(index))
		self.evenly_RB.setChecked(not(index))
		self.customize_RB.setChecked(index)
		self.jointsAmount_GB.setEnabled(not(index))	


	def customizeEnable(self,index):
		self.customize_RB.setChecked(index)
		self.evenly_RB.setEnabled(not(index))

	def create_connections(self):		
		self.straightOrCircle_CB.currentIndexChanged.connect(self.customizeEnable)  
		self.customize_RB.toggled.connect(self.customizeOn)
		self.evenly_RB.toggled.connect(self.evenlyOn)
		self.jointsAmount_HSlider.valueChanged.connect(self.jointsAmount_SpinB.setValue)
		self.jointsAmount_SpinB.valueChanged.connect(self.jointsAmount_HSlider.setValue)
		self.addStartLocator_Btn.clicked.connect(self.addStartLoc)
		self.addEndLocator_Btn.clicked.connect(self.addEndLoc)
		self.createAccessary_Btn.clicked.connect(self.cre)


	def combineName(self): #'N'in parameter = name
		inputN = self.jointName_TE.toPlainText()
		parentJointN = self.parentJoint_CB.currentText()
		parentJointElement = parentJointN.split('_')[2]
		accesserayN = parentJointN.replace(parentJointElement, inputN)
		return accesserayN

	def addLoc(self):
		accJntN = self.combineName()
		locN = accJntN.replace(accJntN.split('_')[4],'LOC')
		targetJnt = self.parentJoint_CB.currentText()
		targetLocation = mc.xform(targetJnt, q = 1, ws = 1, t = 1)
		startLoc = mc.spaceLocator(n = locN)
		mc.move(targetLocation[0], targetLocation[1], targetLocation[2], startLoc)
		return locN

	def addStartLoc(self):
		locN = self.addLoc()
		mc.rename(locN,  locN + '_start')
		return locN

	def addEndLoc(self):
		locN = self.addLoc()
		mc.rename(locN,  locN + '_end')
		return locN
	
	def createJoints(self):
		print self.addStartLoc()
		startN = mc.xform(self.addStartLoc(), q = 1, ws = 1,t = 1)
		endN = mc.xform(self.addEndLoc(), q = 1, ws = 1,t = 1)
		mc.curve(d = 1, p = [startN,endN])


def initializeUI():
	global dialog
	try :
		dialog.close()
		dialog.deleteLater()
	except:pass

	dialog = AccessaryToolWin()
	dialog.show()









