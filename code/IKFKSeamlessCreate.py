import maya.cmds as mc
for each in range(5):
	jj = mc.joint(p = (0,0,each),rad = 0.5,sao = 'yup')
	mc.rename(jj,'advanced_' + str(each+1) + '_JNT')
mc.curve(n='advancedCurve1',p=[(0, 0, 0), (0, 0, 4)])
mc.ikHandle( sj='advanced_1_JNT', ee='advanced_5_JNT', c ='advancedCurve1'  ,fj = True,sol = 'ikSplineSolver')
