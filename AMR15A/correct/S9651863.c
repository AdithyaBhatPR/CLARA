
    #include<stdio.h>
    int main()
    {
        int n,k,e,o;
        scanf("%d",&n);
        e=o=0;
        while(n--)
        {
           scanf("%d",&k);
           if(k%2==0)
              e++;
           else
              o++;
        }
        if(e>o)
          printf("READY FOR BATTLE\n");
        else
          printf("NOT READY\n");
          
          
        return 0;
    }

