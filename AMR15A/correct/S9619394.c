
    #include <stdio.h>
    
    int main(void) {
    	int i,l,k,c=0;
    	scanf("%d",&i);
    	l=i;
    	while(i--)
    	{
    		scanf("%d",&k );
    		if(k%2==0)
    			c++;
    	}
    	
    	if(c>(l-c))
    		printf("READY FOR BATTLE");
    	else
    		printf("NOT READY");
    	return 0;
    }
    

