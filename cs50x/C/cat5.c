#include <stdio.h>

int get_positive_int(void);
void meow(int n);

int main(void)
{
    int times = get_positive_int();
    meow(times);
}

int get_positive_int(void)
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
    return n;
}

void meow(int n)
{
    for (int i = 0; i < n; i++)
    {
        printf("Meow\n");
    }
}