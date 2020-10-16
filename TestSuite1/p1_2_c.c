#include <stdio.h>
// Function to computer quotient
int quotient(int a, int b){
   return a / b;
}

// Function to computer remainder
int remainder(int a, int b){
   return a % b;
}

int main(){
    int num1, num2, quot, rem;

    scanf("%d", &num1);

    scanf("%d", &num2);
    
    //Calling function quotient()    
    quot = quotient(num1, num2);

    //Calling function remainder()    
    rem = remainder(num1, num2);
    printf("%d\n", quot);    
    printf("%d", rem);
    return 0;
}