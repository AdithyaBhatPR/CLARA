
    #include <stdio.h>
    
    int main()
    {
    	
    	int i,y=0,n=0,t,a;
    	scanf("%d",&t);
    	for(i=0;i<t;i++)
    	{
    		scanf("%d",&a);
    		if(a%2==0)
    		y++;
    		else
    		n++;
    	}
    	if(y>n)
    	printf("READY FOR BATTLE");
    	else
    	printf("NOT READY");
    	
    	
    	return 0;
    }

