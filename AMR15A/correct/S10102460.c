
    #include <stdio.h>
    
    int main()
    {
     int n,i,odd,even,b,a[101];
     i = 0;
     odd = 0;
     even = 0;
     scanf("%d",&n);
     for(i=0;i<n;i++)
       {
        scanf("%d",&a[i]);
        b=a[i];
        if(b%2==0)
         {
          even = even + 1;
         }
        else
         {
          odd = odd + 1;
         }
        }
        if(odd >= even)
        {
         printf("NOT READY");
        }
        if(even > odd)
        {
         printf("READY FOR BATTLE");
        }
    	return 0;
    }
    

