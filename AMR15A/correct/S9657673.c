
    #include <stdio.h>
    #include <stdlib.h>
    
    int main()
    {
        int n,i,a,s1=0,s2=0;
     
        scanf("%d",&n);
        
        for(i=0;i<n;i++)
        {scanf("%d",&a);
        if(a%2==0)
            s1+=a;
        else
            s2+=a;
        }
        if(s1>s2)
            printf("READY FOR BATTLE");
        else
            printf("NOT READY");
        return 0;
    }
    

