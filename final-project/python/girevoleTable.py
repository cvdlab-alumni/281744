from pyplasm import*;
import sys
sys.path.append("/home/carlodemedio/larpy")


from lar import *

def GRID(args):
	model = ([[]],[[0]])
	for k,steps in enumerate(args):
		model = larExtrude(model,steps*[1])
	V,cells = model
	verts = AA(list)(scipy.array(V)/AA(float)(args))
	return MKPOL([verts,AA(AA(lambda h:h+1))(cells),None])

def rgb01(r, g, b):
    r0 = r/255.0;
    g0 = g/255.0;
    b0 = b/255.0;
    return [r0, g0, b0]


domain = GRID([25,25])
domainRot = PROD([INTERVALS(1)(10),INTERVALS(2*PI)(30)]);

base1= [[0,0,0],[-0.3,0.7,0],[0,1.9,0],[0.7,2.2,0],[1.3,2.2,0],[2,1.9,0],[2.3,0.75,0],[2,0,0],[2,0,0],[2,0,0],[2,0,0],[0.9,0.7,0],[0,0,0]]
base2= [[0,0,0.5],[-0.3,0.7,0.5],[0,1.9,0.5],[0.7,2.2,0.5],[1.3,2.2,0.5],[2,1.9,0.5],[2.3,0.75,0.5],[2,0,0.5],[2,0,0.5],[2,0,0.5],[0.9,0.7,0.5],[0,0,0.5]]

rotator1 = T([1,2])([3.8,4])(S([1])([1.5])(CYLINDER([ 1, 1 ])(36)))
rotator2 = T([1,2])([3.8,4])(S([2])([1.5])(CYLINDER([ 1, 1 ])(36)))
bas1=MAP(BEZIER(S2)([BEZIER(S1)(base1),BEZIER(S1)([[1,1,0]])]))(domain)
bas2=MAP(BEZIER(S2)([BEZIER(S1)(base2),BEZIER(S1)([[1,1,0.5]])]))(domain)
bas12=MAP(BEZIER(S2)([BEZIER(S1)(base1),BEZIER(S1)(base2)]))(domain)

semiluna = S([1,2])([3.5,3.2])(STRUCT([bas1,bas2,bas12]))

girevoleTable = STRUCT([semiluna,T([1,3])([-0.5,0.5])(rotator2),T([1,3])([6.5,1.5])(R([1,2])(PI/2)(semiluna)),T([1,2,3])([5,-1.7,2])(R([1,2])(PI/3)(rotator1)),T([1,3])([3.5,3])(R([1,2])(PI/4)(semiluna))])

model = S([3])([0.7])(COLOR(rgb01(59,51,50))(girevoleTable))
VIEW(model)
