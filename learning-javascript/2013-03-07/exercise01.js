function identity(n){
s="";
	for(var i=1;i<=n;i++){
		for(var j=1;j<=n;j++){
			if(i!==j)
				s+=0;
			else
				s+=1;
			s+="\t";
		}
	s+="\n";
	}
console.log(s);
}