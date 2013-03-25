for(var i = 1; i<=10;i++){
	var s="";
	for(var j=1; j<=10;j++){
		if(j!==10)
			s+= (i*j) +"," + "\t";
		else
			s+= (i*j) + "\t";
	}
	console.log(s);
}