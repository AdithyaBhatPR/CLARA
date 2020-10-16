
    #include<stdio.h>
    int main()
    {
    	int i,n,count,sum,l,k;
    	count=0;
    	sum=0;
    	scanf("%d",&n);
    	for(i=0;i<n;i++)
    	{
    		scanf("%d",&k);
    		l=k%2;
    		if(l==0)
    			count++;
    			else
    			sum++;
    	}
    	if(count>sum)
    	printf("READY FOR BATTLE");
    	else
    	printf("NOT READY");
        return 0;	
    }
    

