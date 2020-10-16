
        #include<stdio.h>
        int main()
        {
        int n,i,c=0,b=0;
        int a[100];
        scanf("%d",&n);
        for(i=0;i<n;i++)
        scanf("%d",&a[i]);
        for(i=0;i<n;i++)
        {
        if(a[i]%2==0)
        c++;
        else
        b++;
        }
        if(c>b)
        printf("READY FOR BATTLE\n");
        else
        printf("NOT READY\n");
        return 0;
        } 

