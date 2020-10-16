
    #include <stdio.h>
    int main()
    {   int n,i,n1=0,n2=0;
    int ar[100];
        scanf("%d",&n);
        for(i=0;i<n;i++)
            scanf("%d",&ar[i]);
        for(i=0;i<n;i++)
            { if(ar[i]%2==0)
            n1++;
            else
                n2++;
            }
            if(n1>n2)
                printf("READY FOR BATTLE\n");
            else printf("NOT READY\n");
        return 0;
    }
    

