#include <stdio.h>
#include <math.h>
/* This function converts the decimal number "decimalnum"
 * to the equivalent octal number
 */
int decimalToOctal(int decimalnum)
{
        int octalNumber = 0, i = 1;
    while (decimalNumber != 0)
    {
        octalNumber += (decimalNumber % 8) * i;
        decimalNumber /= 8;
        i *= 10;
    }
    return octalNumber;
}
int main()
{
    int decimalnum;

    printf("Enter a Decimal Number: ");
    scanf("%d", &decimalnum);

    printf("Equivalent Octal Number: %d", decimalToOctal(decimalnum));

    return 0;
}