{\rtf1\ansi\ansicpg1252\cocoartf1187\cocoasubrtf370
{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red255\green255\blue255;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720

\f0\fs22 \cf0 \cb2 for(var i = 1; i<=10;i++)\{\
	var s="";\
	for(var j=1; j<=10;j++)\{\
		if(j!==10)\
			s+= (i*j) +"," + "\\t";\
		else\
			\cb1 s+= (i*j) + "\\t";\cb2 \
	\}\
	console.log(s);\
\}}