
    #include<stdio.h>
    int main(){
    int n,i,r=0,nr=0;
    scanf("%d",&n);
    for(i=0;i<n;i++){
        int a;
        scanf("%d",&a);
        if (a%2 == 0)
            r++;
        else
            nr++;
        }
        if (r>nr)
            printf("READY FOR BATTLE");
        else
            printf("NOT READY");
            return 0;
        }

