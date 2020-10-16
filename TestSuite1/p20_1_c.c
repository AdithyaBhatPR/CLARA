#include <stdio.h>
#include <math.h>
//This function converts binary number to octal number
int binaryToOctal(long binarynum)
{
int oct = 0, dec = 0, i = 0;
    // converting binary to decimal
    while (bin != 0) {
        dec += (bin % 10) * pow(2, i);
        ++i;
        bin /= 10;
    }
    i = 1;
    // converting to decimal to octal
    while (dec != 0) {
        oct += (dec % 8) * i;
        dec /= 8;
        i *= 10;
    }
    return oct;
}
int main()
{
    long binarynum;

    printf("Enter a binary number: ");
    scanf("%ld", &binarynum);

    // calling the function here
    printf("Equivalent octal value: %d", binaryToOctal(binarynum));

    return 0;
}