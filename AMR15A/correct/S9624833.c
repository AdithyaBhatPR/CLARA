
    #include<stdio.h>
    int main()
    {
        int i,j,t,s[100],m=0,n=0;
        scanf("%d",&t);
        for(i=0;i<t;i++)
        {
            scanf("%d",&s[i]);
        }
        for(j=0;j<t;j++)
        {
            if(s[j]%2==0)
                m=m+1;
            else
                n=n+1;
        }
        if(m>n)
        printf("READY FOR BATTLE");
        else
        printf("NOT READY");
        return 0;
    }

