
    #include<stdio.h>
    int main()
    {
        int n,i,a,x=0,y=0;
        scanf("%d",&n);
        for(i=1;i<=n;i++)
        {
            scanf("%d",&a);
            if((a%2)==0)
            {
                x++;
            }
            else
            {
                y++;
            }
        }
        if(x>y)
        {
            printf("READY FOR BATTLE\n");
        }
        else
        {
            printf("NOT READY\n");
        }
        return 0;
    }
    

