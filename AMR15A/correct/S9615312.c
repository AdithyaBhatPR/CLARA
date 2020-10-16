
    #include<stdio.h>
    #include<string.h>
    
    int main() {
    	int N,i,flag1=0,flag2=0;
    	scanf("%d",&N);
    	int arr[N];
    	for(i=0;i<N;i++)
    	scanf("%d",&arr[i]);
    	for(i=0;i<N;i++)
    	{
    	    if(arr[i]%2==0)
    	    flag1++;
    	    else
    	    flag2++;
    	}
    	if(flag1>flag2)
    	printf("READY FOR BATTLE\n");
    	else
    	printf("NOT READY\n");
    	return 0;
    }

