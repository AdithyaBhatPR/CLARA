
    #include <stdio.h>
    
    int main(void) {
    	// your code goes here
    	int t;
    	int a[2];
    	a[0]=0;
    	a[1]=0;
    	scanf("%d",&t);
    	int c;
    	while(t--){
    		scanf("%d",&c);
    		a[c%2]=a[c%2]+1;
    	}
    	
    	if(a[0]>a[1]){
    		printf("READY FOR BATTLE");
    	} else {
    		printf("NOT READY");
    	}
    	
    	return 0;
    }
    

