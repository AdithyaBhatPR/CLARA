
    #include<stdio.h>
    int main()
    {
    int n;
    int i,j;
    int e,o;
    scanf("%d",&n);
    e=o=0;
    for(i=0;i<n;i++)
    { scanf("%d",&j);
          if(j%2==0)
            e++;
          else
            o++;
    }
    if(e>o)
    printf("READY FOR BATTLE");
    else
    printf("NOT READY");
    return 0;
    }

