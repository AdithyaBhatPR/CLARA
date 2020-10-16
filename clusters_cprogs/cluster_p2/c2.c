#include <stdio.h>
int main()
{
    int num1, num2;
    float avg;


    scanf("%d",&num1);

    scanf("%d",&num2);

    avg= (float)(num1+num2)/2;

    //%.2f is used for displaying output upto two decimal places
    printf("%f",avg);

    return 0;
}