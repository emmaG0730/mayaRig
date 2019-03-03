pointNameDict = {}

bodyCurves = ['arm_R_', 'arm_L_', 'leg_R_', 'leg_L_', 'head_', 'spine_',
              'thumb_L_', 'index_L_', 'middle_L_', 'ring_L_', 'pinky_L_',
              'thumb_R_', 'index_R_', 'middle_R_', 'ring_R_', 'pinky_R_']

armJntName = ['clavicle', 'shoulder', 'elbow', 'wrist']
legJntName = ['thigh', 'knee', 'ankle', 'ball', 'toe']

for tag in bodyCurves:
    pointNameDict[tag] = []
    if 'arm' in tag:
        for armJnt in armJntName:
            pointNameDict[tag].append(armJnt + '_' + tag[-2])

    elif 'leg' in tag:
        for legJnt in legJntName:
            pointNameDict[tag].append(legJnt + '_' + tag[-2])

    else:
        for n in range(1, 5):
            pointNameDict[tag].append(tag + str(n))

print pointNameDict