import os
from PySide import QtGui
import sys
import xmd_batch_export_UI

rootDir = 'R:\\JX4_SourceData\\Animation\\Morpheme\\JXMain_TEST_ForMorpheme8.0.3\\Characters\\MaleAdult\\Animations'


def get_file_list():
    file_list = []
    for root, dirs, files in os.walk(rootDir):
        for each in files:
            if len(files) != 0 and '.xmd' in each:
                local_file_path = root + '\\' + each
                depot_file_spliced = local_file_path.split('\\')
                depot_file_replaced = local_file_path.replace(depot_file_spliced[0], '//depot')
                depot_file_path = depot_file_replaced.replace('\\', '/')
                file_list.append(depot_file_path)
    return file_list

fileList = get_file_list()

print len(fileList)


