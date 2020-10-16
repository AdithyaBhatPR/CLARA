
    #include<stdio.h>
    int main()
    {
    short n,m,i,c=0;
    scanf("%hi",&n);
    i=n;
    while(i--)
    {scanf("%hi",&m);
    if(m%2==0) c++;
    }
    if(2*c>n) printf("READY FOR BATTLE\n");
    else printf("NOT READY\n");
    return 0;
    }
    

