
    #include<stdio.h>
    
    int main()
    {
    	int i,sum_odd=0, sum_even=0, num, a[100];
    	scanf("%d",&num);
    	for(i=0;i<num;++i)
    	{
    		scanf("%d",&a[i]);
    		if (a[i]%2==0)
    			sum_even++;
    		else
    			sum_odd++;
    	}
    	if (sum_even>sum_odd)
    		printf("READY FOR BATTLE\n");
    	else
    		printf("NOT READY\n");
    	return 0;
    }
    

