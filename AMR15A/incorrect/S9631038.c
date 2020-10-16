
    #include <stdio.h>
    
    int main(void) {
    	int n,i;
    	int n1=0;
    	int n2=0;
    	scanf("%d\n",&n);
    	int a[n];
    	scanf("%d\n",a);
    	for(i=0;i<n;i++){
    	if(a[i]%2==0){
    		n1=n1+1;
    	}
    	else{
    		n2=n2+1;
    	}	
    	
    }if(n1>n2){
    	printf("READ FOR BATTLE");
    }
    	else{
    		printf("NOT READY");
    	}
    
    	return 0;
    }
    

