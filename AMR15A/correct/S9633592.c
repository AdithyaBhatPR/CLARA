
    #include <stdio.h>
    #include <stdlib.h>
    
    int main(){
      int N,e=0,o=0,x;
      scanf("%d",&N);
      while(N--){
        scanf("%d",&x);
        if(x%2)
          o++;
        else
          e++;
      }
      if(e>o)
        printf("READY FOR BATTLE");
      else
        printf("NOT READY");
      return 0;
    }
    

