
    #include <stdio.h>
    
    int main(void) {
    	int n,i,j,counteven=0,countodd=0;
    
    	scanf("%d",&n);
    	for(j=1;j<=n;j++)
    	{   scanf("%d",&i);
    	   if(i%2==0)
            counteven++;
            else
            countodd++;
    	}   
    	if(countodd>counteven)
    	       printf("\nNOT READY FOR WAR");
    	       else
    	       printf("\nREADY FOR WAR");
    	return 0;
    }
    
    

