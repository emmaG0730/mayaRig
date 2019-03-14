import maya.cmds as mc

upperArmLength = mc.getAttr('joint2.tx')
lowerArmLength = mc.getAttr('joint3.tx')
fullLength = upperArmLength + lowerArmLength

mc.setDrivenKeyframe( 'joint2', cd = 'distanceDimensionShape1.distance', driverValue = fullLength,
					attribute = 'translateX', value = upperArmLength)
mc.setDrivenKeyframe( 'joint3', cd = 'distanceDimensionShape1.distance', driverValue = fullLength,
					attribute = 'translateX', value = lowerArmLength)
					
mc.setDrivenKeyframe( 'joint2', cd = 'distanceDimensionShape1.distance', driverValue = fullLength*2,
					attribute = 'translateX', value = upperArmLength*2)
mc.setDrivenKeyframe( 'joint3', cd = 'distanceDimensionShape1.distance', driverValue = fullLength*2,
					attribute = 'translateX', value = lowerArmLength*2)