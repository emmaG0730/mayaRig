#-----------------------------------------------------------------------------------#
# Scripted By: Linh Nguyen                                                          #
# Description: Extracts data from animation file and populates the database with it.#
#-----------------------------------------------------------------------------------#

import sys, os, json, AE_Tag_View, AE_NewFile_UI, AE_MySQL, subprocess, AE_P4
sys.path.append('../../')
import AE_UI
import shutil
import internal.qdarkstyle as style
from PySide import QtGui


class AnimExplorer(QtGui.QMainWindow):

    def __init__(self, login_data):
        """
        constructs the QPaint device
        :param login_data: database login information dictionary
        """

        super(AnimExplorer, self).__init__()
        self.aep4 = AE_P4.animExploreP4()
        self.loginData = self.fetchLoginData(login_data)
        self.filterData = AE_MySQL.MySQL_Animation(self.loginData['user'],
                                                    self.loginData['password'],
                                                    self.loginData['host'],
                                                    self.loginData['port'],
                                                    self.loginData['database'])

        self.ui = AE_UI.Ui_MainWindow()

    def read_data(self, dataPath):
        if os.path.isfile(dataPath):
            with open(dataPath) as dataFile:
                fileData = json.load(dataFile)
            return fileData
        else:
            print 'Missing data file'

    def add_widget_to_component(self):
        self.tags = self.read_data('data/tags.json')
        lineEditButton = AE_Tag_View.LineEditAutocompleteButton('test_a', self.tags)
        item, widget, widgetText, addButton = lineEditButton.create_widget()
        self.ui.l_filter.addItem(item)
        self.ui.l_filter.setItemWidget(item, widget)
        self.connect_item_widget_signals(addButton)

    def connect_item_widget_signals(self, buttonB):
        buttonB.clicked.connect(self.add_widget_to_component)

    def connect_signals(self):
        """
        connects the ui elements to methods
        :return: none
        """

        print 'connects signals to the ui'
        self.ui.btn_newFile.clicked.connect(self.new_file)
        self.ui.l_character.clicked.connect(self.updateUI)
        self.ui.l_weapon.clicked.connect(self.updateUI)
        self.ui.t_category.clicked.connect(self.updateUI)
        self.ui.btn_ok.clicked.connect(self.openFile)
        self.ui.btn_getLatest.clicked.connect(self.getLatest)
        self.ui.btn_checkout.clicked.connect(self.checkout)
        self.ui.btn_revert.clicked.connect(self.revert)
        self.ui.btn_shelve.clicked.connect(self.shelve)
        self.ui.btn_unshelf.clicked.connect(self.unshelf)
        self.ui.lw_fileView.clicked.connect(self.uiFilter)
        self.ui.btn_export.clicked.connect(self.export)
        self.ui.btn_cancel.clicked.connect(self.cancel)
        self.ui.btn_update.clicked.connect(self.updateDetails)
        self.ui.rad_max.clicked.connect(self.toggle)
        self.ui.rad_maya.clicked.connect(self.toggle)

    #---------------------------------------------------- Signals -----------------------------------------------------#
    def updateDetails(self):
        description = self.ui.s_description.toPlainText()
        animStatus, animName = self.getSelected()
        print description
        animation = animName[0].text()

        self.filterData.updateColumnIndex('Animation', 'anim', animation, 'description', description.encode('utf-8'))
        self.filterData.commit()

    def cancel(self):
        """
        closes window
        :return: none
        """
        if self.MainWindow != None:
            self.MainWindow.close()
            self.MainWindow = None

    def toggle(self):
        print 'toggling'
        self.ui.lw_fileView.clearSelection()
        self.uiFilter()
        self.updateUI()

    def uiFilter(self):
        """
        toggles UI features based on selected items
        :return:
        """
        animName = self.ui.lw_fileView.selectedItems()

        if self.ui.rad_max.isChecked() == True:
            if len(animName) > 1:
                print'multiple items selected'
                self.ui.btn_export.setEnabled(True)
                self.ui.btn_convert.setEnabled(True)
                self.ui.btn_getLatest.setEnabled(True)
                self.ui.btn_checkout.setEnabled(True)
                self.ui.btn_revert.setEnabled(True)
                self.ui.btn_shelve.setEnabled(True)
                self.ui.btn_ok.setEnabled(False)
                self.ui.btn_renameFile.setEnabled(True)
                self.ui.btn_update.setEnabled(False)

                # ------checkboxes------
                self.ui.cb_ma.setEnabled(True)
                self.ui.cb_fbx.setEnabled(True)
                self.ui.cb_xmd.setEnabled(True)
                self.ui.cb_mesh.setEnabled(True)
                self.ui.cb_json.setEnabled(False)
                self.ui.cb_legTracking.setEnabled(True)
                self.ui.cb_armTracking.setEnabled(True)
                self.ui.cb_old.setEnabled(False)

                # ------other-------
                self.ui.l_scale.setEnabled(True)
                self.ui.f_scale.setEnabled(True)

            elif len(animName) == 1:
                print 'one item selected'
                self.ui.btn_export.setEnabled(True)
                self.ui.btn_convert.setEnabled(True)
                self.ui.btn_getLatest.setEnabled(True)
                self.ui.btn_checkout.setEnabled(True)
                self.ui.btn_revert.setEnabled(True)
                self.ui.btn_shelve.setEnabled(True)
                self.ui.btn_ok.setEnabled(True)
                self.ui.btn_renameFile.setEnabled(True)
                self.ui.btn_update.setEnabled(True)

                # ------checkboxes------
                self.ui.cb_ma.setEnabled(True)
                self.ui.cb_fbx.setEnabled(True)
                self.ui.cb_xmd.setEnabled(True)
                self.ui.cb_mesh.setEnabled(True)
                self.ui.cb_json.setEnabled(False)
                self.ui.cb_legTracking.setEnabled(True)
                self.ui.cb_armTracking.setEnabled(True)
                self.ui.cb_old.setEnabled(False)

                # ------other-------
                self.ui.l_scale.setEnabled(True)
                self.ui.f_scale.setEnabled(True)

                self.getDescription()

            else:
                print 'no items selected'
                # -------buttons--------
                self.ui.btn_export.setEnabled(True)
                self.ui.btn_convert.setEnabled(False)
                self.ui.btn_getLatest.setEnabled(False)
                self.ui.btn_checkout.setEnabled(False)
                self.ui.btn_revert.setEnabled(False)
                self.ui.btn_shelve.setEnabled(False)
                self.ui.btn_ok.setEnabled(False)
                self.ui.btn_renameFile.setEnabled(False)
                self.ui.btn_update.setEnabled(False)

                # ------checkboxes------
                self.ui.cb_ma.setEnabled(False)
                self.ui.cb_fbx.setEnabled(False)
                self.ui.cb_xmd.setEnabled(False)
                self.ui.cb_mesh.setEnabled(True)
                self.ui.cb_json.setEnabled(False)
                self.ui.cb_legTracking.setEnabled(False)
                self.ui.cb_armTracking.setEnabled(False)
                self.ui.cb_old.setEnabled(False)

                # ------other-------
                self.ui.l_scale.setEnabled(False)
                self.ui.f_scale.setEnabled(False)
        else:


            if len(animName) > 1:
                print'multiple items selected'
                self.ui.btn_export.setEnabled(True)
                self.ui.btn_convert.setEnabled(True)
                self.ui.btn_getLatest.setEnabled(True)
                self.ui.btn_checkout.setEnabled(True)
                self.ui.btn_revert.setEnabled(True)
                self.ui.btn_shelve.setEnabled(True)
                self.ui.btn_ok.setEnabled(False)
                self.ui.btn_renameFile.setEnabled(True)
                self.ui.btn_update.setEnabled(False)

                # ------checkboxes------
                self.ui.cb_ma.setEnabled(True)
                self.ui.cb_fbx.setEnabled(True)
                self.ui.cb_xmd.setEnabled(True)
                self.ui.cb_mesh.setEnabled(True)
                self.ui.cb_json.setEnabled(True)
                self.ui.cb_legTracking.setEnabled(True)
                self.ui.cb_armTracking.setEnabled(True)
                self.ui.cb_old.setEnabled(True)

                # ------other-------
                self.ui.l_scale.setEnabled(True)
                self.ui.f_scale.setEnabled(True)

            elif len(animName) == 1:
                print 'one item selected'
                self.ui.btn_export.setEnabled(True)
                self.ui.btn_convert.setEnabled(True)
                self.ui.btn_getLatest.setEnabled(True)
                self.ui.btn_checkout.setEnabled(True)
                self.ui.btn_revert.setEnabled(True)
                self.ui.btn_shelve.setEnabled(True)
                self.ui.btn_ok.setEnabled(True)
                self.ui.btn_renameFile.setEnabled(True)
                self.ui.btn_update.setEnabled(True)

                # ------checkboxes------
                self.ui.cb_ma.setEnabled(True)
                self.ui.cb_fbx.setEnabled(True)
                self.ui.cb_xmd.setEnabled(True)
                self.ui.cb_mesh.setEnabled(True)
                self.ui.cb_json.setEnabled(True)
                self.ui.cb_legTracking.setEnabled(True)
                self.ui.cb_armTracking.setEnabled(True)
                self.ui.cb_old.setEnabled(True)

                # ------other-------
                self.ui.l_scale.setEnabled(True)
                self.ui.f_scale.setEnabled(True)

                self.getDescription()

            else:
                print 'no items selected'
                #-------buttons--------
                self.ui.btn_export.setEnabled(True)
                self.ui.btn_convert.setEnabled(False)
                self.ui.btn_getLatest.setEnabled(False)
                self.ui.btn_checkout.setEnabled(False)
                self.ui.btn_revert.setEnabled(False)
                self.ui.btn_shelve.setEnabled(False)
                self.ui.btn_ok.setEnabled(False)
                self.ui.btn_renameFile.setEnabled(False)
                self.ui.btn_update.setEnabled(False)

                #------checkboxes------
                self.ui.cb_ma.setEnabled(False)
                self.ui.cb_fbx.setEnabled(False)
                self.ui.cb_xmd.setEnabled(False)
                self.ui.cb_mesh.setEnabled(True)
                self.ui.cb_json.setEnabled(False)
                self.ui.cb_legTracking.setEnabled(False)
                self.ui.cb_armTracking.setEnabled(False)
                self.ui.cb_old.setEnabled(False)

                #------other-------
                self.ui.l_scale.setEnabled(False)
                self.ui.f_scale.setEnabled(False)

    def getDescription(self):
        """
        gets the description of the selected animation
        :return:
        """

        animStatus, animName = self.getSelected()
        if self.ui.rad_max.isChecked():
            self.filterData.fetchMaxAnimDescription(animName[0].text())
        else:
            self.filterData.setCursorToColumnIndex('Animation','description','anim', animName[0].text())
        description = self.filterData.fetchOne()
        self.ui.s_description.setText(description['description'])


    def getLatest(self):
        """
        gets the head revision of file(s) selected
        :return:
        """

        animStatus, animName = self.getSelected()
        if animStatus == True:
            self.aep4.connect()
            fileList = self.getSourceList(animName)
            status = self.aep4.get_latest(fileList)
            self.ui.statusbar.showMessage(status)
            self.aep4.disconnect()
        else:
            self.ui.statusbar.showMessage(animName)

    def getSelected(self):
        """
        returns a list of names selected in the file list
        :return: names list
        """

        animName = self.ui.lw_fileView.selectedItems()
        if len(animName) == 0:
            return False, 'No animation selected'
        else:
            return True, animName

    def getCharacterSelection(self):
        charName = self.ui.l_character.selectedItems()
        if len(charName) == 0:
            return False, 'No character selected'
        else:
            self.filterData.fetchCharacters()
            characterData = self.filterData.fetchAll()
            characters = []

            print characterData

            for i in characterData:
                characters.append(i['char_name'])

            for i in charName:
                if i.text() == 'All Characters':
                    print characters
                    return True, characters
                else:
                    pass
            else:
                characters = []
                for i in charName:
                    characters.append(i.text())
                return True, characters

    def checkout(self):
        """
        checks out the file selected
        :return: none
        """

        print 'checks out file'
        animStatus, animName = self.getSelected()
        if animStatus == True:
            self.aep4.connect()
            cl = self.aep4.create_checkout_cl()

            # generates the source path list
            checkoutList = self.getSourceList(animName)
            self.aep4.open_for_edit(checkoutList, cl)

            for i in animName:
                font = QtGui.QFont()
                font.setBold(True)
                font.setWeight(100)
                i.setFont(font)
                self.ui.statusbar.showMessage(i.text())
            self.aep4.disconnect()
        else:
            self.ui.statusbar.showMessage(animName)

    def revert(self):
        """
        reverts the selected file
        :return: none
        """

        animStatus, animName = self.getSelected()
        if animStatus == True:

            self.aep4.connect()

            # gets the source file(s) path via the database
            animList = self.getSourceList(animName)
            notInCL = []
            for i in animList:
                result = self.aep4.in_changelist(i)
                if result == True:
                    pass
                elif result == False:
                    notInCL.append(i)

            print 'not in cl =', type(notInCL)
            print 'revert list =', type(animList)

            revertList = [x for x in animList if x not in notInCL]

            # reverts the file(s) passed in
            status = self.aep4.revert_file(revertList)

            for i in animName:
                # unbolds reverted files
                font = QtGui.QFont()
                font.setBold(False)
                i.setFont(font)
                self.ui.statusbar.showMessage(status)
            self.aep4.disconnect()
        else:
            self.ui.statusbar.showMessage(animName)

    def shelve(self):
        """
        selves the selected file
        :return: none
        """
        self.aep4.shelveFile('test')

    def unshelf(self):
        """
        unshelves the selected file
        :return: none
        """

        self.aep4.unshelfFile('test')

    def new_file(self):
        """
        launches new file dialog box
        :return: none
        """

        if __name__ == "__main__":
            AE_NewFile_UI.main()

    def openFile(self):
        """
        opens the selected file
        :return: none
        """
        print 'opening file'
        animName = self.ui.lw_fileView.selectedItems()
        if len(animName) == 0:
            print 'No animation selected'
        else:
            sourceFilePath = self.getSourcePath(animName[0].text())
            if self.ui.rad_max.isChecked() == True:
                subprocess.Popen('"E:/Program Files/Autodesk/3ds Max 2016/3dsmax.exe" "' + sourceFilePath + '"') #DJM
            else:

                subprocess.Popen('"E:/Program Files/Autodesk/Maya2016/bin/maya.exe" -file ' + sourceFilePath) #DJM

    def export(self):
        """
        exports the selected file based on the check boxes
        :return: none
        """

        animStatus, animName = self.getSelected()

        if self.ui.cb_mesh.isChecked() == True:
            status, character = self.getCharacterSelection()
            MESHData = {}
            print status
            for i in character:
                self.filterData.fetchSourceCharacter(i)
                sourceData = self.filterData.fetchAll()[0]
                self.filterData.generateCharacterMeshPath(sourceData['unique_id'])
                exportData = self.filterData.fetchAll()[0]
                sourcePath = 'r:' + sourceData['location'] + sourceData['unique_id'] + '.' + sourceData['ext']
                exportPath = 'r:' + exportData['location'] + exportData['char_type'] + '/' + exportData['unique_id']
                characterData = {}
                characterData['exportPath']=exportPath
                characterData['parts']=exportData['parts']
                MESHData[sourcePath] = characterData
            with open('data/MESH.json', 'w') as fp:
                json.dump (MESHData, fp, indent=4)
            p = subprocess.Popen('AE_MayaBatchMesh.bat')

        else:
            pass

        if animStatus == True:
            jsonStatus = self.ui.cb_json.isChecked()
            xmdStatus = self.ui.cb_xmd.isChecked()
            legacyStatus = self.ui.cb_old.isChecked()
            maxStatus = self.ui.rad_max.isChecked()
            mayaStatus = self.ui.cb_ma.isChecked()
            fbxStatus = self.ui.cb_fbx.isChecked()


            if jsonStatus == True and maxStatus == False:
                print '>>> exporting starman'
                animList ={}
                for i in animName:
                    self.filterData.fetchSourceFile(i.text())
                    sourceData = self.filterData.fetchAll()[0]
                    self.filterData.generateStarmanPath(sourceData['unique_id'])
                    jsonData = self.filterData.fetchAll()[0]
                    print '>>>', jsonData
                    sourcePath = 'r:'+ sourceData['location'] + sourceData['unique_id'] + '.' + sourceData['ext']
                    jsonPath = 'r:' + jsonData['location'] + jsonData['unique_id'] + '.' + jsonData['ext']

                    animList[sourcePath]=jsonPath
                with open('data/starman.json', 'w') as fp:
                    json.dump(animList, fp, indent=4)

                subprocess.Popen('R:Jx4/tools/dcc/maya/nightly/scripts/starmanExporter/sm_batch_export.bat')
            else:
                print '>>> not exporting Starman'


            if xmdStatus == True and maxStatus == False:
                print 'exporting xmd'
                animList = {}
                for i in animName:
                    self.filterData.fetchSourceFile(i.text())
                    sourceData = self.filterData.fetchAll()[0]
                    self.filterData.generateXMDPath(sourceData['unique_id'])
                    jsonData = self.filterData.fetchAll()[0]
                    sourcePath = 'r:' + sourceData['location'] + sourceData['unique_id'] + '.' + sourceData['ext']
                    jsonPath = 'r:' + jsonData['location'] + jsonData['project_name'] + '/Characters/' + \
                               jsonData['gender'] + jsonData['size'] + '/' + jsonData['char_name'].replace(' ','') + \
                               '/' + jsonData['anim_category'] + '/' + jsonData['anim_subcategory'] + '/' + \
                               jsonData['export_name'] + '.' + jsonData['ext']

                    animList[sourcePath]=jsonPath
                with open('data/xmd.json', 'w') as fp:
                    json.dump(animList, fp, indent=4)

                p = subprocess.Popen('R:Jx4/tools/dcc/maya/nightly/scripts/matrix/subScripts/exportExternal.bat')
            else:
                print '>>> not exporting XMD'

            if legacyStatus == True and maxStatus == False:
                print 'exporting legacy file'
                for i in animName:
                    self.filterData.fetchSourceFile(i.text())
                    sourceData = self.filterData.fetchAll()[0]
                    self.filterData.generateLegacyPath(sourceData['unique_id'])
                    jsonData = self.filterData.fetchAll()[0]
                    sourcePath = 'r:' + sourceData['location'] + sourceData['unique_id'] + '.' + sourceData['ext']
                    pipelinePath = ('/').join((str(jsonData['location']).split('/'))[:-2]) +'/'
                    jsonData['location'] = pipelinePath
                    print jsonData
                    jsonPath = 'r:' + jsonData['location'] + jsonData['gender'] + '/' + jsonData['size'] + '/' + \
                               (jsonData['char_name']).replace(' ','') + '/' + jsonData['anim_category'] + '/' + \
                               jsonData['anim_subcategory'] + '/' + jsonData['anim'] + '.' +jsonData['ext']
                    self.copyFile(sourcePath, jsonPath)

            else:
                print '>>> not exporting legacy file'

            if mayaStatus == True and maxStatus == True:
                print 'converting Max animation to Maya'
                maxList = {}
                mayaList = {}
                mayaFiles = []
                for i in animName:
                    self.filterData.fetchMaxSourceFile(i.text())
                    sourceData = self.filterData.fetchAll()[0]
                    self.filterData.generateMayaPath(sourceData['unique_id'])
                    mayaData = self.filterData.fetchAll()[0]
                    print mayaData
                    mayaDepotPath = '//depot' + mayaData['location'] + mayaData['unique_id'] + '.' + mayaData['ext']
                    mayaFiles.append(mayaDepotPath)
                    sourcePath = 'r:' + sourceData['location'] + sourceData['unique_id'] + '.' + sourceData['ext']
                    fbxPath = 'r:' + mayaData['location'] + 'fbx/' + mayaData['unique_id'] + '.fbx'
                    mayaPath = 'r:' + mayaData['location'] + mayaData['unique_id'] + '.' + mayaData['ext']

                    maxList[sourcePath] = fbxPath
                    mayaList[fbxPath] = mayaPath

                # writing json data for max to fbx converstion
                with open('data/maxtofbx.json', 'w') as fp:
                    json.dump(maxList, fp, indent=4)

                # writing json data for fbx to maya conversion
                with open('data/fbxtomaya.json', 'w') as fp:
                    json.dump(mayaList, fp, indent=4)

                # checks out maya files in p4
                self.aep4.connect()
                cl = self.aep4.create_checkout_cl()
                self.aep4.open_for_edit(mayaFiles, cl)
                self.aep4.disconnect()

                subprocess.Popen('AE_MaxToMaya.bat')

            else:
                print '>>> not converting Max to Maya'

            if xmdStatus == True and maxStatus == True:
                print 'exporting xmd file from Max'
            else:
                print '>>> not exporting xmd from Max'

            if fbxStatus == True and maxStatus == True:
                print 'exporting fbx from Max'

            else:
                print '>>> not exporting fbx from Max'
                animList = {}
                for i in animName:
                    self.filterData.fetchMaxSourceFile(i.text())
                    sourceData = self.filterData.fetchAll()[0]
                    self.filterData.generateMayaPath(sourceData['unique_id'])
                    mayaData = self.filterData.fetchAll()[0]
                    print mayaData
                    sourcePath = 'r:' + sourceData['location'] + sourceData['unique_id'] + '.' + sourceData['ext']
                    fbxPath = 'r:' + mayaData['location'] + 'fbx/' + mayaData['unique_id'] + '.fbx'

                    animList[sourcePath] = fbxPath
                with open('data/maxtofbx.json', 'w') as fp:
                    json.dump(animList, fp, indent=4)
                subprocess.Popen('ExportMax.bat')

        else:
            pass


    def ensure_dir(self, file_path):
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

    def copyFile(self, source, output):
        out = output.split('/')
        outPath=(('/').join((out)[:-2])) + '/'
        outFile = out[-1]
        self.ensure_dir(outPath)
        shutil.copyfile(source, outPath+outFile)

    def getSourcePath(self, animName):
        """
        gets the source file location
        :param animName: animation name string
        :return: source file path string
        """
        if self.ui.rad_max.isChecked() == True:
            self.filterData.fetchMaxSourceFile(animName)
        else:
            self.filterData.fetchSourceFile(animName)
        sourceData = self.filterData.fetchAll()[0]
        sourceFilePath = 'r:' + sourceData['location'] + sourceData['unique_id'] + '.' + sourceData['ext']
        print 'path>>>', sourceFilePath
        return sourceFilePath

    # returns a list of the source files locations
    def getSourceList(self, animList):
        sourceList = []
        for i in animList:
            print '>>>', i
            sourceFilePath = self.getSourcePath(i.text())
            actualPath = self.aep4.get_actual_path(sourceFilePath)
            depotPath = self.aep4.get_depot_path(actualPath)
            sourceList.append(depotPath)
        return sourceList

    # ------------------------------------------------------ UI -------------------------------------------------------#

    def updateUI(self):
        print 'ui is updating'
        characters = self.ui.l_character.selectedItems()
        weapons = self.ui.l_weapon.selectedItems()
        categories = self.ui.t_category.selectedItems()

        catList = []
        subCatList = []

        charList = [i.text() for i in characters]
        weapList = [i.text() for i in weapons]

        maxFilter = self.ui.rad_max.isChecked()

        for i in categories:
            if i.text(0) in self.categories:
                catList.append(i.text(0))
            else:
                subCatList.append(i.text(0))
        #catList = [i.text(0) for i in categories]

        charIDs = self.getIDs(self.characters[0], charList, 'Character_Asset', 'char_name')
        weapIDs = self.getIDs(self.weapons[0], weapList, 'Weapon_Type', 'weap_type')

        # only subcategories are selected
        if len(catList) == 0:
            print 'only subcategories are selected'
            subCatIDs = []
            for i in subCatList:
                self.filterData.setCursorToID('Anim_Subcategory', 'anim_subcategory',  i )
                id = self.filterData.fetchAll()
                id = [v['id'] for v in id][0]
                subCatIDs.append(id)

            if maxFilter == True:
                self.filterData.getMaxAnimData(None, subCatIDs, charIDs, weapIDs)
            else:
                self.filterData.getAnimData(None, subCatIDs, charIDs, weapIDs)
            animData = self.filterData.fetchAll()

            self.ui.lw_fileView.setColumnCount(1)
            self.ui.lw_fileView.setRowCount(len(animData))

            if maxFilter == True:
                for i in range(len(animData)):
                    self.ui.lw_fileView.setItem(i, 0, QtGui.QTableWidgetItem(animData[i]['original_name']))
            else:
                for i in range(len(animData)):
                    self.ui.lw_fileView.setItem(i, 0, QtGui.QTableWidgetItem(animData[i]['anim']))

        # only categories are selected
        elif len(subCatList) == 0:
            print 'only categories are selected'
            catIDs = self.getIDs(self.categories[0], catList, 'Anim_Category', 'anim_category')

            if maxFilter == True:
                self.filterData.getMaxAnimData(catIDs, None, charIDs, weapIDs)
            else:
                self.filterData.getAnimData(catIDs, None, charIDs, weapIDs)
            animData = self.filterData.fetchAll()

            self.ui.lw_fileView.setColumnCount(1)
            self.ui.lw_fileView.setRowCount(len(animData))

            if maxFilter == True:
                for i in range(len(animData)):
                    self.ui.lw_fileView.setItem(i, 0, QtGui.QTableWidgetItem(animData[i]['original_name']))
            else:
                for i in range(len(animData)):
                    self.ui.lw_fileView.setItem(i, 0, QtGui.QTableWidgetItem(animData[i]['anim']))

        # subcategories and categories are selected
        else:
            print 'subcategories and categories are selected'
            catIDs = self.getIDs(self.categories[0], catList, 'Anim_Category', 'anim_category')
            subCatIDs = []
            for i in subCatList:
                self.filterData.setCursorToID('Anim_Subcategory', 'anim_subcategory', i )
                id = self.filterData.fetchAll()
                id = [v['id'] for v in id][0]
                subCatIDs.append(id)

            if maxFilter == True:
                self.filterData.getMaxAnimData(catIDs, subCatIDs, charIDs, weapIDs)
            else:
                self.filterData.getAnimData(catIDs, subCatIDs, charIDs, weapIDs)
            animData = self.filterData.fetchAll()

            self.ui.lw_fileView.setColumnCount(1)
            self.ui.lw_fileView.setRowCount(len(animData))
            if maxFilter == True:
                for i in range(len(animData)):
                    self.ui.lw_fileView.setItem(i, 0, QtGui.QTableWidgetItem(animData[i]['original_name']))
            else:
                for i in range(len(animData)):
                    self.ui.lw_fileView.setItem(i, 0, QtGui.QTableWidgetItem(animData[i]['anim']))

        self.uiFilter()


    # returns a list of subcategories for the passed in category
    def getSubCategories(self, category):
        self.filterData.setCursorToID('Anim_Category', 'anim_category', category)
        catID = self.filterData.fetchOne()
        if catID == None:
            return False, []
        else:
            self.filterData.setCursorToColumnIndex('Anim_Subcategory', 'anim_subcategory', 'anim_cat_id', str(catID['id']))
            subCatList = [i['anim_subcategory'] for i in self.filterData.fetchAll()]

            return True, subCatList


    # returns a list of IDs
    def getIDs(self, firstItem, items, table, column):
        """

        :param firstItem:
        :param items:
        :param table: table name string
        :param column: column name string
        :return: IDs list
        """

        IDList = []
        if firstItem in items:
            IDList = None
            return IDList
        else:
            for i in items:
                self.filterData.setCursorToID(table, column, i)
                id = self.filterData.fetchAll()
                id = [v['id'] for v in id][0]
                IDList.append(id)

            return IDList

    def fetchLoginData(self, data_path):
        """
        Gets the login data from the data_path
        :param data_path: json login data file string
        :return: data from json login file dictionary
        """

        print 'gets login data'
        with open(data_path) as data_file:
            data = json.load(data_file)
        return data

    def launchUIData(self):
        """
        generates the data needed for the UI at launch
        :return:
        """

        connectStatus, message = self.filterData.connect()
        if connectStatus:
            self.ui.statusbar.showMessage(message)
            print 'setting cursor to column'
            self.filterData.setCursorToColumn('Character_Asset', 'char_name')
            self.characters = [v['char_name'] for v in self.filterData.fetchAll()]
            self.characters = ['All Characters'] + self.characters

            self.filterData.setCursorToColumn('Weapon_Type', 'weap_type')
            self.weapons = [v['weap_type'] for v in self.filterData.fetchAll()]
            self.weapons = ['All Weapons'] + self.weapons

            self.filterData.setCursorToColumn('Anim_Category', 'anim_category')
            self.categories = [v['anim_category'] for v in self.filterData.fetchAll()[1::]]
            self.categories = ['All Animations'] + self.categories

            self.category = []
            self.ui.t_category.setColumnCount(3)

            for i in self.categories:
                std_item = QtGui.QTreeWidgetItem([i])
                status, data = self.getSubCategories(i)
                if status == False:
                    pass
                else:
                    for y in data:
                        child_std_item = QtGui.QTreeWidgetItem([y])
                        std_item.addChild(child_std_item)
                self.category.append(std_item)


            self.ui.l_character.addItems(self.characters)
            self.ui.l_weapon.addItems(self.weapons)
            self.ui.t_category.addTopLevelItems(self.category)

            self.ui.l_character.item(0).setSelected(True)
            self.ui.l_weapon.item(0).setSelected(True)

            self.ui.t_category.setCurrentItem(self.ui.t_category.topLevelItem(0))

            self.updateUI()
        else:
            self.ui.statusbar.showMessage(str(message))

    def main(self):

        self.MainWindow = QtGui.QMainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWidget = QtGui.QWidget()
        self.ui.l_filter = AE_Tag_View.List(self.MainWidget)
        self.ui.hl_filter.addWidget(self.ui.l_filter)
        self.add_widget_to_component()
        self.connect_signals()
        self.MainWindow.show()
        self.launchUIData()

def main():
    app = QtGui.QApplication(sys.argv)
    ae = AnimExplorer('AE_Login_Data.json')
    ae.main()
    app.setStyleSheet(style.load_stylesheet(pyside=True))
    sys.exit(app.exec_())

main()
