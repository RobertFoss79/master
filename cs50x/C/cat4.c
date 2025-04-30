#include <stdio.h>

void meow(int n);

int main(void)
{
    int n;
    do
    {
        printf("Number: ");
        if (scanf("%d", &n) != 1) // Ensure valid integer input
        {
            while (getchar() != '\n')
                ;  // Clear invalid input
            n = 0; // Reset n to ensure the loop continues
        }
    } while (n < 1);
    meow(n);
}

void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("Meow\n");
    }
}