
    #include<stdio.h>
    #include<string.h>
    int main ()
    {
        int N=0,i=0,j=0,weapons[100],q=0;
        scanf("%d",&N);
        for(i=0;i<N;i++)
        {
            scanf("%d",&weapons[i]);
            if(weapons[i]%2==0)
            {
                j++;
            }
            else
            {
                q++;
            }
        }
        if(q>=j)
        {
                    printf("NOT READY");
        }
        else
                    printf("READY FOR BATTLE");
        q=0;j=0;
        return(0);
    }
     

