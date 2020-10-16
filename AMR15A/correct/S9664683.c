
    #include<stdio.h>
    int main()
    {
    int s,w,odd=0,even=0,i;
    
    scanf("%d",&s);
    if(s<=100){
        
        for(i=0;i<s;i++)
        {
        scanf("%d",&w);
        if(w%2==0)even++;
        else odd++;
        }
        }
    if(even>odd)printf("READY FOR BATTLE");
    else printf("NOT READY");
    return 0;
    }
    

