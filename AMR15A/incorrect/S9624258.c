
    #include <stdio.h>
    
    int main(void) {
    	// your code goes here
    int i,n,a[100],ctr=0,ctr1=0;
    scanf("%d",&n);
    for(i=0;i<n;++i)
    scanf("%d",&a[i]);
    for(i=0;i<n;++i)
    {if(a[i]%2==0)
    ++ctr;
    else
    ++ctr1;}
    if(ctr>ctr1)
    printf("READY FOR WAR");
    else printf("NOT READY FOR WAR");
    	return 0;
    }
    

