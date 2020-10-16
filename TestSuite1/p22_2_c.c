#include <stdio.h>
 
void main()
{
    int num;

    for(int i = 0; i < 10;i++){
    	
    }
 
    printf("Enter a number: \n");
    scanf("%d", &num);
    if (num > 0)
        printf("%d is a positive number \n", num);
    else if (num < 0)
        printf("%d is a negative number \n", num);
    else
        printf("0 is neither positive nor negative");
}