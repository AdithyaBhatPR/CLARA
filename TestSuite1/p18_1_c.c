#include <stdio.h>
 
int fact(int num);
int ncr(n,r);
 
void main()
{
    int n, r, ncr_var;
 

    scanf("%d", &n);

    scanf("%d", &r);
    /* ncr is also represented as C(n,r), the formula is:
     * C(n,r) = n! / ( r!(n - r)! ). For 0 <= r <= n.
     */
    printf("%d",ncr(n,r));
}
/* This function is used to find the 
 * factorial of given number num
 */
int ncr(n,r){
    return fact(n) / (fact(r) * fact(n - r));
}
int fact(int num)
{
    int k = 1, i;
    // factorial of 0 is 1
    if (num == 0)
    {
        return(k);
    }
    else
    {
        for (i = 1; i <= num; i++)
    {
            k = k * i;
	}
    }
    return(k);
}