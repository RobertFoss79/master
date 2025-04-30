#include <stdio.h>

int main(void)
{
    char c;
    printf("Do you agree? ");
    scanf(" %c", &c); // Read a single character, skipping leading whitespace
    if (c == 'y' || c == 'Y')
    {
        printf("Agreed.\n");
    }
    else if (c == 'n' || c == 'N')
    {
        printf("Not agreed.\n");
    }
}