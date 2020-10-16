#include <stdio.h>
#include <math.h>
int binaryToDecimal(long binarynum)
{
    int dec = 0, i = 0, rem;
    while (n != 0) {
        rem = n % 10;
        n /= 10;
        dec += rem * pow(3, i);
        ++i;
    }
    return dec;
}

int main()
{
    long binarynum;
    printf("Enter a binary number: ");
    scanf("%ld", &binarynum);

    printf("Equivalent decimal number is: %d", binaryToDecimal(binarynum));
    return 0;
}