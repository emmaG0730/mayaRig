import os
from PySide import QtGui
import sys
import xmd_export_UI2
import subprocess
import json

class BatchExport(QtGui.QMainWindow):

	"""
	this class is the whole tool script,include UI and funtions
	"""

	def __init__(self):
		super(BatchExport, self).__init__()

		self.setWindowTitle("BatchExportXMD")
		self.ui = xmd_export_UI2.Ui_MainWindow()
		self.MainWindow = QtGui.QMainWindow()
		self.MainWidget = QtGui.QWidget()

	def create_connections(self):
		"""
		connects the ui elements to methods
		:return: none
		"""
		self.ui.exportBtn.clicked.connect(self.batch_export)
		print 'connects signals to the ui'

	def batch_export(self):
		pass

	def set_workspace(self):
		input_text = self.ui.textEdit.toPlainText()
		subprocess.Popen('powershell.exe P4 CLIENT ' + str(input_text))

	def export(self):
		"""
		exports the selected file based on the check boxes
		:return: none
		"""

		print 'exporting xmd'
		animList = {}
		for i in animName:
			self.filterData.fetchSourceFile(i.text())
			sourceData = self.filterData.fetchAll()[0]
			self.filterData.generateXMDPath(sourceData['unique_id'])
			jsonData = self.filterData.fetchAll()[0]
			sourcePath = 'r:' + sourceData['location'] + sourceData['unique_id'] + '.' + sourceData['ext']
			jsonPath = 'r:' + jsonData['location'] + jsonData['project_name'] + '/Characters/' + \
					   jsonData['gender'] + jsonData['size'] + '/' + jsonData['char_name'].replace(' ',
																								   '') + \
					   '/' + jsonData['anim_category'] + '/' + jsonData['anim_subcategory'] + '/' + \
					   jsonData['export_name'] + '.' + jsonData['ext']

			animList[sourcePath] = jsonPath
		with open('data/xmd.json', 'w') as fp:
			json.dump(animList, fp, indent=4)

		p = subprocess.Popen('R:Jx4/tools/dcc/maya/nightly/scripts/matrix/subScripts/exportExternal.bat')
		print 'exporting xmd'

	def mai(self):
		self.ui.setupUi(self.MainWindow)
		self.create_connections()
		self.MainWindow.show()


def main():
	app = QtGui.QApplication(sys.argv)
	be = BatchExport()
	be.mai()
	sys.exit(app.exec_())


main()
