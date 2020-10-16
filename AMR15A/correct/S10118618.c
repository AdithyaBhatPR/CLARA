
    // ConsoleApplication2.cpp : Defines the entry point for the console application.
    //
    
    #include<stdio.h>
    
    int main()
    {
    	int n,i;
    	int arr[100];
    	int sum_even=0, sum_odd=0;
    	scanf("%d", &n);
    	for (i = 0; i < n; i++)
    	{
    		scanf("%d",&arr[i]);
    		if (arr[i] % 2 == 0)
    			sum_even += 1;
    		else
    			sum_odd += 1;
    
    	}
    	if (sum_even > sum_odd)
    		printf("READY FOR BATTLE");
    	else
    		printf("NOT READY");
    
    	return 0;
    }
    
    

