
    #include <stdio.h>
    
    int main(void) {
    	int n,i,a,counte=0,counto=0;
    	scanf("%d",&n);
    	while(n--)
    	{
    		scanf("%d",&a);
    		if(a%2==0)
    			counte++;
    		else
    			counto++;
    	}
    	if(counte>counto)
    		printf("READY FOR BATTLE\n");
    	else
    		printf("NOT READY\n");
    	return 0;
    }
    

