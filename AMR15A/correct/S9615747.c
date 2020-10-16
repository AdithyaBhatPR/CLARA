
    #include<stdio.h>
    int main()
    {
    int t,i,c=0;
    scanf("%d",&t);
    int a[100];
    for(i=0;i<t;i++)
    scanf("%d",&a[i]);
    for(i=0;i<t;i++)
    {
    if(a[i]%2==0)
    c++;
    else
    c--;
    }
    if(c>0)
    printf("READY FOR BATTLE");
    else
    printf("NOT READY");
    return 0;
    }
    

