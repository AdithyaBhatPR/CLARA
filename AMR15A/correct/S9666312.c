
    #include<stdio.h>
    
    
    int main()
    {
        int t,i,a=0,b=0,h;
        scanf("%d",&t);
        for(i=0;i<t;i++)
        {
            scanf("%d",&h);
            if(h%2==0)
                a++;
            else
                b++;
    
        }
        if(a>b)
            printf("READY FOR BATTLE");
        else
            printf("NOT READY");
        return 0;
    
    }
    
    
    
    
    

