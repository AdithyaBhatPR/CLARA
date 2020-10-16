
    #include<stdio.h>
    int main()
    {
    	int i,j,k,l;
    	scanf("%d",&i);
    	while(i--);
    	{
    		k=0;
    		l=0;
    		scanf("%d",&j);
    		if(j%2==0)
    		k++;
    		else
    		l++;
    	}
    	if(k>l)
    	printf("READY FOR BATTLE\n");
    	else
    	printf("NOT READY");
    	return 0;
    }

