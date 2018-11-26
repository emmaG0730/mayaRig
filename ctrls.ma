//Maya ASCII 2016 scene
//Name: ctrls.ma
//Last modified: Thu, Nov 08, 2018 02:52:57 PM
//Codeset: 936
requires maya "2016";
requires "stereoCamera" "10.0";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2016";
fileInfo "version" "2016";
fileInfo "cutIdentifier" "201603180400-990260";
fileInfo "osv" "Microsoft Windows 8 Enterprise Edition, 64-bit  (Build 9200)\n";
createNode transform -n "l_Arm_Switch_Ctrl1";
	rename -uid "1F99AB12-42EA-E0D6-62B4-F8BE54ED5FBA";
	addAttr -ci true -sn "switchIkFk" -ln "switchIkFk" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "modCoreName" -ln "modCoreName" -dt "string";
	addAttr -ci true -sn "moduleType" -ln "moduleType" -dt "string";
	addAttr -ci true -sn "rightControl" -ln "rightControl" -dt "string";
	addAttr -ci true -sn "modRigName" -ln "modRigName" -dt "string";
	addAttr -ci true -sn "modRigConnection" -ln "modRigConnection" -dt "string";
	addAttr -ci true -sn "modControlName" -ln "modControlName" -dt "string";
	addAttr -ci true -sn "isMirrored" -ln "isMirrored" -dv 1 -at "double";
	setAttr ".rp" -type "double3" 0 0 5.9 ;
	setAttr ".sp" -type "double3" 0 0 5.9 ;
	setAttr -l on -k on ".modCoreName" -type "string" "l_Arm";
	setAttr -l on -k on ".moduleType" -type "string" "arm";
	setAttr -k on ".rightControl";
	setAttr -l on -k on ".modRigName" -type "string" "";
	setAttr -l on -k on ".modRigConnection";
	setAttr -l on ".modControlName" -type "string" "l_Arm_Switch_Ctrl";
	setAttr ".isMirrored" 1015;
createNode nurbsCurve -n "l_Arm_Switch_Ctrl1Shape" -p "l_Arm_Switch_Ctrl1";
	rename -uid "AE8AFB6B-4986-2BFF-9560-D59510F25C81";
	addAttr -ci true -sn "curveCheck" -ln "curveCheck" -dt "string";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
	setAttr ".cc" -type "nurbsCurve" 
		1 14 0 no 3
		15 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
		15
		0 0 6.4000000000000004
		-0.40000000000000002 0 6
		-0.20000000000000001 0 6
		-0.20000000000000001 0 5.4000000000000004
		0.20000000000000001 0 5.4000000000000004
		0.20000000000000001 0 6
		0.40000000000000002 0 6
		0 0 6.4000000000000004
		0 0.40000000000000002 6
		0 0.20000000000000001 6
		0 0.20000000000000001 5.4000000000000004
		0 -0.20000000000000001 5.4000000000000004
		0 -0.20000000000000001 6
		0 -0.40000000000000002 6
		0 0 6.4000000000000004
		;
	setAttr -l on -k on ".curveCheck" -type "string" "";
createNode transform -n "r_Leg_KneeIk_Ctrl2";
	rename -uid "15286581-4963-1328-2DC7-759FB516743E";
	addAttr -ci true -sn "follow" -ln "follow" -min 0 -max 3 -en "Main:Ankle:Hip:Ankle and Hip" 
		-at "enum";
	addAttr -ci true -sn "modCoreName" -ln "modCoreName" -dt "string";
	addAttr -ci true -sn "moduleType" -ln "moduleType" -dt "string";
	addAttr -ci true -sn "leftControl" -ln "leftControl" -dt "string";
	addAttr -ci true -sn "modRigName" -ln "modRigName" -dt "string";
	addAttr -ci true -sn "modRigConnection" -ln "modRigConnection" -dt "string";
	addAttr -ci true -sn "modControlName" -ln "modControlName" -dt "string";
	addAttr -ci true -sn "controlSizeX" -ln "controlSizeX" -dv 1 -at "double";
	addAttr -ci true -sn "controlSizeY" -ln "controlSizeY" -dv 1 -at "double";
	addAttr -ci true -sn "controlSizeZ" -ln "controlSizeZ" -dv 1 -at "double";
	addAttr -ci true -sn "isMirrored" -ln "isMirrored" -dv 1 -at "double";
	setAttr -l on -k on ".modCoreName" -type "string" "r_Leg";
	setAttr -l on -k on ".moduleType" -type "string" "leg";
	setAttr -k on ".leftControl";
	setAttr -l on -k on ".modRigName" -type "string" "";
	setAttr -l on -k on ".modRigConnection";
	setAttr -l on ".modControlName" -type "string" "r_Leg_KneeIk_Ctrl";
	setAttr ".isMirrored" 1015;
createNode nurbsCurve -n "r_Leg_KneeIk_Ctrl2Shape" -p "r_Leg_KneeIk_Ctrl2";
	rename -uid "B55D0E7B-475A-E79C-8B37-0F8B53860CB3";
	addAttr -ci true -sn "curveCheck" -ln "curveCheck" -dt "string";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 24 0 no 3
		25 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
		25
		1.60568502e-017 -4.6618055260000002 -0.88574304999999998
		-1.8647222109999999 -2.7970833160000002 9.5249914940000004e-016
		-0.93236110530000005 -2.7970833160000002 5.3869961980000002e-016
		-0.93236110530000005 -0.93236110530000005 0.60603471840000001
		-2.7970833160000002 -0.93236110530000005 1.2830319519999999e-015
		-2.7970833160000002 -1.8647222109999999 1.3246653159999999e-015
		-4.6618055260000002 9.6934663570000002e-017 -0.88574304999999998
		-2.7970833160000002 1.8647222109999999 1.158131862e-015
		-2.7970833160000002 0.93236110530000005 1.1997652249999998e-015
		-0.93236110530000005 0.93236110530000005 0.60603471840000001
		-0.93236110530000005 2.7970833160000002 2.8889943930000001e-016
		-1.8647222109999999 2.7970833160000002 7.0269896879999992e-016
		-1.6271238050000001e-017 4.6618055260000002 -0.88574304999999998
		1.8647222109999999 2.7970833160000002 -9.5249914940000004e-016
		0.93236110530000005 2.7970833160000002 -5.3869961980000002e-016
		0.93236110530000005 0.93236110530000005 0.60603471840000001
		2.7970833160000002 0.93236110530000005 -1.2830319519999999e-015
		2.7970833160000002 1.8647222109999999 -1.3246653159999999e-015
		4.6618055260000002 -4.7495044509999998e-017 -0.88574304999999998
		2.7970833160000002 -1.8647222109999999 -1.158131862e-015
		2.7970833160000002 -0.93236110530000005 -1.1997652249999998e-015
		0.93236110530000005 -0.93236110530000005 0.60603471840000001
		0.93236110530000005 -2.7970833160000002 -2.8889943930000001e-016
		1.8647222109999999 -2.7970833160000002 -7.0269896879999992e-016
		1.60568502e-017 -4.6618055260000002 -0.88574304999999998
		;
	setAttr -l on -k on ".curveCheck" -type "string" "";
createNode displayLayer -n "ControlsLayer";
	rename -uid "71642E70-4163-A46F-34B3-C0ADD77EDB73";
	setAttr ".hpb" yes;
	setAttr ".do" 1;
createNode displayLayerManager -n "layerManager";
	rename -uid "20E77BBB-48B2-8C10-4A52-4F9A70CF5957";
	setAttr ".cdl" 3;
	setAttr -s 14 ".dli[1:13]"  14 2 1 3 4 6 7 8 
		9 10 11 12 13;
	setAttr -s 6 ".dli";
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".o" 0;
	setAttr -av ".unw";
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".msaa" yes;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 16 ".st";
	setAttr -k on ".an";
	setAttr -k on ".pt";
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 24 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 1509 ".u";
select -ne :defaultRenderingList1;
select -ne :defaultTextureList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 7 ".tx";
select -ne :initialShadingGroup;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 4 ".dsm";
	setAttr -k on ".mwc";
	setAttr -k on ".an";
	setAttr -k on ".il";
	setAttr -k on ".vo";
	setAttr -k on ".eo";
	setAttr -k on ".fo";
	setAttr -k on ".epo";
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -k on ".an";
	setAttr -k on ".il";
	setAttr -k on ".vo";
	setAttr -k on ".eo";
	setAttr -k on ".fo";
	setAttr -k on ".epo";
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".macc";
	setAttr -k on ".macd";
	setAttr -k on ".macq";
	setAttr -cb on ".ifg";
	setAttr -k on ".clip";
	setAttr -k on ".edm";
	setAttr -k on ".edl";
	setAttr -av -k on ".esr";
	setAttr -k on ".ors";
	setAttr -cb on ".sdf";
	setAttr ".outf" 51;
	setAttr ".imfkey" -type "string" "exr";
	setAttr -k on ".gama";
	setAttr -cb on ".ar";
	setAttr ".fs" 0.96;
	setAttr ".ef" 9.6;
	setAttr -av -k on ".bfs";
	setAttr -cb on ".me";
	setAttr -cb on ".se";
	setAttr -k on ".be";
	setAttr -k on ".fec";
	setAttr -k on ".ofc";
	setAttr -cb on ".ofe";
	setAttr -cb on ".efe";
	setAttr -cb on ".oft";
	setAttr -cb on ".umfn";
	setAttr -cb on ".ufe";
	setAttr -cb on ".peie";
	setAttr -cb on ".ifp";
	setAttr -k on ".comp";
	setAttr -k on ".cth";
	setAttr -k on ".soll";
	setAttr -k on ".rd";
	setAttr -k on ".lp";
	setAttr -av -k on ".sp";
	setAttr -k on ".shs";
	setAttr -k on ".lpr";
	setAttr -cb on ".gv";
	setAttr -cb on ".sv";
	setAttr -k on ".mm";
	setAttr -k on ".npu";
	setAttr -k on ".itf";
	setAttr -k on ".shp";
	setAttr -cb on ".isp";
	setAttr -k on ".uf";
	setAttr -k on ".oi";
	setAttr -k on ".rut";
	setAttr -av -k on ".mbf";
	setAttr -k on ".afp";
	setAttr -k on ".pfb";
	setAttr -cb on ".prm";
	setAttr -cb on ".pom";
	setAttr -cb on ".pfrm";
	setAttr -cb on ".pfom";
	setAttr -av -k on ".bll";
	setAttr -k on ".bls";
	setAttr -k on ".smv";
	setAttr -k on ".ubc";
	setAttr -k on ".mbc";
	setAttr -cb on ".mbt";
	setAttr -k on ".udbx";
	setAttr -k on ".smc";
	setAttr -k on ".kmv";
	setAttr -cb on ".isl";
	setAttr -cb on ".ism";
	setAttr -cb on ".imb";
	setAttr -k on ".rlen";
	setAttr -av -k on ".frts";
	setAttr -k on ".tlwd";
	setAttr -k on ".tlht";
	setAttr -k on ".jfc";
	setAttr -cb on ".rsb";
	setAttr -k on ".ope";
	setAttr -k on ".oppf";
	setAttr ".hbl" -type "string" "Bakkar";
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av ".w";
	setAttr -av ".h";
	setAttr -av ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av ".dar";
	setAttr -av -k on ".ldar";
	setAttr -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -k on ".isu";
	setAttr -k on ".pdu";
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr ".ctrs" 256;
	setAttr -av ".btrs" 512;
	setAttr -k off ".fbfm";
	setAttr -k off -cb on ".ehql";
	setAttr -k off -cb on ".eams";
	setAttr -k off -cb on ".eeaa";
	setAttr -k off -cb on ".engm";
	setAttr -k off -cb on ".mes";
	setAttr -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -k off -cb on ".mbs";
	setAttr -k off -cb on ".trm";
	setAttr -k off -cb on ".tshc";
	setAttr -k off ".enpt";
	setAttr -k off -cb on ".clmt";
	setAttr -k off -cb on ".tcov";
	setAttr -k off -cb on ".lith";
	setAttr -k off -cb on ".sobc";
	setAttr -k off -cb on ".cuth";
	setAttr -k off -cb on ".hgcd";
	setAttr -k off -cb on ".hgci";
	setAttr -k off -cb on ".mgcs";
	setAttr -k off -cb on ".twa";
	setAttr -k off -cb on ".twz";
	setAttr -k on ".hwcc";
	setAttr -k on ".hwdp";
	setAttr -k on ".hwql";
	setAttr -k on ".hwfr";
	setAttr -k on ".soll";
	setAttr -k on ".sosl";
	setAttr -k on ".bswa";
	setAttr -k on ".shml";
	setAttr -k on ".hwel";
select -ne :ikSystem;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av ".gsn";
	setAttr -k on ".gsv";
	setAttr -s 3 ".sol";
connectAttr "ControlsLayer.di" "l_Arm_Switch_Ctrl1.do";
connectAttr "ControlsLayer.di" "r_Leg_KneeIk_Ctrl2.do";
connectAttr "layerManager.dli[11]" "ControlsLayer.id";
// End of ctrls.ma
