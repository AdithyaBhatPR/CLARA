
    #include<stdio.h>
    int main()
    {
        int i,n,even=0,odd=0,k;
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%d",&k);
            if(k%2)
                odd++;
            else
                even++;
        }
        if(even>odd)
            printf("READY FOR BATTLE");
        else
            printf("NOT READY");
        return 0;
    
    }
    

