
     #include<stdio.h>
    
    
    int main()
    {
        int n;
        scanf("%d",&n);
       int i,t,cnt1=0,cnt2=0;
         for(i=0;i<n;i++)
         {
             scanf("%d",&t);
             if(t%2==0)
                cnt1++;
             else
                cnt2++;
         }
          if(cnt1>cnt2)
            printf("READY FOR BATTLE");
          else
            printf("NOT READY");
       return 0;
    }
    

