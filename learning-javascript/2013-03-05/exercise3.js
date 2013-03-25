for(var i = 1; i<=10;i++){
	var s="";
	for(var j=1; j<=10;j++){
		if(j!==10){
			if(i!==j)
				s+= 0 +"," + "\t";
			else
				s+= 1 +"," + "\t";
		}
		else{
			if(i!==j)
				s+= 0 + "\t";
			else
				s+= 1 + "\t";		}
	}
	console.log(s);
}
