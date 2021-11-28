#include <stdio.h>

void print_start(int height)
{
    for (int i = 0; i < height; i++)
    {
        // left half
        for (int j = 0; j < height; j++)
        {
            if (j < height - 1 - i)
                printf(" ");
            else
                printf("*");
        }

         // right half
        for (int j = height - 2; j >= 0; j--)
        {
            printf("%i", j);
            if (j < height - 1 - i)
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