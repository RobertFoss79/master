#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int validate_key(const char *key);
void encrypt(const char *plaintext, const char *key);

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    if (!validate_key(argv[1]))
    {
        printf("Key must contain 26 unique alphabetic characters.\n");
        return 1;
    }

    char plaintext[1000];
    printf("plaintext: ");
    fgets(plaintext, sizeof(plaintext), stdin);

    printf("ciphertext: ");
    encrypt(plaintext, argv[1]);
    printf("\n");

    return 0;
}

int validate_key(const char *key)
{
    if (strlen(key) != 26)
        return 0;

    int seen[26] = {0};
    for (int i = 0; i < 26; i++)
    {
        if (!isalpha(key[i]))
            return 0;

        int index = toupper(key[i]) - 'A';
        if (seen[index])
            return 0;
        seen[index] = 1;
    }
    return 1;
}

void encrypt(const char *plaintext, const char *key)
{
    for (int i = 0; plaintext[i] != '\0'; i++)
    {
        char c = plaintext[i];
        if (isupper(c))
        {
            int index = c - 'A';
            putchar(toupper(key[index]));
        }
        else if (islower(c))
        {
            int index = c - 'a';
            putchar(tolower(key[index]));
        }
        else
        {
            putchar(c);
        }
    }
}