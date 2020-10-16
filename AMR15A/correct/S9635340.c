
    #include <stdio.h>
    #include <stdlib.h>
    
    int main()
    {
        int n;
        scanf("%d",&n);
       int count=0,count2=0;
        //printf("%d\n",t);
        while(n--)
        {
            int a;
          scanf("%d",&a);
            (a%2==0)?(count=count+1):(count2=count2+1);
    
        }
        (count>count2)?(printf("%s","READY FOR BATTLE")):(printf("%s","NOT READY"));
        return 0;
    }
    

