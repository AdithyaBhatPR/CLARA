
    #include<stdio.h>
    
    
    int main(){
    int n,i=0,w,c=0;
    scanf("%d",&n);
    while(i<n){
        scanf("%d",&w);
        if(w%2==0){c++;}
        i++;
    }
    if(c>n-c) printf("READY FOR BATTLE\n");
    else printf("NOT READY\n");
    
    return 0;
    }
    

