
    #include <stdio.h>
    int main()
    {
    	int n,c,f,h=0,b=0,i,j;int a[100];
    	scanf("%d",&n);
    	for(i=0;i<n;i++)
    	scanf("%d",&a[i]);
    	f=n/2;
    	for(i=0;i<n;i++)
    	{
    		if(a[i]%2==0)
    		h++;
    	}
    	if(h>f)
    	printf("READY FOR BATTLE \n");
    	else
    	printf("NOT READY \n");
    	return 0;
    	
    }
    

