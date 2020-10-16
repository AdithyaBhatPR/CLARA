
    #include<stdio.h>
    int main()
    {
    	int t,n,i,count=0,l=0;
    	scanf("%d",&t);
    	for(i=0;i<t;i++)
    	{
    		scanf("%d",&n);
    		if(n%2==0)
    		{
    			count++;
    		}
    		else
    		{
    			l++;
    		}
    	}
    	if(count>l)
    	{
    		printf("READY FOR BATTLE\n");
    	}
    	else
    	{
    		printf("NOT READY\n");
    	}
    	return 0;
    }
    

