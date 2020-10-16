
    #include <stdio.h>
    
    int main(){
        int n, lSldrs = 0, ulSldrs = 0, i;
        
        scanf("%d", &n);
        int wpns[n];
        
        for (i = 0; i < n; i++){
            scanf("%d", &wpns[i]);
            if (wpns[i] % 2 == 0)
                lSldrs++;
            else
                ulSldrs++;
        }
        if (lSldrs > ulSldrs)
            printf("READY FOR BATTLE\n");
        else
            printf("NOT READY");
        return 0;
    }

