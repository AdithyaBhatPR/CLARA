
    #include<stdio.h>
    int main()
    {
    	int i,j,k,l;
    	scanf("%d",&i);
    	while(i--)
    	{
    		scanf("%d",&j);
    		if(j%2==0)
    		k++;
    		else
    		l++;
    	}
    	if(k>l)
    	printf("READY FOR BATTLE");
    	else
    	printf("NOT READY");
    	return 0;
    }

