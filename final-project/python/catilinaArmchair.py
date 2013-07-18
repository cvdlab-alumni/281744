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

base1= [[0,0,0],[-0.5,0.7,0],[0,1.9,0],[0.7,2.2,0],[1.3,2.2,0],[2,1.9,0],[2.5,0.7,0],[2,0,0]]
base2= [[-0.1,-0.2,0],[-0.75,0.7,0],[-0.1,2.1,0],[0.7,2.4,0],[1.3,2.4,0],[2.1,2.1,0],[2.75,0.7,0],[2.1,-0.2,0]]


base3= [[0,0,-0.1],[-0.5,0.7,-0.1],[0,1.9,-0.1],[0.7,2.2,-0.1],[1.3,2.2,-0.1],[2,1.9,-0.1],[2.5,0.7,-0.1],[2,0,-0.1]]
base4= [[-0.1,-0.2,-0.1],[-0.75,0.7,-0.1],[-0.1,2.1,-0.1],[0.7,2.4,-0.1],[1.3,2.4,-0.1],[2.1,2.1,-0.1],[2.75,0.7,-0.1],[2.1,-0.2,-0.1]]


base5= [[0,0,0],[-0.1,-0.2,0]]
base6= [[0,0,-0.1],[0,0,-0.1],[-0.1,-0.2,-0.1]]
base7= [[2,0,-0.1],[2,0,-0.1],[2.1,-0.2,-0.1]]
base8= [[2,0,0],[2,0,0],[2.1,-0.2,0]]


bas1=MAP(BEZIER(S2)([BEZIER(S1)(base1),BEZIER(S1)(base2)]))(domain)
bas2=MAP(BEZIER(S2)([BEZIER(S1)(base3),BEZIER(S1)(base4)]))(domain)
bas3=MAP(BEZIER(S2)([BEZIER(S1)(base1),BEZIER(S1)(base3)]))(domain)
bas4=MAP(BEZIER(S2)([BEZIER(S1)(base2),BEZIER(S1)(base4)]))(domain)
bas5=MAP(BEZIER(S2)([BEZIER(S1)(base7),BEZIER(S1)(base8)]))(domain)
bas6=MAP(BEZIER(S2)([BEZIER(S1)(base5),BEZIER(S1)(base6)]))(domain)

base = COLOR(rgb01(0,0,0))(S([1,2])([1.05,1.18])(STRUCT([bas1,bas2,bas3,bas4,bas5,bas6])))

bar =COLOR([0,0,0])(S([1,2])([0.5,0.5])(CYLINDER([0.1,3.5])(20)))
hor_bar = COLOR([0,0,0])(R([1,3])(-PI/2)(S([0,1])([0.5,0.5])(CYLINDER([0.1,2.5])(20))))

puntiCuscino = [[0,0,0.9],[1,0,0.9],[1,0,0.5],[1,0,0.1],[0,0,0.1]]

cuscino= COLOR(rgb01(106,18,30))(MAP(ROTATIONALSURFACE(BEZIER(S1)(puntiCuscino)))(domainRot))


profile1 = BEZIER(S1)([[2.2,0,1],[2.35,0,1],[2.5,0,0.75],[2.35,0,0.5],[2.2,0,0.5]]);
mapping1 = ROTATIONALSURFACE(profile1)
toro = S([1,2,3])([0.6,0.55,0.3])(COLOR([0,0,0])(MAP(mapping1)(domainRot)))

parteSup1 = [[-0.2,0,-0.15],[0,0,-0.15],[0,0,0],[-0.3,0.5,0],[0.6,0.8,0.3],[1.5,0.8,0.3],[2.3,0.5,0],[2,0,0],[2,0,-0.15],[2.2,0,-0.15]]
parteSup2 = [[-0.2,0,-0.2],[-0.2,0,0],[-0.5,0.5,0],[0.6,0.8,0.5],[1.5,0.8,0.5],[2.5,0.5,0],[2.2,0,0],[2.2,0,-0.2]]

superiore=MAP(BEZIER(S2)([BEZIER(S1)(parteSup1),BEZIER(S1)(parteSup2)]))(domain)

surfaceSup = S([1,2])([1.15,3.65])(COLOR([0,0,0])(superiore))

model = STRUCT([S([3])([1.08])(T([1,2])([1,2.3])(bar)),T([1,2])([-0.3,0.3])(bar),T([1,2])([2.3,0.3])(bar),T([1])([-0.05])(base),S([1,2])([1.55,1.45])(T([1,2,3])([0.65,0.7,1.6])(cuscino)),T([1,2,3])([1,1,1.7])(toro),T([1,2,3])([-0.25,0.3,1.8])(hor_bar),T([1,2,3])([-0.15,0.15,3.55])(surfaceSup)])

VIEW(model)
