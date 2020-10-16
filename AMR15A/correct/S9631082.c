
    #include<stdio.h>
    int main()
    {
    	int i,t,a[102],c1=0,c2=0;
    	scanf("%d",&t);
    	for(i=0;i<t;i++)
    	{
    		scanf("%d",&a[i]);
    	}
    	for(i=0;i<t;i++)
    	{
    		if(a[i]%2==0)
    		c1++;
    		else
    		c2++;
    	}
    	if(c1>c2)
    	printf("READY FOR BATTLE\n");
    	else
    	printf("NOT READY\n");
    	return 0;
    } 

