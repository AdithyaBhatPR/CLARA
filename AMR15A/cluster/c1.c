
    #include<stdio.h>
    main(){
    	int n,a[105],e=0,o=0,i;
    	scanf("%d",&n);
    	for(i=0;i<n;i++){
    		scanf("%d",&a[i]);
    	if(a[i]%2==0){
    		a[i]=2;
    	}else{
    		a[i]=1;
    	}
    	}
    	for(i=0;i<n;i++){
    		if(a[i]==2){
    			e++;
    		}else if(a[i]==1){
    			o++;
    		}
    	}
    	if(e>o){
    		printf("READY FOR BATTLE");
    	}else{
    		printf("NOT READY");
    	}
    	return 0;
    	}

