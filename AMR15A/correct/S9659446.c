
    #include<stdio.h>
    
     int main()
    {
     int t,s[100];
     scanf("%d",&t);
     while(t--)
     {
     scanf("%d",&s[t]);
     }
     if(s[0]%2==0 && s[t-1]%2==0)
     printf("READY FOR BATTLE");
     else
     printf("NOT READY");
     return 0;
    }

