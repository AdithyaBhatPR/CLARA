
    #include<stdio.h>
    
    int main() {
    	int n,i,j,count=0;
    	int arr[100];
    	scanf("%d",&n);
    	for(i=0;i<n;i++) {
    		scanf("%d",&arr[i]);
    	}
    	for(j=0;j<n;j++) {
    		if(arr[j]%2==0)
    			count++;
    	}
    	int rest=n-count;
    	if(count==0 || rest>count || rest==count)
    		printf("NOT READY\n");
    	else printf("READY FOR BATTLE\n");
    return 0;
    }
    

