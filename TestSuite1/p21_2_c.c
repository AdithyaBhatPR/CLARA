#include <stdio.h>
#include <math.h>
//This function converts octal number to binary number
long octalToBinary(int oct)
{
    int dec = 0, i = 0;
    long long bin = 0;
    // converting octal to decimal
    while (oct != 0) {
        dec += (oct % 10) * pow(8, i);
        ++i;
        oct /= 10;
    }
    i = 1;
   // converting decimal to binary
    while (dec != 0) {
        bin += (dec % 2) * i;
        dec /= 2;
        i *= 10;
    }
    return bin;
}
int main()
{
    int octalnum;

    printf("Enter an octal number: ");
    scanf("%d", &octalnum);

    //Calling the function octaltoBinary
    printf("Equivalent binary number is: %ld", octalToBinary(octalnum));

    return 0;
}