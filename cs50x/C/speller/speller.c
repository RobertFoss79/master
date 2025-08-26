#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

// Default dictionary
#define DICTIONARY "dictionaries/large"

int main(int argc, char *argv[])
{
    // Check for correct number of args
    if (argc != 2 && argc != 3)
    {
        printf("Usage: ./speller [DICTIONARY] text\n");
        return 1;
    }

    // Determine dictionary to use
    char *dictionary = (argc == 3) ? argv[1] : DICTIONARY;

    // Load dictionary
    if (!load(dictionary))
    {
        printf("Could not load %s.\n", dictionary);
        return 1;
    }

    // Try to open text
    char *text = (argc == 3) ? argv[2] : argv[1];
    FILE *file = fopen(text, "r");
    if (file == NULL)
    {
        printf("Could not open %s.\n", text);
        unload();
        return 1;
    }

    // Prepare to report misspellings
    printf("\nMISSPELLED WORDS\n\n");

    // Prepare to spell-check
    int index = 0, misspellings = 0, words = 0;
    char word[LENGTH + 1];
    char c;

    // Spell-check each word in text
    while (fread(&c, sizeof(char), 1, file))
    {
        if (isalpha(c) || (c == '\'' && index > 0))
        {
            word[index++] = c;
            if (index > LENGTH)
            {
                while (fread(&c, sizeof(char), 1, file) && isalpha(c))
                    ;
                index = 0;
            }
        }
        else if (isdigit(c))
        {
            while (fread(&c, sizeof(char), 1, file) && isalnum(c))
                ;
            index = 0;
        }
        else if (index > 0)
        {
            word[index] = '\0';
            words++;

            if (!check(word))
            {
                printf("%s\n", word);
                misspellings++;
            }

            index = 0;
        }
    }

    if (ferror(file))
    {
        fclose(file);
        printf("Error reading %s.\n", text);
        unload();
        return 1;
    }

    fclose(file);

    // Report summary
    printf("\nWORDS MISSPELLED:     %d\n", misspellings);
    printf("WORDS IN DICTIONARY:  %d\n", size());
    printf("WORDS IN TEXT:        %d\n", words);

    // Unload dictionary
    if (!unload())
    {
        printf("Could not unload %s.\n", dictionary);
        return 1;
    }

    return 0;
}