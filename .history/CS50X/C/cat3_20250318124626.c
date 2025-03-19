#include <stdio.h>

void meow(int n);

int main(void)
{
    {
        meow(5);
    }
}

void meow(int n)
{
    for (int i = 0; i < 3; i++)
    {
        printf("Meow\n");
    }
}