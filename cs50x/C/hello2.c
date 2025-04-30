#include <stdio.h>
#include <string.h> // Include string.h for strchr function

int main(void)
{
    char answer[100]; // Allocate a buffer for the name
    printf("What's your name? ");
    if (fgets(answer, sizeof(answer), stdin) != NULL) // Read input from the user
    {
        // Remove the newline character if present
        char *newline = strchr(answer, '\n');
        if (newline)
        {
            *newline = '\0';
        }
    }
    printf("Hello, %s\n", answer);
}