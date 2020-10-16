
    #include<stdio.h>
    int main()
    {
        int n,a[100],ce=0,co=0,i;
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
            if(a[i]%2==0)
                ce++;
            else if(a[i]%2!=0)
                co++;
        }
        if(ce>co)
            printf("READY FOR BATTLE\n");
        else
            printf("NOT READY\n");
        return 0;
    }
    

