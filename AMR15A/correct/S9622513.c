
    #include <stdio.h>
    #include <string.h>
    #include <math.h>
    #include <stdlib.h>
    	int main()
    	{
    	    
    	int e,o,N,A;
    
    
    	scanf("%d", &N);
    		e=o=0;
    while(N--)
    {	scanf("%d ", &A);
    	if (A % 2 == 0)
    		e++;
    	else
    		o++;
    }
    if (e > o)
    printf("READY FOR BATTLE\n");
    else
    printf("NOT READY\n");
    return 0;
    }
    

