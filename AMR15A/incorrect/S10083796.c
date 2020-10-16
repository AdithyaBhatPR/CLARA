
    #include<stdio.h>
    int main()
    {
        int n,a[100],c_even=0,c_odd=0,i,j,x;
        scanf("%d",&n);
        if(n>0 && n<=100 )
        {
        for(i=0;i<n;i++)
        {
            scanf("%d",&x);
            if(x>1 && x<=100)
            {
                a[i]=x;
            if(a[i]%2==0)
                c_even++;
            else
                c_odd++;
            }
        }
        }
        if(c_even>c_odd)
            printf("READY FOR BATTLE");
        else
            printf("NOT READY");
            return 0;
    }
    

