
    #include<stdio.h>
    #include<stdlib.h>
    #include<string.h>
    #include<math.h>
    #define sf scanf
    #define pf printf
    #define hell 1000000007
    int main()
    {
        int t,n,i,j=0,k=0,p,sum1=0,sum2=0;
        sf("%d",&n);
        int a[n];
        for(i=0;i<n;i++)
        {
            sf("%d",&a[i]);
            if(a[i]%2==0)
                j++;
            else
                k++;
        }
        if(j>k)
            pf("READY FOR BATTLE");
        else
            pf("NOT READY");
        
        return 0;
    }
    

