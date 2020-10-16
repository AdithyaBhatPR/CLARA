
    #include<stdio.h>
    
    int main()
    {
    	int n,a[100],countO=0,countE=0,i;
    	scanf("%d",&n);
    	for(i=0;i<n;i++)
    	{
    		scanf("%d",&a[i]);
    
    		if(a[i]%2==0)
    		
    			countE++;
    		
    		else
    		
    			countO++;
    		
    	}
    	if(countE>countO)
    	
    		printf("READY FOR BATTLE");
    	
    	else
    	
    		printf("NOT READY");
    		return 0;
    	
    }

