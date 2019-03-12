'''
remove suffix and prefix
'''

def removeSuffix(name):
    tempList = name.split('_')[:-1]
    newName = '_'.join(tempList)
    return newName

def removePrefix(name):
    tempList = name.split('_')[1:]
    newName = '_'.join(tempName)
    return newName

def insertLetters(name, index, obj):
    tempList = name.split('_')
    tempList.insert(index, obj)
    newName = '_'.join(tempList)
    return newName
    