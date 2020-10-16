
    #include<stdio.h>
    int main() 
    {
    	int tc,a,b=0,c=0;
    	scanf("%d",&tc);
    	while(tc--) 
    	{
    		scanf("%d",&a);
    		if(a%2!=0)
    		b++;
    		else
    		c++;
    	}
    	if(c>b)
    	{printf("\nREADY FOR BATTLE");} 
    	else
    	printf("NOT READY");
    	return 0;
    }
    		
    		

