var circle = CIRCLE(0.5)(36);
var pillar = EXTRUDE([10])(circle)

pillars0round = STRUCT(REPLICA([5])([pillar,T([0])([10])]))
pillars0square = SIMPLEX_GRID([[-4.5,1,-3.5,1,-9,1,-9,1],[1],[10]  ])
pillars2square = SIMPLEX_GRID([[1,-9,1,-29,1],[1],[10]  ])
pillars22square = SIMPLEX_GRID([[1,-8.5,1,-9,1,-9,1,-9.5,1],[1],[10]  ])


pillars1square =  T([0,1,2])([-0.5,-0.5,10])(SIMPLEX_GRID([[1,-9,1,-9,1,-9,1,-9,1],[1],[10]]))
pillars12square = T([0,1,2])([-1,19.5,10])(SIMPLEX_GRID([[-0.5,1,-8.5,1,-9,1,-9,-10.5,1],[1],[10]]))
pillarSmall = CUBOID([0.5,0.5,10])
pillars3square = SIMPLEX_GRID([[-20,1,-19,1],[1],[10]  ])
pillars33square = SIMPLEX_GRID([[-20,1,-9,1,-9.5,1],[1],[10]  ])

pillars0 = STRUCT([pillars0round,T([1])([20])(pillar),T([1])([19.5])(pillars0square)])
pillars3 = T([0,1,2])([-0.5,-0.5,30])(STRUCT([pillars3square,T([0,1])([-0.5,20])(pillars33square),T([0,1])([9.5,20.5])(pillarSmall),T([1])([20.5])(pillarSmall),T([0,1])([40,24])(S([0,1])([2,2])(pillarSmall))]))
pillars1 = STRUCT([pillars1square,pillars12square,T([0,1,2])([2,19.5,10])(pillarSmall),T([0,1,2])([29.5,20,10])(pillar)])
pillars2 = T([0,1,2])([-0.5,-0.5,20])(STRUCT([pillars2square,T([1])([20])(pillars22square)]))
pillars = STRUCT([pillars0, pillars1,pillars2,pillars3])

floor10 = T([0])([-0.5])(SIMPLEX_GRID([ [41],[20],[1]  ]))
floor11 = SIMPLEX_GRID([ [3],[-20,5],[1]])
floor12 = SIMPLEX_GRID([ [-17,23],[-20,5],[1]])



floor30 = SIMPLEX_GRID([   [20],[25],[1]])
floor31 = SIMPLEX_GRID([   [-19,14],[20],[1]])
floor32 = SIMPLEX_GRID([ [-33,8],[25],[1]])

balcony = T([0])([-4])(SIMPLEX_GRID([ [4],[-20,5],[1]]))


floor41= T([0,1,2])([-0.5,-0.5,40])(SIMPLEX_GRID([ [-19.5,21.5],[25.5],[1]]))
floor42 = T([0,1,2])([-0.5,-0.5,40])(SIMPLEX_GRID([ [19.5],[-20,5.5],[1]]))


function annulus_sector (alpha, r, R) {
  var domain = DOMAIN([[0,alpha],[r,R]])([36,1]);
  var mapping = function (v) {
    var a = v[0];
    var r = v[1];
    
    return [r*COS(a), r*SIN(a)];
  }
  var model = MAP(mapping)(domain);
  return model;
}


floor01 = R([0,1])(-PI/2)(annulus_sector(PI, 1, 3));
floor02 = R([0,1])(PI)(annulus_sector(PI, 1, 3));

floor03 = EXTRUDE([1])(POLYLINE([ [29.5,25],[-0.5,25],[-0.5,19.5],[5,19.5],[5,8],[29.5,8],[29.5,25]]))
floor03 = SIMPLEX_GRID([[31],[-24,1]])
floor04 = SIMPLEX_GRID([ [1],[-19.5,5] ])
floor05 = SIMPLEX_GRID([ [5],[-19.5,1] ])
floor07 = SIMPLEX_GRID([[-4,1],[-8,12] ])
floor06 = T([1])([8])(SIMPLEX_GRID([ [-7,24],[1] ]))
floor08 = SIMPLEX_GRID([[-30,1],[-9,5]])


floor04 =T([1])([-0.5])(STRUCT([   floor08,floor07,floor06,floor04,floor05,floor03,T([0,1])([29.5,19.5])(floor01)  , T([0,1])([6,8])(floor02)]))
floor0= EXTRUDE([10])(floor04)
floor1 = T([0,1,2])([-0.5,-0.5,10])(STRUCT([floor30,floor31,floor32,balcony]))
floor2 = T([1,2])([-0.5,20])(STRUCT([floor10,floor11,floor12]))
floor3 = T([0,1,2])([-0.5,-0.5,30])(STRUCT([floor30,floor31,floor32]))
floor4 = STRUCT([floor41,floor42])


est0 = SIMPLEX_GRID([ [20],[1],[20,-10,1]]);
est1 = SIMPLEX_GRID([[-20,1],[1],[31]])
est2 = SIMPLEX_GRID([ [-21,9],[1],[6.5,-4,3,-4,3,-4,6.5]])
est3 =SIMPLEX_GRID([ [-30,11],[1],[31]])
est4 = SIMPLEX_GRID([[1],[1],[31]])
est5 = SIMPLEX_GRID([[20,-20],[1],[23]])

north0 = SIMPLEX_GRID([ [1],[10],[31]])
north1 = T([0])([18])(north0);
north2 = SIMPLEX_GRID([[14],[1],[5.5,-5,3,-5,3,-5,4.5]])
north3 = SIMPLEX_GRID([[-14,2],[1],[31] ] )
north4 = SIMPLEX_GRID([[-16,2],[1],[1,-9,1,-9,1,-9,1]])
north5 = S([1])([1])(SIMPLEX_GRID([[1],[1],[10]]))

west0 = T([0,1,2])([40,24-0.5,10])(R([0,1])(PI/2)(SIMPLEX_GRID([ [1],[10],[31]])))
west1 = SIMPLEX_GRID([[3,-10,17],[1],[40]])
west2 = SIMPLEX_GRID([[20],[1],[5]])
west3 = SIMPLEX_GRID([[20],[1],[5,-3,7,-5,5,-5,10]])
west4 = T([0,2])([8,5])(SIMPLEX_GRID([[10],[1],[3]]))
west5 = T([0,2])([7.5,15])(SIMPLEX_GRID([[1],[1],[9]]))
west6 = T([0,2])([3.5,25])(SIMPLEX_GRID([[1,-0.5,10],[1],[9]]))
west7 = T([0,2])([-10.5,10])(S([0])([1.3])(SIMPLEX_GRID([[10.5],[1],[30]])))

south0 = T([2])([10])(SIMPLEX_GRID([[25],[1],[3,-7,1]]))
south1 = SIMPLEX_GRID([[5],[1],[10]])

northwall = S([1])([1.33])(T([0,1,2])([41,-0.5,10])(R([0,1])(PI/2)(STRUCT([north0,north2,north3,north4,T([0,2])([18,-10])(north5),T([1])([18])(north5),T([0,2])([18,10])(north5),T([0,2])([18,20])(S([2])([1.1])(north5))]))))
estwall = T([0,1,2])([-0.5,-0.5,10])(STRUCT([est0,est1,est2,est3,est4,est5]))
westwall= T([0,1])([29.5,25])(R([0,1])(PI)(STRUCT([west1,west2,west3,west4,west5,west6,west7])))
southwall = T([0,1,2])([-0.5,24.5,20])(R([0,1])(-PI/2)(STRUCT([south0,south1])))
buildings = STRUCT([floor0,floor1,pillars,floor2,floor3,floor4,estwall,northwall,westwall,southwall]);



DRAW(buildings)