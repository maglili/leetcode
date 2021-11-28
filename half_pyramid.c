#include <stdio.h>

void print_start(int height)
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < height; j++)
        {
            if (j < height - i - 1 )
                printf(" ");
            else
                printf("*");
        }
        printf("\n");
    }
    printf("\n");

}

int main(void)
{
    int height;
    printf("Input height: ");
    scanf("%i",&height);

    print_start(height);
}