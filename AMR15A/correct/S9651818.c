
    #include <stdio.h>
    #include <string.h>
    int main(void) {
    	int n,lucky,unlucky,i;
    	    lucky=0;
    	    unlucky=0;
    	    scanf("%d",&n);
    	    int a[n];
    	    for(i=0;i<n;i++)
    	    {
    	        scanf("%d",&a[i]);
    	        if(a[i]%2==0)
    	            lucky++;
    	        else
    	            unlucky++;
    	    }
    	    if(lucky>unlucky)
    	        printf("READY FOR BATTLE\n");
    	    else
    	        printf("NOT READY\n");
    return 0;
    }

