
    #include<stdio.h>
    int main()
    {
    	int i,k,count=0,sum=0;
    	scanf("%d",&k);
    	int arr[k];
    	for(i=0;i<k;i++)
    	{
    		scanf("%d",&arr[i]);
    	}
    	for(i=0;i<k;i++)
    	{
    		if(arr[i]%2==0)
    			count=count+1;
    		else
    			sum=sum+1;
    	}
    	if(count>sum)
    		printf("READY FOR BATTLE\n");
    	else
    		printf("NOT READY FOR BATTLE");
    	return 0;
    }

