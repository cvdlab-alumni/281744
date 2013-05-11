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
	
domain = GRID([6,6])

## esercizio 2
#vista dietro

puntial1 = [[0,0,0],[0,1,0]]
mappingpal1 = MAP(BEZIER(S1)(puntial1))(domain)
puntigiunto1 = [[0,0.5,-1.6],[0,-0.3,-1.6]]
puntigiunto2 = [[0,0.5,-1.7],[0,-0.3,-1.7]]
puntigiunto3 = [[0,0.4,0],[0,0,-0.5],[0,-0.5,-0.5]]
puntigiunto4 = [[0,0.6,0],[0,1,-0.5],[0,1.5,-0.5]]
puntigiunto5 = [[0,0.5,-0.5],[0,0.3,-0.12]]

mappingpg1 = MAP(BEZIER(S1)(puntigiunto1))(domain)
mappingpg2 = MAP(BEZIER(S1)(puntigiunto2))(domain)
mappingpg3 = MAP(BEZIER(S1)(puntigiunto3))(domain)
mappingpg4 = MAP(BEZIER(S1)(puntigiunto4))(domain)
mappingpg5 = MAP(BEZIER(S1)(puntigiunto5))(domain)
giunti = STRUCT([mappingpg1,mappingpg2])
giuntiSup = STRUCT([mappingpg3,mappingpg4,mappingpg5,T(2)(1)(R([1,2])(-PI)(mappingpg5))])

vista_dietro = STRUCT([giuntiSup,T(2)(0.9)(giunti),giunti,R([2,3])(-PI/2)(S(2)(2)(mappingpal1)),T(2)(1)(R([2,3])(-PI/2)(S(2)(2)(mappingpal1))),mappingpal1,T(3)(-0.5)(mappingpal1),T(3)(-2)(mappingpal1),T([2,3])([-0.2,-2.3])(S(2)(1.4)(mappingpal1)),T(3)(-0.8)(mappingpal1)])
##VIEW(vista_dietro)
##vista alto

p1 = [[0,0,2],[2,-0.5,2],[4,-2,2],[5,0,2]]
p2 = [[5,0,2],[10,0,2],[10,1,2],[5,1,2]]
p3 = [[0,1,2],[2,1.5,2],[4,3,2],[5,1,2]]
p4 = [[1,-0.3,0],[1,-1,0]]
p5 = [[5,-1,0],[1,-1,0]]
p6 = [[1,1.3,0],[1,2,0]]
p7 = [[5,2,0],[1,2,0]]
mappingp1 = MAP(BEZIER(S1)(p1))(domain)
mappingp2 = MAP(BEZIER(S1)(p2))(domain)
mappingp3 = MAP(BEZIER(S1)(p3))(domain)
mappingp4 = MAP(BEZIER(S1)(p4))(domain)
mappingp5 = MAP(BEZIER(S1)(p5))(domain)
mappingp6 = MAP(BEZIER(S1)(p6))(domain)
mappingp7 = MAP(BEZIER(S1)(p7))(domain)
parte_inf = STRUCT([mappingp1,mappingp3,mappingp2,mappingp4,mappingp5,mappingp6,mappingp7])


##parte sup
ps1 = [[0,0,3],[2,-0.5,3],[4,-2,3],[5,0,3]]
ps2 = [[5,0,3],[10,0,3],[10,1,3],[5,1,3]]
ps3 = [[0,1,3],[2,1.5,3],[4,3,3],[5,1,3]]
ps4 = [[0,0,3],[-0.5,0.25,3]]
ps5 = [[0,1,3],[-0.5,0.75,3]]
ps6 = [[-0.5,0.25,3],[-1,0.4,3]]
ps7 = [[-0.5,0.75,3],[-1,0.6,3]]

p1alettone = [[-1,0,3],[-1,1,3]]

mappingps1 = MAP(BEZIER(S1)(ps1))(domain)
mappingps2 = MAP(BEZIER(S1)(ps2))(domain)
mappingps3 = MAP(BEZIER(S1)(ps3))(domain)
mappingps4 = MAP(BEZIER(S1)(ps4))(domain)
mappingps5 = MAP(BEZIER(S1)(ps5))(domain)
mappingps6 = MAP(BEZIER(S1)(ps6))(domain)
mappingps7 = MAP(BEZIER(S1)(ps7))(domain)
mappingp1alettone = MAP(BEZIER(S1)(p1alettone))(domain)

alettone_post = T([2,3])([-0.25,-1])(S(2)(1.5)(STRUCT([mappingps4,mappingps5,mappingps6,mappingps7,mappingp1alettone,T(1)(-0.5)(mappingp1alettone),T([1])([-0.75])(mappingp1alettone),T([1,2])([-0.7,1])(R([1,2])(PI/2)(S(2)(1.5)(mappingp1alettone))),T(1)(-2.2)(R([1,2])(-PI/2)(S(2)(1.5)(mappingp1alettone)))])))



##alettone anteriore
pa1 = [[0,0,0],[0.7,0,0]]
pa2 = [[0.7,0,0],[0.7,1.1,0]]
pa3 = [[0,0,0],[0,0.5,0]]
pa4 = [[0,0.5,0],[0.4,0.7,0]]
pa5 = [[0.4,0.7,0],[0.4,1,0]]

mappingpa1 = MAP(BEZIER(S1)(pa1))(domain)
mappingpa2 = MAP(BEZIER(S1)(pa2))(domain)
mappingpa3 = MAP(BEZIER(S1)(pa3))(domain)
mappingpa4 = MAP(BEZIER(S1)(pa4))(domain)
mappingpa5 = MAP(BEZIER(S1)(pa5))(domain)
semiala = STRUCT([mappingpa1,mappingpa2,mappingpa3,mappingpa4,mappingpa5])
ala_anteriore = STRUCT([semiala,T([2])([2.5])(R([2,3])(PI)(semiala))])

##pilota

pp1 = [[1,0,0],[0,-0.5,0],[0,1.5,0],[1,1,0]]
pp2 = [[1,0,0],[0.8,0.5,0],[1,1,0]]
pp3 = [[1,-0.2,0],[1,1.2,0]]
pp4 = [[1,-0.2,0],[2,-0.5,0],[2,1.5,0],[1,1.2,0]]
mappingpp1 = MAP(BEZIER(S1)(pp1))(domain)
mappingpp2 = MAP(BEZIER(S1)(pp2))(domain)
mappingpp3 = MAP(BEZIER(S1)(pp3))(domain)
mappingpp4 = MAP(BEZIER(S1)(pp4))(domain)
posto_pilota = T([1,2,3])([0.5,0.4,1.5])(S([1,2])([2,0.4])(STRUCT([mappingpp1,mappingpp2,mappingpp3,mappingpp4])))
#VIEW(parte_sup)

vista_alto = STRUCT([parte_inf,alettone_post,posto_pilota,T([1,2])([8,-0.75])(ala_anteriore)])
##VIEW(vista_alto)

#vista laterale
#alettoneposteriore
pal1 = [[0,0,0.3],[-1,0,0.5],[-1,0,0.5],[-1,0,2.5]]
pal2 = [[-1,0,2.5],[-0.75,0,2.5],[-0.5,0,2.2]]
pal3 = [[-0.5,0,2.2],[-0.5,0,2.5]]
pal4 = [[-0.5,0,2.5],[0.5,0,2.5],[0.5,0,2.5],[0.5,0,2]]
pal5 = [[0.5,0,2],[-0.5,0,1],[0.7,0,1]]
pal6 = [[0,0,0.3],[0.3,0,0.3],[0.7,0,1]]
mappingpal1 = MAP(BEZIER(S1)(pal1))(domain)
mappingpal2 = MAP(BEZIER(S1)(pal2))(domain)
mappingpal3 = MAP(BEZIER(S1)(pal3))(domain)
mappingpal4 = MAP(BEZIER(S1)(pal4))(domain)
mappingpal5 = MAP(BEZIER(S1)(pal5))(domain)
mappingpal6 = MAP(BEZIER(S1)(pal6))(domain)
alettone_p = STRUCT([mappingpal1,mappingpal2,mappingpal3,mappingpal4,mappingpal5,mappingpal6])
##alettone ant
pal6 = [[15,0,0.3],[15.2,0,0]]
pal7 = [[14,0,0.3],[14.3,0,0.15],[14.7,0,0]]
pal8 = [[13.5,0,0],[15.5,0,0]]
pal9 = [[13.5,0,-1],[15.5,0,-1]]
pal10 = [[13.5,0,0],[13.5,0,-1]]
pal11 = [[15.5,0,0],[15.5,0,-1]]
mappingpal6 = MAP(BEZIER(S1)(pal6))(domain)
mappingpal7 = MAP(BEZIER(S1)(pal7))(domain)
mappingpal8 = MAP(BEZIER(S1)(pal8))(domain)
mappingpal9 = MAP(BEZIER(S1)(pal9))(domain)
mappingpal10 = MAP(BEZIER(S1)(pal10))(domain)
mappingpal11 = MAP(BEZIER(S1)(pal11))(domain)
alettone_ant = STRUCT([mappingpal6,mappingpal7,mappingpal8,mappingpal9,mappingpal10,mappingpal11])
#linea alta
pl1 = [[0.7,0,1],[4,0,2],[6,0,2.5],[8,0,2]]
pl2 = [[8,0,2],[7.5,0,1.7],[7,0,1.5],[8.5,0,0.9]]
pl3 = [[0.5,0,0.4],[4,0,0.8],[8.5,0,1],[10,0,0.8]]
pl4 = [[0.5,0,0.2],[7.5,0,-1],[8.5,0,-0.5],[10,0,0.2]]
pl5 = [[10,0,0.8],[10,0,0.2]]
pl6 = [[10,0,0.8],[12,0,0.9],[14,0,0.9],[16,0,0.3]]
pl7 = [[10,0,0.2],[13,0,0.3],[16,0,0.3]]
pl9 = [[0.5,0,0.4],[0,0,1.2],[0,0,0.3]]
mappingpl1 = MAP(BEZIER(S1)(pl1))(domain)
mappingpl2 = MAP(BEZIER(S1)(pl2))(domain)
mappingpl3 = MAP(BEZIER(S1)(pl3))(domain)
mappingpl4 = MAP(BEZIER(S1)(pl4))(domain)
mappingpl5 = MAP(BEZIER(S1)(pl5))(domain)
mappingpl6 = MAP(BEZIER(S1)(pl6))(domain)
mappingpl7 = MAP(BEZIER(S1)(pl7))(domain)
mappingpl9 = MAP(BEZIER(S1)(pl9))(domain)
#linea sotto
pl8 = [[0.3,0,-1],[10,0,-1]]
mappingpl8 = MAP(BEZIER(S1)(pl8))(domain)
vista_lat = STRUCT([mappingpl9,mappingpl8,T(1)(7.7)(S(1)(0.5)(alettone_ant)),alettone_p,mappingpl1,mappingpl2,mappingpl3,mappingpl4,mappingpl5,mappingpl6,mappingpl7])
vista_tot = STRUCT([T([1,3])([2.5,-1])(S(1)(1.5)(vista_alto)),T(2)(-1)(vista_lat),T(2)(2)(vista_lat),T([1,2,3])([-1,-0.3,2.5])(S([2,3])([1.5,1.5])(vista_dietro))])
#VIEW(vista_tot)


##esercizio3
dom = PROD([INTERVALS(2*PI)(32),INTERVALS(2*PI)(32)])

def anulusSector(R,r):
    def circle0(p):
        u,v = p;
        return (r*COS(u)+R)*COS(v),(r*COS(u)+R)*SIN(v);
    return MAP(circle0)(dom)

def toro3d(R, r):
          def toro0(v):
              a = v[0]
              b = v[1]
  
              u = (r * COS(a) + R) * COS(b)
              v = (r * COS(a) + R) * SIN(b)
              w = (r * SIN(a))
              return [u,v,w]
          return toro0

perno1=anulusSector(1, 1.3)
perno=PROD([perno1, Q(1)])

baseRaggio=R([1,3])(PI/2)(CYLINDER([0.1,3])(36))
raggio=T([1,3])([-1.2,0.5])(S(2)(0.5)(baseRaggio))

raggi=STRUCT([raggio,R([1,2])(1*PI/6)(raggio),R([1,2])(1.1*PI/6)(raggio),R([1,2])(2*PI/6)(raggio),R([1,2])(2.1*PI/6)(raggio),R([1,2])(3*PI/6)(raggio),R([1,2])(3.1*PI/6)(raggio),R([1,2])(4*PI/6)(raggio),R([1,2])(4.1*PI/6)(raggio),R([1,2])(5*PI/6)(raggio),R([1,2])(5.1*PI/6)(raggio),R([1,2])(6*PI/6)(raggio),R([1,2])(6.1*PI/6)(raggio),R([1,2])(7*PI/6)(raggio),R([1,2])(7.1*PI/6)(raggio),R([1,2])(8*PI/6)(raggio),R([1,2])(8.1*PI/6)(raggio),R([1,2])(9*PI/6)(raggio),R([1,2])(9.1*PI/6)(raggio),R([1,2])(10*PI/6)(raggio),R([1,2])(10.1*PI/6)(raggio),R([1,2])(11*PI/6)(raggio),R([1,2])(11.1*PI/6)(raggio),R([1,2])(12*PI/6)(raggio),R([1,2])(12.1*PI/6)(raggio)])

copertone=COLOR(BLACK)(T(3)(0.5)(MAP(toro3d(6.5,2.2))(dom)))

pneumatico = S([1,2,3])([0.1,0.1,0.1])(STRUCT([perno,raggi,copertone]))
es3=STRUCT([T([2,3])([-1,-0.3])(R([2,3])(PI/2)(S(3)(2)(pneumatico))),T([2,3])([2,-0.3])(R([2,3])(-PI/2)(S(3)(2)(pneumatico))),T([1,2,3])([13,-1,-0.3])(R([2,3])(PI/2)(S(3)(2)(pneumatico))),T([1,2,3])([13,2,-0.3])(R([2,3])(-PI/2)(S(3)(2)(pneumatico))),vista_tot])
#VIEW(es3)
#VIEW(pneumatico)

## esercizio4
p1 = [[0,0,0],[1,0,0.5],[2,0,0.5],[3,0,0]]
p2 = [[0,1,0],[1,1,0.5],[2,1,0.5],[3,1,0]]
p3 = [[0.5,0,0],[1,0,0.25],[2,0,0.25],[2.5,0,0]]
p4 = [[0.5,1,0],[1,1,0.25],[2,1,0.25],[2.5,1,0]]

p5 = [[0,0,0],[0,-0.25,-1.5],[0,0,-3]]
p6 = [[3,0,0],[3,-0.25,-1.5],[3,0,-3]]
p7 = [[0.5,0,-3],[1,0,-3.25],[2,0,-3.25],[2.5,0,-3]]

p8 = [[0,1,0],[0,1.25,-1.5],[0,1,-3]]
p9 = [[3,1,0],[3,1.25,-1.5],[3,1,-3]]

c1 = MAP(BEZIER(S2)([BEZIER(S1)(p1),BEZIER(S1)(p2)]))(domain)
c2 = MAP(BEZIER(S2)([BEZIER(S1)(p3),BEZIER(S1)(p4)]))(domain)
c3 = MAP(BEZIER(S2)([BEZIER(S1)(p3),BEZIER(S1)(p1)]))(domain)
c4 = MAP(BEZIER(S2)([BEZIER(S1)(p2),BEZIER(S1)(p4)]))(domain)
c6 = MAP(BEZIER(S2)([BEZIER(S1)(p5),BEZIER(S1)(p6)]))(domain)
c7 = MAP(BEZIER(S2)([BEZIER(S1)(p8),BEZIER(S1)(p9)]))(domain)
c8 = MAP(BEZIER(S2)([BEZIER(S1)(p8),BEZIER(S1)(p5)]))(domain)
c9 = MAP(BEZIER(S2)([BEZIER(S1)(p6),BEZIER(S1)(p9)]))(domain)

c5 =STRUCT([c1,c2,c3,c4])
baseVolante = STRUCT([c9,c8,c7,c6,T(3)(-3)(S(3)(0.7)(c5)),S([3])([0.05])(c5),T(3)(-3)(R([1,3])(PI/2)(S(3)(2)(c5))),T(1)(3)(R([1,3])(-PI/2)(S(3)(2)(c5)))])
pulsante = R([2,3])(PI/2)(CYLINDER([0.1,0.1])(36))

pv1 = [[0,0,0.1],[0.3,0,0.1],[0.5,0,0.2]]
pv2 = [[0,0,-0.1],[0.3,0,-0.1],[0.5,0,-0.2]]
pv3 = [[0,1,0.1],[0.3,1,0.1],[0.5,1,0.2]]
pv4 = [[0,1,-0.1],[0.3,1,-0.1],[0.5,1,-0.2]]

cv1 = S(3)(2)(MAP(BEZIER(S2)([BEZIER(S1)(pv2),BEZIER(S1)(pv1)]))(domain))
cv2 = S(3)(2)(MAP(BEZIER(S2)([BEZIER(S1)(pv3),BEZIER(S1)(pv4)]))(domain))
cv3 = S(3)(2)(MAP(BEZIER(S2)([BEZIER(S1)(pv4),BEZIER(S1)(pv2)]))(domain))
cv4 = S(3)(2)(MAP(BEZIER(S2)([BEZIER(S1)(pv1),BEZIER(S1)(pv3)]))(domain))

orizz = STRUCT([T([1,3])([3,-1.4])(cv4),T([1,3])([3,-1.4])(cv1),T([1,3])([3,-1.4])(cv2),T([1,3])([3,-1.4])(cv3)])
volante = COLOR(BLACK)(STRUCT([T([1,3])([3,-3])(R([1,3])(PI)(orizz)),orizz,T([1,2,3])([2.7,-0.05,-1])(COLOR(RED)(pulsante)),T([1,2,3])([2.8,0,-0.5])(COLOR(RED)(pulsante)),T([1,3])([0.2,-0.5])(COLOR(RED)(pulsante)),T([1,2,3])([0.3,-0.05,-1])(COLOR(RED)(pulsante)),T([1,2,3])([0.3,-0.05,-1.5])(COLOR(RED)(pulsante)),T([1,2,3])([2.7,-0.05,-1.5])(COLOR(RED)(pulsante)),T([1,2,3])([2.7,-0.05,-2])(COLOR(RED)(pulsante)),T([1,2,3])([0.3,-0.05,-2])(COLOR(RED)(pulsante)),T([1,3])([1.5,-1.5])(COLOR(YELLOW)(S([1,2,3])([2,2,2])(pulsante))),T([1,2,3])([1.5,2,-1.5])(S([1,2,3])([2,10,2])(pulsante)),baseVolante]))
es4 = STRUCT([es3,T([1,2])([7,0.9])(R([1,2])(-PI/2)(S([1,2,3])([0.2,0.2,0.2])(volante)))])
#VIEW(volante)
VIEW(es4)
