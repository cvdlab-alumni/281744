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
buildings = STRUCT([estwall,northwall,westwall,southwall]);



DRAW(buildings)