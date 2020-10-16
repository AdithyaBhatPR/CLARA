
    #include<stdio.h>
    int main()
    {
    	int e=0;
    	int o=0;
    	int i,n,t;
    	scanf("%d",&t);
    	
    		for(i=0;i<t;i++)
    		{
    			scanf("%d",&n);
    			if(n%2==0)
    			e++;
    			else
    			o++;
    			
    		}
    		if(e>o)
    		printf("READY FOR BATTLE");
    		else
    		printf("NOT READY FOR BATTLE");
    		return 0;
    	
    	
    	
    }
    

