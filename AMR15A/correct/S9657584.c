
    #include <stdio.h>
    #include <stdlib.h>
    
    int main()
    {   int s,i,l=0,u=0,n;
        int w[100];
        scanf("%d",&s);
        for(i=0;i<s;i++)
        {
            scanf("%d",&w[i]);
            if(w[i]%2==0)
                {
                    l++;
                }
    
            else
                {
                    u++;
                }
    
    
        }
        n=l-u;
        if(n>0)
            printf("READY FOR BATTLE");
        else
            printf("NOT READY");
    
        return 0;
    }
    

