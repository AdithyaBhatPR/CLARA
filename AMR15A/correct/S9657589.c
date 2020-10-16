
    #include<stdio.h>
    int main()
    {
    int n,ce=0,co=0,i;
    scanf("%d",&n);
    int a[n];
    for(i=0;i<n;i++)
    {
    scanf("%d",&a[i]);
    if(a[i]%2==0)
    ce+=1;
    else
    co+=1;
    }
    if(ce>co)
    printf("READY FOR BATTLE\n");
    else
    printf("NOT READY\n");
    return 0;
    }

