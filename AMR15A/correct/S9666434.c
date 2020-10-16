
    #include<stdio.h>
    int main (void)
    {
    	int n,a,e=0,o=0;
    	scanf("%d",&n);
    	while(n--)
    	{
    		scanf("%d",&a);
    		if(a%2 == 0)
    			e++;
    		else 
    			o++;
    	}
    	if(e > o)
    		printf("READY FOR BATTLE\n");
    	else 
    		printf("NOT READY\n");	
    		
    	return 0;
    }

