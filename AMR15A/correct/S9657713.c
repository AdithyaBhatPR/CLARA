
    #include<stdio.h>
    
    int main()
    {
    	int i, ac, wc[100], o = 0, e = 0;
    	scanf("%d", &ac);
    	for(i = 0; i < ac; i++)
    	{
    		scanf("%d", &wc[i]);
    		if(wc[i] % 2 == 1)
    			o++;
    		else
    			e++;
    	}
    	if (o >= e)
    		printf("NOT READY\n");
    	else
    		printf("READY FOR BATTLE\n");
    	return 0;
    }

