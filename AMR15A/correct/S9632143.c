
    #include<stdio.h>
    int main()
    {
    	int i,j,k,l;
    	scanf("%d\n",&i);
    	int a[100];
    	k=0;j=0;
    	for(j=0;j<i;j++)
    	{
    		scanf("%d",&a[j]);
    		if(a[j]==0||a[j]==1||a[j]%2!=0)
    		l++;
    		else 
    		k++;
    	}
    	 if(l == k)
    	printf("NOT READY");
    	else if(l<k)	
    	printf("READY FOR BATTLE");
    	else
    	printf("NOT READY");
    	return 0;
    }

