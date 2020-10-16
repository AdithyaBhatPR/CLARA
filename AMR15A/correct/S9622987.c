
    #include<stdio.h>
    int main()
    {
    	int i,t,a[100],ev=0,od=0;
    	scanf("%d",&t);
    	for(i=0;i<t;i++)
    	{
    		scanf("%d",&a[i]);
    	}
    	for(i=0;i<t;i++)
    	{
    		if(a[i]%2==0)
    		ev++;
    		else
    		od++;
    	}
    	if(ev>od)
    	printf("READY FOR BATTLE\n");
    	else
    	printf("NOT READY\n");
    	return 0;
    } 

