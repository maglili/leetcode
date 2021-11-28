//給定一個unsigned short，問換算成16進制後四個值是不是一樣，是回傳1，否則0
#include <stdio.h>

int check_hex(unsigned short num)
{
    int res = num;
    int last_a, last_b;

    while (num)
    {
        last_a = (res & (0x000f));
        last_b = ((res>>4) & (0x000f));

        if (last_a != last_b)
            return 0;

        num >>= 4;
    }
    return 1;

}

int main(void)
{
    unsigned short a;
    printf("Input a:");
    scanf("%hi", &a);
    int res = check_hex(a);
    if (res)
        printf("True\n");
    else
        printf("False\n");
}