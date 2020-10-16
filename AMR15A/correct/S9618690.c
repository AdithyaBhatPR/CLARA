
    #include<stdio.h>
    #include<stdlib.h>
    int main()
    {
    	int i,n,a,b,arr[100];
    		scanf("%d",&n) ;
    		a=b=0;
    		for (i=0;i<n;i++) {
                 scanf("%d",&arr[i]) ;
    			 if (arr[i]%2==0)
    			       a++;
    		     else
    			 if (arr[i]%2 != 0)
    			       b++;		
    		}
    	    if(a>b)
    	       printf ("READY FOR BATTLE\n") ;
    	    else if(b>=a || (b==0 && a==0))
    		    printf ("NOT READY\n");
    	
    return 0;
     }
    

