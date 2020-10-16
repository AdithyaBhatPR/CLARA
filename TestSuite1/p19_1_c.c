#include <stdio.h>
#include <math.h>

long decimalToBinary(int n)
{
    long binarynum = 0;
    int rem, temp = 1;

    // while (decimalnum!=0)
    // {
    //     rem = decimalnum%2;
    //     decimalnum = decimalnum / 2;
    //     binarynum = binarynum + rem*temp;
    //     temp = temp * 10;
    // }

    for (int i = 31; i >= 0; i--) { 
        int k = n >> i; 
        if (k & 1) {
            // cout << "1"; 
            rem = 1;

        }
        else{
            // cout << "0"; 
            rem = 0;

        }
        binarynum = binarynum + rem*temp;

            temp = temp * 10;

    } 
    return binarynum;
}

int main()
{
    int decimalnum;
    printf("Enter a Decimal Number: ");
    scanf("%d", &decimalnum);
    printf("Equivalent Binary Number is: %ld", decimalToBinary(decimalnum));
    return 0;
}