
    #include <stdio.h>
    
    int main()
    {
    	int n;
    	scanf ("%d", &n);
    	int i, j, k;
    	int arr[n];
    	for (i=0; i<n; i++)
    	{
    		scanf ("%d", &arr[i]);
    	}
    	for (i=0; i<n; i++)
    	{
    		if (arr[i]%2 == 0)
    			j++;
    		else
    			j--;
    	}
    	if (j>0)
    	{
    		printf ("READY FOR BATTLE\n");
    	}
    	else 
    		printf ("NOT READY\n");
    	return 0;
    }

