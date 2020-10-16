
    #include<stdio.h>
    int main()
    {
    int n,m[102],i,so=0,se=0;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
    scanf("%d",&m[i]);
    }
    for(i=0;i<n;i++)
    {
    if(m[i]%2==0)
    se++;
    else
    so++;
    }
    if(se>so)
    printf("ready for battle\n");
    else
    printf("not ready\n");
    return 0;
    } 

