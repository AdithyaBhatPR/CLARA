
    #include<stdio.h>
    int main()
    {  int n,arr[100],i,counte=0,counto=0;
       scanf("%d",&n);
       for(i=0;i<n;i++)
       scanf("%d",&arr[i]);
       for(i=0;i<n;i++)
       {
       	if(arr[i]%2==0) counte++;
       	else counto++;
       }
       if(counte>counto) printf("READY FOR BATTLE\n");
       else printf("NOT READY\n");
    	return 0;
    }

