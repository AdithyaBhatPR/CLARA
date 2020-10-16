
    #include<stdio.h>
    #include<math.h>
    #include<stdlib.h>
    int main()
    {
    int n=0,i=0,j=0;
    scanf("%d",&n);
    int a[n];
    int ne=0,no=0;
    for(i=0;i<n;i++)
    {
    scanf("%d",&a[i]);
    }
    for(j=0;j<n;j++)
    {
    if(a[j]%2==0)
    ne++;
    else
    no++;
    }
    if(no>ne)
    printf("NOT READY\n");
    else
    printf("READY FOR BATTLE\n");
    return 0;
    }

