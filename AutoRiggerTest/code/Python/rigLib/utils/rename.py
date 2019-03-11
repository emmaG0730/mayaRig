'''
remove suffix and prefix
'''

def removeSuffix(name):
    tempName = name.split('_')[:-1]
    newName = '_'.join(tempName)
    return newName

def removePrefix(name):
    tempName = name.split('_')[1:]
    newName = '_'.join(tempName)
    return newName

def insertLetters(name, index):
    