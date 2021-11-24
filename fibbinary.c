/*
Check if input number is Fibbinary.
https://www.geeksforgeeks.org/fibbinary-numbers-no-consecutive-1s-binary-o1-approach/
*/
#include <stdio.h>

int inspect_bit(int a)
{
    int ans = a&(a>>1);
    if (ans == 0)
        return 0;
    else
        return 1;;
}

int main(void)
{
    // 21 : 10101, 13: 1101
    int a;
    printf("Input a number: ");
    scanf("%i",&a);
    printf("Ans: %i\n", inspect_bit(a));
}