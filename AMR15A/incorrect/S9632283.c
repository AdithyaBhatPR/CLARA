
    #include<stdio.h>
    #include<stdlib.h>
    int main()
    {
        int N;
        scanf("%d",&N);
        int weapon[N];
        int y=0,a=0,b=0;
        while(y<N){
            if(weapon[y]%2==0)
            {
                a++;
            }
            else{
                b++;
            }
            y++;
        }
        if(a>b){
            printf("READY FOR BATTLE\n");
        }
        else{
            printf("NOT READY\n");
        }
        return 0;
    }

