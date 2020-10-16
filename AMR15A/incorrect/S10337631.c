
    #include<stdio.h>
    int main()
    {
    int n,i,p=0,c=0;
    scanf("%d",&n);
    int a[n];
    for(i=0;i<n;i++)
    {
    scanf("%d",&a[i]);
    if(a[i]%2==0)
    p++;
    if(p>n/2)
    {
    c=1;
    break;
    }
    }
    if(c==1)
    printf("READY FOR BATTLE");
    else
    printf("NOT READY FOR BATTLE");
    c=0;
    return 0;
    }
    

