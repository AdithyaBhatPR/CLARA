#include <stdio.h>
int main(){
   int num1, num2, quot, rem;


   scanf("%d", &num1);


   scanf("%d", &num2);

   /* The "/" Arithmetic operator returns the quotient
    * Here the num1 is divided by num2 and the quotient
    * is assigned to the variable quot
    */
   quot = num1 / num2;

   /* The modulus operator "%" returns the remainder after
    * dividing num1 by num2.
    */
   rem = num1 % num2;

   printf("%d\n", quot);
   printf("%d", rem);

   return 0;
}