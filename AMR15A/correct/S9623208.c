
    #include<stdio.h>
    int main()
    {
    int n;
    scanf("%d",&n);
    int a[n],se=0,so=0,i;
    for(i=0;i<n;i++)
    {
    scanf("%d",&a[i]);
    if(a[i]%2==0)
    se++;
    else
    so++;
    }
    if(se>so)
    printf("READY FOR BATTLE\n");
    else
    printf("NOT READY\n");
    return 0;
    }
    
    
    

