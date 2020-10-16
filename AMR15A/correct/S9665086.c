
    #include<stdio.h>
    
    int main()
    {
        int n,hld,i;
        scanf("%d",&n);
        int even=0,odd=0;
        for(i=0;i<n;i++)
        {
            scanf("%d",&hld);
            (hld&1==1)?odd++:even++;
        }
        (even>odd)?printf("READY FOR BATTLE"):printf("NOT READY");
        return 0;
    }

