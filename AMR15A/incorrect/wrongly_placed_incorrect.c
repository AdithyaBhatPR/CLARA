#include<stdio.h>
    int main()
    {
     int i,A[100],even=0,odd=0,N;
     printf("Enter the number of soldiers \n");
     scanf("%d", &N);
     for(i=1;i<=N;i++)
     {
      scanf("%d",&A[i]);
      if(A[i]%2==0)
      {
       even++;
      }
      else
      {
       odd++;
      }
     }
     if(even>odd)
     printf("\nREADY FOR BATTLE");
     else
     printf("\nNOT READY");
     return 0;
    }

