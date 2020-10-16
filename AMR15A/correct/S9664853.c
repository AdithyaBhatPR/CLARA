
    #include <stdio.h>
    #include <stdlib.h>
    
    int main()
    {
       int t,rev=0,unrev,i;
       scanf("%d",&t);
       int arr[t];
        for(i=0;i<t;i++)
       {
           scanf("%d",&arr[i]);
           if((arr[i]%2)==0)
            rev++;
       }
    
       unrev=t-rev;
       if(unrev >= rev)
        printf("NOT READY");
        else
        printf("READY FOR BATTLE");
       return 0;
    }
    

