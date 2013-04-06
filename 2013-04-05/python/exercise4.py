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

##buildings = STRUCT([pillars])
##VIEW(buildings);

##es2




floor10 = T(1)(-0.5)(GRID([ [41],[20],[1]  ]))
floor11 = GRID([ [3],[-20,5],[1]])
floor12 = GRID([ [-17,23],[-20,5],[1]])



floor30 = GRID([   [20],[25],[1]])
floor31 = GRID([   [-19,14],[20],[1]])
floor32 = GRID([ [-33,8],[25],[1]])

balcony = T([1])([-4])(GRID([ [4],[-20,5],[1]]))


floor41= T([1,2,3])([-0.5,-0.5,40])(GRID([ [-19.5,21.5],[25.5],[1]]))
floor42 = T([1,2,3])([-0.5,-0.5,40])(GRID([ [19.5],[-20,5.5],[1]]))



##floor0 = PROD([STRUCT([curva1,curva2,floor01]),Q(1)])
dom = PROD([INTERVALS(PI)(32),INTERVALS(PI)(32)])

def circle(R,r):
    def circle0(p):
        u,v = p;
        return (r*COS(u)+R)*COS(v),(r*COS(u)+R)*SIN(v);
    return MAP(circle0)(dom)


floor01 = R([1,2])(-PI/2)(circle(5,0.5));
floor02 = R([1,2])(PI)(circle(1.5,0.5));

floor03 = PROD([SOLIDIFY(POLYLINE([ [29.5,25],[-0.5,25],[-0.5,19.5],[5,19.5],[5,8],[29.5,8],[29.5,25]])),Q(1)])
floor03 = GRID([[31],[-24,1]])
floor04 = GRID([ [1],[-19.5,5] ])
floor05 = GRID([ [5],[-19.5,1] ])
floor07 = GRID([[-4,1],[-8,12] ])
floor06 = T(2)(8)(GRID([ [-7,24],[1] ]))
floor08 = GRID([[-30,1],[-9,5]])


floor04 =T(2)(-19.5)(STRUCT([   floor08,floor07,floor06,floor04,floor05,floor03,T([1,2])([29.5,19.5])(floor01)  , T([1,2])([6,8])(floor02)]))
floor0= T([2])([19])(PROD([floor04,Q(10)]))

floor1 = T([1,2,3])([-0.5,-0.5,10])(STRUCT([floor30,floor31,floor32,balcony]))
floor2 = T([2,3])([-0.5,20])(STRUCT([floor10,floor11,floor12]))
floor3 = T([1,2,3])([-0.5,-0.5,30])(STRUCT([floor30,floor31,floor32]))
floor4 = STRUCT([floor41,floor42])

##buildings = STRUCT([floor0,floor1,pillars,floor2,floor3,floor4]);
##VIEW(buildings);

##es3

est0 = GRID([ [20],[1],[20,-10,1]])
est1 = GRID([[-20,1],[1],[31]])
est2 = GRID([ [-21,9],[1],[6.5,-4,3,-4,3,-4,6.5]])
est3 = GRID([ [-30,11],[1],[31]])
est4 = GRID([[1],[1],[31]])
est5 = GRID([[20,-20],[1],[23]])

north0 = GRID([ [1],[10],[31]])
north1 = T(1)(18)(north0);
north2 = GRID([[14],[1],[5.5,-5,3,-5,3,-5,4.5]])
north3 = GRID([[-14,2],[1],[31] ] )
north4 = GRID([[-16,2],[1],[1,-9,1,-9,1,-9,1]])
north5 = S([2])([1])(GRID([[1],[1],[10]]))

west0 = T([1,2,3])([40,24-0.5,10])(R([1,2])(PI/2)(GRID([ [1],[10],[31]])))
west1 = GRID([[3,-10,17],[1],[40]])
west2 = GRID([[20],[1],[5]])
west3 = GRID([[20],[1],[5,-3,7,-5,5,-5,10]])
west4 = T([1,3])([8,5])(GRID([[10],[1],[3]]))
west5 = T([1,3])([7.5,15])(GRID([[1],[1],[9]]))
west6 = T([1,3])([3.5,25])(GRID([[1,-0.5,10],[1],[9]]))
west7 = T([1,3])([-10.5,10])(S([1])([1.3])(GRID([[10.5],[1],[30]])))

south0 = T([3])([10])(GRID([[25],[1],[3,-7,1]]))
south1 = GRID([[5],[1],[10]])


northwall = S([2])([1.33])(T([1,2,3])([41,-0.5,10])(R([1,2])(PI/2)(STRUCT([north0,north2,north3,north4,T([1,3])([18,-10])(north5),T([1])([18])(north5),T([1,3])([18,10])(north5),T([1,3])([18,20])(S([3])([1.1])(north5))]))))
estwall = T([1,2,3])([-0.5,-0.5,10])(STRUCT([est0,est1,est2,est3,est4,est5]))
westwall= T([1,2])([29.5,25])(R([1,2])(PI)(STRUCT([west1,west2,west3,west4,west5,west6,west7])))
southwall = T([1,2,3])([-0.5,24.5,20])(R([1,2])(-PI/2)(STRUCT([south0,south1])))

##buildings = STRUCT([floor0,floor1,pillars,floor2,floor3,floor4,estwall,northwall,westwall,southwall]);

##VIEW(buildings);

##es4

windowest1 = COLOR([0,0,0])(GRID([  [0.2],[1],[3.6] ]))
windowest2 = COLOR([0,0,0])(GRID([  [9],[1],[0.2] ]))
window1 = STRUCT([T(3)(0.2)(windowest1),T(3)(0.2)(windowest2),T(3)(3.8)(windowest2),T([1,3])([4.4,0.2])(windowest1),T([1,3])([8.8,0.2])(windowest1)])
estwindows = T([1,2,3])([20.5,-1,16.5])(STRUCT([T(3)(-0.3)(window1),T(3)(6.9)(window1),T(3)(14.2)(window1)]))


windownorth1= COLOR([0,0,0])(GRID([[0.2],[1],[4.6]]))
windownorth2 = COLOR([0,0,0])(GRID([[13],[1],[0.2]]))
window2 = S([2])([0.95])(T([1,2,3])([41,-17,16.5])(R([1,2])(PI/2)(STRUCT([  T(3)(-0.8)(windownorth1),T([1,3])([6.9,-0.8])(windownorth1),T([1,3])([12.8,-0.8])(windownorth1),T(3)(-1)(windownorth2),T(3)(3.8)(windownorth2)  ]))))

windownorth3 = COLOR([0,0,0])(GRID([  [0.2],[1],[9] ]) )
windownorth4 = COLOR([0,0,0])(GRID([  [1.6],[1],[0.2] ]) )
window3 = T([1,2,3])([41,-2,11])(R([1,2])(PI/2)(STRUCT([   T(3)(0)(windownorth3),T([1,3])([1.8,0])(windownorth3),T(1)(0.2)(windownorth4),T([1,3])([0.2,4.4])(windownorth4),T([1,3])([0.2,8.8])(windownorth4)  ])))
 
northwindows = S([2])([1.4])(T([2])([16.5])(STRUCT([T([3])([-0.2])(window2),T(3)(8)(window2),T(3)(16)(window2),window3,T(3)(10)(window3),T(3)(20)(window3)])))

southwindow1 = COLOR([0,0,0])(GRID([  [0.5,-4.5,0.5,-4.5,0.5,-4.5,0.5,-4.5,0.5],[0.5],[0.5,-4,0.5,-4,0.5] ]))
southwindow2 = COLOR([0,0,0])(GRID([  [20],[0.5],[0.5] ]))
southwindow3 = COLOR([0,0,0])(GRID([  [0.5],[0.5],[10] ]))
southwindows = S([2,3])([0.92,0.9])(R([1,2])(PI/2)(STRUCT([southwindow1,T([3])([4.5])(southwindow2),T([3])([9.5])(southwindow2),T([1])([5])(southwindow3),southwindow3,southwindow2,T([1])([10])(southwindow3),T([1])([15])(southwindow3),T([1])([20])(southwindow3)])))

estwindow1 = COLOR([0,0,0])(GRID([  [5],[0.5],[0.5] ]))
estwindow2 = COLOR([0,0,0])(GRID([  [0.5],[0.5],[3] ]))
estwindow= S([3])([0.9])(T([1,2,3])([21.5,25,5.5])(STRUCT([estwindow1,estwindow2,T([3])([3])(estwindow1),T([1])([4.5])(estwindow2)])))
estDoppia = S([3])([1.5])(T([1,2,3])([21.5,25,10])(STRUCT([estwindow1,estwindow2,T([3])([3])(estwindow1),T([1])([4.5])(estwindow2)])))

buildings = STRUCT([floor0,floor1,pillars,floor2,floor3,floor4,estwall,estwindow,estDoppia,T([1])([-5])(estDoppia),northwall,southwall,westwall,northwindows,estwindows,T([2,3])([0.4,11])(southwindows),T([2,3])([0.4,21])(southwindows)])
VIEW(buildings)
