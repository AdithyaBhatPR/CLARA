
    #include<stdio.h>
    #include<math.h>
    int main()
    {
        int i,k,n1,n2,army[100];
        n1=0;
        n2=0;
        printf("give the no of soldiers\n");
        scanf("%d",&k);
        
        for(i=0;i<k;i++)
        {
            scanf("%d",&army[i]);
        }
        for(i=0;i<k;i++)
            {
                if((army[i]%2)==0)
                      n1++;
                else
                    n2++;
            }
        if(n1>n2)
                printf("READY FOR BATTLE\n");
            else
                printf("NOT READY\n");
        return 0;
    }

