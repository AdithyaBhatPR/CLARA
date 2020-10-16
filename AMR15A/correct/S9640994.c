
    #include <stdio.h>
    #include <string.h>
    
    inline int min(int a, int b)
    {
    	return a<b?a:b;
    }
    
    int main()
    {
    	int n, a[100], i;
    	scanf("%d", &n);
    	for (i = 0; i < n; ++i) 
    		scanf("%d", &a[i]);
    		
    	int count = 0;
    	for (i = 0; i < n; i++) {
    		if (a[i]&1)
    			count++;
    	}
    	if (count<n-count)
    		printf("READY FOR BATTLE\n");
    	else
    		printf("NOT READY\n");
    	return 0;
    }

