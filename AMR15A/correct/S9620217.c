
    #include<stdio.h>
    int main()
    {
    	int a,i,count=0,odd;
    	scanf("%d",&a);
    	int arr[a];
    	for(i=0 ; i<a; i++)
    	{
    		scanf("%d",&arr[i]);
    	}
    	for(i=0 ; i<a ; i++)
    	{
    		if(arr[i]%2==0)
    		count++;
    	}
    	odd=a-count;
    	if(count>odd)
    	printf("READY FOR BATTLE");
    	else
    	printf("NOT READY");
    	return 0;
    }
    

