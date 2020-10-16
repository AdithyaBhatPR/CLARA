
    #include<stdio.h>
    int main()
    {
       int a,i,j,count1,count2,b;
       count1=count2=0;
       scanf("%d",&a);
       for( i=0;i<a;i++)
     {
       
       scanf("%d",&b);
       
       
         if(b%2==0)
         count1++;
         else
         count2++;
       }
       
     
      if(count1>count2)
       printf("\nREADY FOR BATTLE");
       else
       printf("\nNOT READY");
     return 0;
    }
    

