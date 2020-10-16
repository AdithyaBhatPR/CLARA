#include <stdio.h>
#include <math.h>
/* This function converts the octal number "octalnum" to the
 * decimal number and returns it.
 */
long octalToDecimal(int octalnum)
{
       int decimalNumber = 0, i = 0;
    while(octalNumber != 0)
    {
        decimalNumber += (octalNumber%10) * pow(8,i);
        ++i;
        octalNumber/=10;
    }
    i = 1;
    return decimalNumber;
}
int main()
{
    int octalnum;

    printf("Enter an octal number: ");
    scanf("%d", &octalnum);

    printf("Equivalent decimal number is: %ld", octalToDecimal(octalnum));

    return 0;
}