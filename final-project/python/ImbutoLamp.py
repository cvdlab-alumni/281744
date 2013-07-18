from pyplasm import *



def rgb01(r, g, b):
    r0 = r/255.0;
    g0 = g/255.0;
    b0 = b/255.0;
    return [r0, g0, b0]


domain = PROD([INTERVALS(1)(10),INTERVALS(2*PI)(20)]);




pointsup = [[0.2,0,0],[1,0,1.5],[2,0,3]]
profile = BEZIER(S1)(pointsup)
lamp = COLOR([0.4,0.4,0.4])(MAP(ROTATIONALSURFACE(profile))(domain))


bar = COLOR(rgb01(246,172,0))(CYLINDER([0.2,19])(30))

base = COLOR([0.4,0.4,0.4])(CYLINDER([ 2, 0.5 ])(36))
lampada = STRUCT([bar,T([3])([19])(lamp),base])
VIEW(lampada)
