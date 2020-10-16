
    #include <stdio.h>
    
    int main(void) 
    {
    	int n,i,e,o,x[100];
    	scanf("%d",&n);
    	for(i=0;i<n;i++)
    	{
    		scanf("%d",&x[i]);
    	}
    	e=0;
    	o=0;
    	for(i=0;i<n;i++)
    	{
    		if(x[i]%2==0)
    		   e++;
    		else
    		   o++;
    	}
    	if(e>o)
    	   printf("READY FOR BATTLE");
    	else
    	   printf("NOT READY");
    	
    	return 0;
    }
    

