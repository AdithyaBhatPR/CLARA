
    #include<stdio.h>
    int main()
    {
    	int n,t;
    	int even=0;
    	int odd=0;
    	scanf("%d",&n);
    	while(n--)
    	{scanf("%d",&t);
    	
    		if(t%2==0)
    		even++;
    		else
    		odd++;}
    		if(even>odd)
    		printf("READY FOR BATTLE\n");
    		else
    		printf("NOT READY\n");
    		return 0;
    	
    	
    }

