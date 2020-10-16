
    #include<stdio.h>
    int main()
    {
        int n,a[102],i,t,odd=0,even=0;
            scanf("%d",&n);
            for(i=0; i<n; i++)
            {
            scanf("%d",&a[i]);
            if(a[i]%2)
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

