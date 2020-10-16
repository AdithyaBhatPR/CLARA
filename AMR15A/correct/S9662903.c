
    #include<stdio.h>
    int main()
    {
     int n,i,c=0,d=0;
     int a[101];
     scanf("%d",&n);
     for(i=0;i<n;i++)
     {
         scanf("%d",&a[i]);
         if(a[i]%2==0)
            c++;
         else
            d++;
     }
     if(c>d)
        printf("READY FOR BATTLE\n");
     else
        printf("NOT READY\n");
    return 0;
    }
    
    

