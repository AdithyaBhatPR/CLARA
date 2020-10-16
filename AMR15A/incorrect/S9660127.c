
    #include <stdio.h>
    
    int main (){
       // int arr1[99];
        int n,i;
        int arr[99];
        int c1,c2;
        printf("Enter the number of soldiers: ");
        scanf("%d",&n);
        printf("Enter their weapons(using spaces) ");
        for(i=0;i<n;i++){
            scanf("%d",&arr[i]);
            if(arr[i]%2!=0){
                c1+=1;
            }
            else if(c2%2==0){
                c2+=1;
            }
        }
        if(c1>c2){
            printf("NOT READY");
        }
        else
            printf("READY FOR BATTLE");
        return 0;
    }
    

