
    #include<stdio.h>
    int main()
    {
    int n,m[102],i,odd=0,even=0;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
    scanf("%d",&m[i]);
    }
    for(i=0;i<n;i++)
    {
    if(m[i]%2==0)
    even++;
    else
    odd++;
    }
    if(even>odd)
    printf("ready for battle");
    else
    printf("not ready");
    return 0;
    }
    

