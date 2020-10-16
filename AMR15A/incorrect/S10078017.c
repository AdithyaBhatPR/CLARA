
    void main()
    	{
    		int n,t,i,k,j;
    		scanf("%d",&t);
    		while(t!=0)
    		{
    			k=0;
    			j=0;
    			scanf("%d",&n);
    			int a[n];
    			for(i=0;i<n;i++)
    				scanf("%d",&a[i]);
    			for(i=0;i<n;i++)
    			{
    				if(a[i]%2==0)
    					k++;
    				else
    					j++;
    			}
    			if(k>j)
    				printf("READY FOR BATTLE");
    			else
    				printf("NOT READY");
    			t--;
    		}
    	}
    

