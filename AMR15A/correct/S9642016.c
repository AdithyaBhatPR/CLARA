
    #include <stdio.h>
    
    int main(){
    	
    	int i=0,no,even=0,odd=0,w;
    	
    	scanf("%d",&no);
    	while(i < no && scanf("%d",&w)){
    		i++;
    		if(w%2 == 0)even++;
    		else odd++;
    	}
    	
    	if(even > odd) printf("READY FOR BATTLE");
    	else printf("NOT READY");
    	
    	return 0;
    }

