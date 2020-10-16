
    #include<stdio.h>
    int main(void)
    {
     int N,i,c1=0,c2=0;
     scanf("%d",&N);
     int A[N];
     if(N>0&&N<101)
     {
      for(i=0;i<N;i++)
      scanf("%d",&A[i]);
      for(i=0;i<N;i++)
      {
       if(A[i]>=1&&A[i]<=100)
       {
        if(A[i]%2==0)
        c1+=1;
        else
        c2+=1;
       }
      }
      if(c1>c2)
      printf("READY FOR BATTLE");
      else
      printf("NOT READY");
     }
     return 0;
    }
     
    

