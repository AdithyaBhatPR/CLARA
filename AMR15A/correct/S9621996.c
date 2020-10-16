
    #include <stdio.h>
    int main()
    {int n;
    scanf("%d",&n);
    int now;
    int a[100];
    int c1=0;
    int c2=0;
    while(n--)
    {
        scanf("%d",&now);
        if(now%2==0)
            c1++;
        else{c2++;}
    }
    if(c1>c2)
        printf("READY FOR BATTLE\n");
    else {printf("NOT READY\n");}
        return 0;
    }
    

