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

baseInf = CUBOID([7,5,3.4])

domain = GRID([25,25])

bracciolo1 = [[0,0,0],[0,0,7],[0,0,7],[0,0,7],[0,5,7],[0,5,7],[0,5,7],[0,5,12],[0,5,12],[0,5,12],[0,8,12],[0,8,12],[0,8,12],[0,8,0],[0,8,0],[0,8,0],[0,0,0]]
bracciolo2 = [[1,0,0],[1,0,7],[1,0,7],[1,0,7],[1,5,7],[1,5,7],[1,5,7],[1,5,12],[1,5,12],[1,5,12],[1,8,12],[1,8,12],[1,8,12],[1,8,0],[1,8,0],[1,8,0],[1,0,0]]

bracc1=MAP(BEZIER(S2)([BEZIER(S1)(bracciolo1),BEZIER(S1)(bracciolo2)]))(domain)
bracc2=MAP(BEZIER(S2)([BEZIER(S1)(bracciolo1),BEZIER(S1)([[0,6,6]])]))(domain)
bracc3=MAP(BEZIER(S2)([BEZIER(S1)(bracciolo2),BEZIER(S1)([[1,6,6]])]))(domain)

bracciolo = STRUCT([bracc1,bracc2,bracc3])

schienale1 = [[0,0,0],[0,0,4.5],[0,0,4.5],[0,0,4.5],[0,2,11],[0,2,11],[0,2,11],[0,3,11],[0,3,11],[0,3,11],[0,3,0],[0,3,0],[0,3,0],[0,0,0]]
schienale2 = [[7,0,0],[7,0,4.5],[7,0,4.5],[7,0,4.5],[7,2,11],[7,2,11],[7,2,11],[7,3,11],[7,3,11],[7,3,11],[7,3,0],[7,3,0],[7,3,0],[7,0,0]]
schienale=MAP(BEZIER(S2)([BEZIER(S1)(schienale2),BEZIER(S1)(schienale1)]))(domain)

pointcusc1 = [[0,0,0],[0,2.5,-0.4],[0,5,0],[0,5,0],[0,5.2,0.75],[0,5,1.5],[0,5,1.5],[0,2.5,1.9],[0,0,1.5],[0,0,1.5],[0,-0.2,0.75],[0,0,0]]
pointcusc2 = [[7,0,0],[7,2.5,-0.4],[7,5,0],[7,5,0],[7,5.2,0.75],[7,5,1.5],[7,5,1.5],[7,2.5,1.9],[7,0,1.5],[7,0,1.5],[7,-0.2,0.75],[7,0,0]]
cusc1=MAP(BEZIER(S2)([BEZIER(S1)(pointcusc1),BEZIER(S1)(pointcusc2)]))(domain)
cusc2=MAP(BEZIER(S2)([BEZIER(S1)(pointcusc1),BEZIER(S1)([[0,2.5,0.75]])]))(domain)
cusc3=MAP(BEZIER(S2)([BEZIER(S1)(pointcusc2),BEZIER(S1)([[7,2.5,0.75]])]))(domain)
cuscino = STRUCT([cusc1,cusc2,cusc3])

poltrona = S([3])([0.8])(COLOR(rgb01(175,89,67))(STRUCT([T([1,3])([1,3.5])(cuscino),bracciolo,T([1])([8])(bracciolo),T([1])([1])(baseInf),T([1,2])([1,5])(schienale)])))

VIEW(poltrona)
