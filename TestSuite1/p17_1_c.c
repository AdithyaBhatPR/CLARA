#include <stdio.h>
int fact(int num);
void main()
{
    int n, r, npr_var;
 

    scanf("%d", &n);

    scanf("%d", &r);
    
    /* nPr is also known as P(n,r), the formula is:
     * P(n,r) = n! / (n - r)! For 0 <= r <= n.
     */
    npr_var = fact(n) / fact(n - r);
    printf("%d",npr_var);
}
// Function for calculating factorial
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