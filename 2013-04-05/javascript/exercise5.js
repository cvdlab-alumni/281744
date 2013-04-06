step2D = SIMPLICIAL_COMPLEX([[0,0],[0,1.56],[1.5,1.56,],[1.5,1.56]])([[0,2,1],[1,2,3]])

step3D = MAP([S0,S2,S1])(EXTRUDE([4.5])(step2D));
ramp = STRUCT(REPLICA(7)([step3D,T([0,2])([1.5,1.56])]))

DRAW(ramp);