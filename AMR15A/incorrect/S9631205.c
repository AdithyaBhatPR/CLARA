
    #include<stdio.h>
    int main()
    {
    int n,s[100],i,e=0,o=0;
    printf("enter the no of soldier");
    scanf("%d\n",&n);
    printf("weapons");
    for(i=0;i<n;i++)
    scanf("%d ",&s[i]);
    for(i=0;i<n;i++)
    {
    if(s[i]%2==0)
    e++;
    else
    o++;
    }
    if(e>0)
    printf("ready");
    else
    printf("not raedy");
    return 0;
    }

