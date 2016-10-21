from pyplasm import *

def fun(xPil,yPil,xBeam,zBeam,ldy,lhz):

	pilx=QUOTE([xPil,0])
	pily=QUOTE([yPil,0])
	height=0
	pillar=PROD([pilx,pily])
	pillarS=STRUCT([QUOTE([0])])
	for h in lhz:
		newPillar=PROD([pillar,QUOTE([h])])
		pillarS=STRUCT([pillarS,T(3)(-height)(newPillar)])
		dist=0	
		for d in ldy:
			dist=-d-xPil+dist
			pillarS=STRUCT([pillarS,T([1,3])([-dist,-height])(newPillar)])
		height=height-h-xBeam
		

	beamx=QUOTE([xBeam,0])
	beamz=QUOTE([zBeam,0])
	beamS=STRUCT([QUOTE([0])])
	height=0
	a=0
	for h in lhz: 
		height=height-h-a
		dist = 0
		for d in ldy:
			newBeam=PROD([PROD([QUOTE([d+xPil]),beamz]),beamx])
			beamS=STRUCT([beamS,T([1,3])([-dist,-height])(newBeam)])	
			dist=dist-d-xPil
		a=xBeam
	struct=STRUCT([pillarS,beamS])
	return struct
	
#struttura=fun(0.02,0.03,0.02,0.03,[0.2,0.1,0.2,0.1,0.4,0.7],[0.4,0.5,0.3,0.8])
#VIEW(struttura)


	
	
