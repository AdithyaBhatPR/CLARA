
    #include<stdio.h>
    #define sum 100
    
    int main()
    {
    	int i,N,count=0,discount=0;
    	
    	printf ("enter the number of soldiers");
    	scanf ("%d",&N);
    	
    	if (N<sum && N>0)
    	{
    	
    	int a[N],num;
    	
    	for (i=0;i<N;i++)
    	{
    		
    		scanf ("%d",&a[i]);
    	}
    	
    	for (i=0;i<N;i++)
    	{
    		num=0;
    		num = a[i]%2;
    		
    		if (num==0)
    		{
    			count++;
    		
    		}
    		else
    		{
    			discount++;
    		}
    	}
    	
    	
    	
    	if (count>discount)
    	{
    		printf ("READY FOR BATTLE");
    	
    	}
    	else
    	{
    		printf ("NOT READY FOR BATTLE");
    	}
    	}
    	return 0;
    }

