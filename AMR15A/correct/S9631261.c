
    #include<stdio.h>
    int main()
    {
    int  s , i ,count1 =0, count2 =0 ;
    scanf("%d",&s) ;
    int arr[s] ;
    for(i = 0 ; i<s ; i++)
        {
        scanf("%d",&arr[i]) ;
        if(arr[i]%2 == 0)
        {count1++ ;}
        else
        {
            count2++ ;
        }
        }
    
    if(count1 > count2)
    {
    printf("READY FOR BATTLE");
    }
    else
    {
    printf("NOT READY") ;
    }
    return 0 ;
    }

