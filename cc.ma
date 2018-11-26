//Maya ASCII 2016 scene
//Name: cc.ma
//Last modified: Thu, Nov 08, 2018 03:58:25 PM
//Codeset: 936
requires maya "2016";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2016";
fileInfo "version" "2016";
fileInfo "cutIdentifier" "201603180400-990260";
fileInfo "osv" "Microsoft Windows 8 Enterprise Edition, 64-bit  (Build 9200)\n";
createNode transform -n "ROOT_Ctrl4";
	rename -uid "97CB328A-4929-D377-665E-269E646A3ABF";
	addAttr -ci true -sn "parentControl" -ln "parentControl" -min 0 -max 1 -at "bool";
	addAttr -ci true -sn "modCoreName" -ln "modCoreName" -dt "string";
	addAttr -ci true -sn "isROOT" -ln "isROOT" -dt "string";
	addAttr -ci true -sn "isROOT_Ctrl" -ln "isROOT_Ctrl" -dt "string";
	addAttr -ci true -sn "modRigName" -ln "modRigName" -dt "string";
	addAttr -ci true -sn "modRigConnection" -ln "modRigConnection" -dt "string";
	addAttr -ci true -sn "modControlName" -ln "modControlName" -dt "string";
	addAttr -ci true -sn "controlSizeX" -ln "controlSizeX" -dv 1 -at "double";
	addAttr -ci true -sn "controlSizeY" -ln "controlSizeY" -dv 1 -at "double";
	addAttr -ci true -sn "controlSizeZ" -ln "controlSizeZ" -dv 1 -at "double";
	addAttr -ci true -sn "isMirrored" -ln "isMirrored" -dv 1 -at "double";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 53.340307311262038 48.923508163625982 ;
	setAttr -k on ".parentControl";
	setAttr -l on -k on ".modCoreName" -type "string" "ROOT_Ctrl";
	setAttr -l on -k on ".isROOT" -type "string" "ROOT_Ctrl";
	setAttr -l on -k on ".isROOT_Ctrl";
	setAttr -l on -k on ".modRigName" -type "string" "";
	setAttr -l on -k on ".modRigConnection";
	setAttr -l on ".modControlName" -type "string" "ROOT_Ctrl";
	setAttr -l on -k on ".controlSizeX";
	setAttr -l on -k on ".controlSizeY";
	setAttr -l on -k on ".controlSizeZ";
	setAttr ".isMirrored" 1015;
createNode nurbsCurve -n "ROOT_Ctrl4Shape" -p "ROOT_Ctrl4";
	rename -uid "D3EB5358-4E0B-5B95-4A8E-848FD57F0E39";
	addAttr -ci true -sn "curveCheck" -ln "curveCheck" -dt "string";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		14.00712996 8.5768934370000008e-016 -14.00712996
		-2.25997839e-015 1.2129559020000001e-015 -19.809073160000001
		-14.00712996 8.5768934370000008e-016 -14.00712996
		-19.809073160000001 3.5148427470000006e-031 -5.7401738190000001e-015
		-14.00712996 -8.5768934370000008e-016 14.00712996
		-5.9688603399999997e-015 -1.2129559020000001e-015 19.809073160000001
		14.00712996 -8.5768934370000008e-016 14.00712996
		19.809073160000001 -6.5148098120000012e-031 1.0639491839999999e-014
		14.00712996 8.5768934370000008e-016 -14.00712996
		-2.25997839e-015 1.2129559020000001e-015 -19.809073160000001
		-14.00712996 8.5768934370000008e-016 -14.00712996
		;
	setAttr -l on -k on ".curveCheck" -type "string" "";
createNode nurbsCurve -n "ROOT_Ctrl42Shape" -p "ROOT_Ctrl4";
	rename -uid "4DFB4115-4294-F366-C809-FDBD1056F7B3";
	addAttr -ci true -sn "curveCheck" -ln "curveCheck" -dt "string";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 0 no 3
		13 0 0 0 1 2 3 4 5 6 7 8 8 8
		11
		7.1379147100000004 1.1421221379999999e-015 17.232450499999999
		11.008206530000001 1.1421221379999999e-015 15.62932314
		17.829787570000001 9.5514076740000008e-016 9.4984983159999992
		19.78243505 2.4105821870000002e-016 -3.9330135049999999
		12.803703479999999 -5.824717876e-016 -15.59970848
		1.7256816360000001e-015 -1.1415269629999999e-015 -20.178550779999998
		-12.803703479999999 -1.182519964e-015 -15.59970848
		-19.78243505 -6.8604963659999997e-016 -3.9330135049999999
		-17.829787570000001 1.1954413490000001e-016 9.4984983159999992
		-11.008206530000001 6.2622029340000006e-016 15.62932314
		-7.1379147100000004 8.0760230900000001e-016 17.232450499999999
		;
	setAttr -l on -k on ".curveCheck" -type "string" "";
createNode nurbsCurve -n "ROOT_Ctrl43Shape" -p "ROOT_Ctrl4";
	rename -uid "745F6614-4672-F220-8920-388C531FDC36";
	addAttr -ci true -sn "curveCheck" -ln "curveCheck" -dt "string";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 4 0 no 3
		5 0 1 2 3 4
		5
		7.1383480830000003 0 17.232816719999999
		7.1383480830000003 0 19.154249230000001
		0 0 22.615317820000001
		-7.1383480830000003 0 19.154249230000001
		-7.1383480830000003 0 17.232816719999999
		;
	setAttr -l on -k on ".curveCheck" -type "string" "";
createNode transform -n "ROOTSecondary_Ctrl6";
	rename -uid "77C3A7A1-49FE-0FF0-FFE3-109FCCF37FD0";
	addAttr -ci true -sn "modCoreName" -ln "modCoreName" -dt "string";
	addAttr -ci true -sn "isROOT" -ln "isROOT" -dt "string";
	addAttr -ci true -sn "modRigName" -ln "modRigName" -dt "string";
	addAttr -ci true -sn "modRigConnection" -ln "modRigConnection" -dt "string";
	addAttr -ci true -sn "modControlName" -ln "modControlName" -dt "string";
	addAttr -ci true -sn "controlSizeX" -ln "controlSizeX" -dv 1 -at "double";
	addAttr -ci true -sn "controlSizeY" -ln "controlSizeY" -dv 1 -at "double";
	addAttr -ci true -sn "controlSizeZ" -ln "controlSizeZ" -dv 1 -at "double";
	addAttr -ci true -sn "isMirrored" -ln "isMirrored" -dv 1 -at "double";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 53.340307311262038 43.822284424449464 ;
	setAttr -l on -k on ".modCoreName" -type "string" "ROOT_Ctrl";
	setAttr -l on -k on ".isROOT" -type "string" "ROOTSecondary_Ctrl";
	setAttr -l on -k on ".modRigName" -type "string" "";
	setAttr -l on -k on ".modRigConnection";
	setAttr -l on ".modControlName" -type "string" "ROOTSecondary_Ctrl";
	setAttr -l on -k on ".controlSizeX";
	setAttr -l on -k on ".controlSizeY";
	setAttr -l on -k on ".controlSizeZ";
	setAttr ".isMirrored" 1015;
createNode nurbsCurve -n "ROOTSecondary_Ctrl6Shape" -p "ROOTSecondary_Ctrl6";
	rename -uid "E8FA690E-4B6C-A383-DCF8-2F8BC4DD9A66";
	addAttr -ci true -sn "curveCheck" -ln "curveCheck" -dt "string";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		9.744090409 -0.46630675030000002 -9.744090409
		-1.5721588799999999e-015 -0.46630675030000002 -13.78022481
		-9.744090409 -0.46630675030000002 -9.744090409
		-13.78022481 -0.46630675030000002 -3.9931643959999999e-015
		-9.744090409 -0.46630675030000002 9.744090409
		-4.1522506720000001e-015 -0.46630675030000002 13.78022481
		9.744090409 -0.46630675030000002 9.744090409
		13.78022481 -0.46630675030000002 7.401385627e-015
		9.744090409 -0.46630675030000002 -9.744090409
		-1.5721588799999999e-015 -0.46630675030000002 -13.78022481
		-9.744090409 -0.46630675030000002 -9.744090409
		;
	setAttr -l on -k on ".curveCheck" -type "string" "";
createNode nurbsCurve -n "ROOTSecondary_Ctrl62Shape" -p "ROOTSecondary_Ctrl6";
	rename -uid "F17469B4-487D-4CF0-88AB-BE8DED9B9BD4";
	addAttr -ci true -sn "curveCheck" -ln "curveCheck" -dt "string";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 20 0 no 3
		21 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
		21
		6.9777054070000002 -0.46630675030000002 10.24639138
		7.1164472090000004 -0.46630675030000002 10.99944569
		6.7710848859999997 -0.46630675030000002 11.28942632
		6.0577443630000003 -0.46630675030000002 11.835813480000001
		4.9292820270000002 -0.46630675030000002 12.54742867
		3.7646342879999999 -0.46630675030000002 13.24845869
		2.5654798479999998 -0.46630675030000002 13.84864211
		1.4239857929999999 -0.46630675030000002 14.339834099999999
		0.55119789419999998 -0.46630675030000002 14.675994640000001
		0 -0.46630675030000002 14.866434310000001
		0 -0.46630675030000002 12.437147120000001
		0 -0.46630675030000002 14.866434310000001
		-0.55119789419999998 -0.46630675030000002 14.675994640000001
		-1.4239857929999999 -0.46630675030000002 14.339834099999999
		-2.5654798479999998 -0.46630675030000002 13.84864211
		-3.7646342879999999 -0.46630675030000002 13.24845869
		-4.9292820270000002 -0.46630675030000002 12.54742867
		-6.0577443630000003 -0.46630675030000002 11.835813480000001
		-6.7710848859999997 -0.46630675030000002 11.28942632
		-7.1164472090000004 -0.46630675030000002 10.99944569
		-6.9777054070000002 -0.46630675030000002 10.24639138
		;
	setAttr -l on -k on ".curveCheck" -type "string" "";
createNode nurbsCurve -n "ROOTSecondary_Ctrl63Shape" -p "ROOTSecondary_Ctrl6";
	rename -uid "3B5B4ABA-42AD-0D73-A956-9D8ABFD210AF";
	addAttr -ci true -sn "curveCheck" -ln "curveCheck" -dt "string";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 2 0 no 3
		3 0 1 2
		3
		12.32974113 -0.46630675030000002 -1.30430972
		11.123700899999999 -0.46630675030000002 0
		12.32974113 -0.46630675030000002 1.30430972
		;
	setAttr -l on -k on ".curveCheck" -type "string" "";
createNode nurbsCurve -n "ROOTSecondary_Ctrl64Shape" -p "ROOTSecondary_Ctrl6";
	rename -uid "5575B3ED-4C98-9A25-136D-009E0F6F4AF8";
	addAttr -ci true -sn "curveCheck" -ln "curveCheck" -dt "string";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 2 0 no 3
		3 0 1 2
		3
		-1.30430972 -0.46630675030000002 -12.32974113
		2.4699577709999999e-015 -0.46630675030000002 -11.123700899999999
		1.30430972 -0.46630675030000002 -12.32974113
		;
	setAttr -l on -k on ".curveCheck" -type "string" "";
createNode nurbsCurve -n "ROOTSecondary_Ctrl65Shape" -p "ROOTSecondary_Ctrl6";
	rename -uid "2C02C5D6-4EEE-7C4E-04D3-AC9161D25C78";
	addAttr -ci true -sn "curveCheck" -ln "curveCheck" -dt "string";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 17;
	setAttr ".cc" -type "nurbsCurve" 
		1 2 0 no 3
		3 0 1 2
		3
		-12.32974113 -0.46630675030000002 1.30430972
		-11.123700899999999 -0.46630675030000002 -6.3021760130000003e-015
		-12.32974113 -0.46630675030000002 -1.30430972
		;
	setAttr -l on -k on ".curveCheck" -type "string" "";
createNode displayLayer -n "ControlsLayer";
	rename -uid "71642E70-4163-A46F-34B3-C0ADD77EDB73";
	setAttr ".hpb" yes;
	setAttr ".do" 1;
createNode displayLayerManager -n "layerManager";
	rename -uid "EB04738F-47EF-5543-571C-F8B8B417E425";
	setAttr ".cdl" 3;
	setAttr -s 14 ".dli[1:13]"  14 2 1 3 4 6 7 8 
		9 10 11 12 13;
	setAttr -s 4 ".dli";
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
	setAttr -s 2 ".st";
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
	setAttr -s 4 ".s";
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
	setAttr -s 1476 ".u";
select -ne :defaultRenderingList1;
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
	setAttr -s 2 ".sol";
connectAttr "ControlsLayer.di" "ROOT_Ctrl4.do";
connectAttr "ControlsLayer.di" "ROOTSecondary_Ctrl6.do";
connectAttr "layerManager.dli[11]" "ControlsLayer.id";
// End of cc.ma
