#include <stdio.h>

int main(void)
{
    int x, y;
    printf("What's x? ");
    while (scanf("%d", &x) != 1) // Ensure valid integer input for x
    {
        while (getchar() != '\n')
            ; // Clear invalid input
        printf("Invalid input. What's x? ");
    }

    printf("What's y? ");
    while (scanf("%d", &y) != 1) // Ensure valid integer input for y
    {
        while (getchar() != '\n')
            ; // Clear invalid input
        printf("Invalid input. What's y? ");
    }

    if (x < y)
    {
        printf("X is less than y\n");
    }
    else if (x > y)
    {
        printf("X is greater than y\n");
    }
    else
    {
        printf("X is equal to y\n");
    }
}