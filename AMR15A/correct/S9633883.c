
    #include<stdio.h>
    int main()
    {
    int i,k;
    scanf("%d",&k);
    int a[k];
    int count1=0;
    int count2=0;
    for(i=0;i<k;i++)
    {scanf("%d ",&a[i]);
    if(a[i]%2==0)
    count1++;
    else
    count2++;
    }
    if(count1>count2)
    printf("READY FOR BATTLE");
    else
    printf("NOT READY");
    return 0;
    }

