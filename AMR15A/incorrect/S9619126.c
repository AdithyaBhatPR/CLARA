
    #include<stdio.h>
    int main()
    {
       int a,i,j,count1,count2;
       scanf("%d",&a);
       for( i=0;i<a;i++)
     {
       int array[100];
       scanf("%d",&array[i]);
       count1=count2=0;
       for(j=0;array[j]!='\0';j++)
       {
         if(array[j]%2==0)
         count1++;
         else
         count2++;
       }
       
     }
      if(count1>count2)
       printf("\nREADY FOR BATTLE");
       else
       printf("\nNOT READY");
     return 0;
    }
    

