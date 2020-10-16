
    #include <stdio.h>
    #include <stdlib.h>
    int main(){
    	int t;
    	scanf("%d",&t);
    	int a[100];
    	int x=0,y=0,i;
    	while(t--){
    		int n;
    		scanf("%d",&n);
    		for(i=0;i<n;i++)
    		{
    		scanf("%d",a[i]);
    		if(a[i]%2==0)
    		x++;
    		else y++;
    	}
    	if(x>y)
    	printf("\nREADY FOR BATTLE");
    	else printf("\nNOT READY");
    
    	}
    }
    

