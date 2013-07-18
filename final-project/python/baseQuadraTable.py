from pyplasm import *;
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
	
domain = GRID([25,25])

def rgb01(r, g, b):
    r0 = r/255.0;
    g0 = g/255.0;
    b0 = b/255.0;
    return [r0, g0, b0]


base= COLOR(rgb01(47,51,53))(CUBOID([6,6,0.1]))

pointsb1= [[-1,-1,-1],[-0.25,-0.25,-0.5],[0,0,0]]
bez1 = BEZIER(S1)(pointsb1);
curveb1 = MAP(bez1)(domain);

pointsb2= [[5,-1,-1],[4.25,-0.25,-0.5],[4,0,0]]
bez2 = BEZIER(S1)(pointsb2);
curveb2 = MAP(bez2)(domain);

pointsb3= [[-1,5,-1],[-0.25,4.25,-0.5],[0,4,0]]
bez3 = BEZIER(S1)(pointsb3);
curveb3 = MAP(bez3)(domain);

pointsb4= [[5,5,-1],[4.25,4.25,-0.5],[4,4,0]]
bez4 = BEZIER(S1)(pointsb4);
curveb4 = MAP(bez4)(domain);

sur1 = BEZIER(S2)([bez1,bez2])
surface1 = MAP(sur1)(domain)

sur2 = BEZIER(S2)([bez1,bez3])
surface2 = MAP(sur2)(domain)

sur3 = BEZIER(S2)([bez3,bez4])
surface3 = MAP(sur3)(domain)

sur4 = BEZIER(S2)([bez2,bez4])
surface4 = MAP(sur4)(domain)


pointsb11= [[0,0,0],[1.5,1.5,2],[0,0,4]]
bez11 = BEZIER(S1)(pointsb11);
curveb11 = MAP(bez11)(domain);


pointsb12= [[4,0,0],[2.5,1.5,2],[4,0,4]]
bez12 = BEZIER(S1)(pointsb12);
curveb12 = MAP(bez12)(domain);

pointsb13= [[0,4,0],[1.5,2.5,2],[0,4,4]]
bez13 = BEZIER(S1)(pointsb13);
curveb13 = MAP(bez13)(domain);

pointsb14= [[4,4,0],[2.5,2.5,2],[4,4,4]]
bez14 = BEZIER(S1)(pointsb14);
curveb14 = MAP(bez14)(domain);

sur12 = BEZIER(S2)([bez11,bez12])
surface12 = MAP(sur12)(domain)

sur13 = BEZIER(S2)([bez11,bez13])
surface13 = MAP(sur13)(domain)

sur34 = BEZIER(S2)([bez13,bez14])
surface34 = MAP(sur34)(domain)

sur24 = BEZIER(S2)([bez12,bez14])
surface24 = MAP(sur24)(domain)

baseSup = STRUCT([surface12,surface24,surface34,surface13])
baseInf = STRUCT([surface1,surface2,surface3,surface4])

baseCompleta = STRUCT([COLOR(rgb01(198,198,197))(baseInf),COLOR(rgb01(47,51,53))(baseSup),T([1,2,3])([-1,-1,-1.1])(base)])


domainRot = PROD([INTERVALS(1)(36),INTERVALS(2*PI)(36)])

profile = BEZIER(S1)([[0,0,4.2],[2.5,0,4.2],[5,0,4.2]]);
mapping = ROTATIONALSURFACE(profile);
surface = MAP(mapping)(domainRot);
coloredSurface = COLOR(rgb01(230,145,0))(surface)

profile2 = BEZIER(S1)([[5,0,4.2],[5.2,0,4.1],[5,0,4]]);
mapping2 = ROTATIONALSURFACE(profile2);
surfaceTor = MAP(mapping2)(domainRot);
parteSupCompleta =  STRUCT([COLOR(rgb01(47,51,53))(surfaceTor),coloredSurface])
model = STRUCT([T([1,2])([2,2])(parteSupCompleta),baseCompleta])
VIEW(model)
