
    #include<stdio.h>
    int main()
    {
    	int even=0,i,n,j=0;
    	scanf("%d",&n);
    	int a[n];
    	for(i=0;i<n;i++)
    	{
    		scanf("%d ",&a[i]);
    			
    	}
    	for(i=0;i<n;i++)
    	{
    	if(a[i]%2==0)
    	even++;
    	else
    	j++;	
    	}
    	if(even>j)
    	printf("READY FOR BATTLE\n");
    	else
    	printf("NOT READY\n");
    	return 0;
    }

