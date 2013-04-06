from pyplasm import *;

##es1
GRID = COMP([INSR(PROD),AA(QUOTE)])

pillar = CYLINDER([ 0.5, 10 ])(36)
pillars0round = STRUCT(NN(5)([pillar,T([1])([10])]))
pillars0square = GRID([[-4.5,1,-3.5,1,-9,1,-9,1],[1],[10]  ])

pillars2square = GRID([[1,-9,1,-29,1],[1],[10]  ])
pillars22square = GRID([[1,-8.5,1,-9,1,-9,1,-9.5,1],[1],[10]  ])


pillars1square =  T([1,2,3])([-0.5,-0.5,10])(GRID([[1,-9,1,-9,1,-9,1,-9,1],[1],[10]]))
pillars12square = T([1,2,3])([-1,19.5,10])(GRID([[-0.5,1,-8.5,1,-9,1,-9,-10.5,1],[1],[10]]))
pillarSmall = CUBOID([0.5,0.5,10])

pillars3square = GRID([[-20,1,-19,1],[1],[10]  ])
pillars33square = GRID([[-20,1,-9,1,-9.5,1],[1],[10]  ])

pillars0 = STRUCT([pillars0round,T([2])([20])(pillar),T([2])([19.5])(pillars0square)])
pillars3 = T([1,2,3])([-0.5,-0.5,30])(STRUCT([pillars3square,T([1,2])([-0.5,20])(pillars33square),T([1,2])([9.5,20.5])(pillarSmall),T([2])([20.5])(pillarSmall),T([1,2])([40,24])(S([1,2])([2,2])(pillarSmall))]))
pillars1 = STRUCT([pillars1square,pillars12square,T([1,2,3])([2,19.5,10])(pillarSmall),T([1,2,3])([29.5,20,10])(pillar)])
pillars2 = T([1,2,3])([-0.5,-0.5,20])(STRUCT([pillars2square,T([2])([20])(pillars22square)]))
pillars = STRUCT([pillars0, pillars1,pillars2,pillars3])

buildings = STRUCT([pillars])
VIEW(buildings);
