
        #include<stdio.h>
        int main (void)
        {
        	int n;
        	scanf("%d",&n);
        	int a[n],i,odd=0,even=0;
        	while(n--)
        		scanf("%d",&a[i]);
        	for(i=0;i<n;i++)
        	{
        		if(a[i] % 2 == 0)
        			even++;
        		else
        			odd++; 
        	}
        	if(odd >= even)
        		printf("NOT READY\n");
        	else
        		printf("READY FOR BATTLE\n");
        } 

