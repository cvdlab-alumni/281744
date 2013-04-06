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

windowest1 = COLOR([0,0,0])(SIMPLEX_GRID([  [0.2],[1],[3.6] ]))
windowest2 = COLOR([0,0,0])(SIMPLEX_GRID([  [9],[1],[0.2] ]))
window1 = STRUCT([T([2])([0.2])(windowest1),T([2])([0.2])(windowest2),T([2])([3.8])(windowest2),T([0,2])([4.4,0.2])(windowest1),T([0,2])([8.8,0.2])(windowest1)])
estwindows = T([0,1,2])([20.5,-1,16.5])(STRUCT([T([2])([-0.3])(window1),T([2])([6.9])(window1),T([2])([14.2])(window1)]))

windownorth1= COLOR([0,0,0])(SIMPLEX_GRID([[0.2],[1],[4.6]]))
windownorth2 = COLOR([0,0,0])(SIMPLEX_GRID([[13],[1],[0.2]]))
window2 = S([1])([0.95])(T([0,1,2])([41,-17,16.5])(R([0,1])(PI/2)(STRUCT([  T([2])([-0.8])(windownorth1),T([0,2])([6.9,-0.8])(windownorth1),T([0,2])([12.8,-0.8])(windownorth1),T([2])([-1])(windownorth2),T([2])([3.8])(windownorth2)  ]))))

windownorth3 = COLOR([0,0,0])(SIMPLEX_GRID([  [0.2],[1],[9] ]) )
windownorth4 = COLOR([0,0,0])(SIMPLEX_GRID([  [1.6],[1],[0.2] ]) )
window3 = T([0,1,2])([41,-2,11])(R([0,1])(PI/2)(STRUCT([   T([2])([0])(windownorth3),T([0,1])([1.8,0])(windownorth3),T([0])([0.2])(windownorth4),T([0,2])([0.2,4.4])(windownorth4),T([0,2])([0.2,8.8])(windownorth4)  ])))

northwindows = S([1])([1.4])(T([1])([16.5])(STRUCT([T([2])([-0.2])(window2),T([2])([8])(window2),T([2])([16])(window2),window3,T([2])([10])(window3),T([2])([20])(window3)])))


southwindow1 = COLOR([0,0,0])(SIMPLEX_GRID([  [0.5,-4.5,0.5,-4.5,0.5,-4.5,0.5,-4.5,0.5],[0.5],[0.5,-4,0.5,-4,0.5] ]))
southwindow2 = COLOR([0,0,0])(SIMPLEX_GRID([  [20],[0.5],[0.5] ]))
southwindow3 = COLOR([0,0,0])(SIMPLEX_GRID([  [0.5],[0.5],[10] ]))
southwindows = S([1,2])([0.92,0.9])(R([0,1])(PI/2)(STRUCT([southwindow1,T([2])([4.5])(southwindow2),T([2])([9.5])(southwindow2),T([0])([5])(southwindow3),southwindow3,southwindow2,T([0])([10])(southwindow3),T([0])([15])(southwindow3),T([0])([20])(southwindow3)])))


estwindow1 = COLOR([0,0,0])(SIMPLEX_GRID([  [5],[0.5],[0.5] ]))
estwindow2 = COLOR([0,0,0])(SIMPLEX_GRID([  [0.5],[0.5],[3] ]))
estwindow= S([2])([0.9])(T([0,1,2])([21.5,25,5.5])(STRUCT([estwindow1,estwindow2,T([2])([3])(estwindow1),T([0])([4.5])(estwindow2)])))
estDoppia = S([2])([1.5])(T([0,1,2])([21.5,25,10])(STRUCT([estwindow1,estwindow2,T([2])([3])(estwindow1),T([0])([4.5])(estwindow2)])))

buildings = STRUCT([estwindow,estDoppia,T([0])([-5])(estDoppia),estwall,northwall,southwall,westwall,northwindows,estwindows,T([1,2])([0.4,11])(southwindows),T([1,2])([0.4,21])(southwindows)])

DRAW(buildings)

