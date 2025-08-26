#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int count_letters(const char *text);
int count_words(const char *text);
int count_sentences(const char *text);

int main()
{
    char text[1000];

    printf("Text: ");
    fgets(text, sizeof(text), stdin);

    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    float L = ((float)letters / words) * 100;
    float S = ((float)sentences / words) * 100;
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int grade = round(index);

    if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %d\n", grade);
    }

    return 0;
}

int count_letters(const char *text)
{
    int count = 0;
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (isalpha(text[i]))
        {
            count++;
        }
    }
    return count;
}

int count_words(const char *text)
{
    int count = 1; // Start at 1 assuming no leading/trailing/multiple spaces
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (text[i] == ' ')
        {
            count++;
        }
    }
    return count;
}

int count_sentences(const char *text)
{
    int count = 0;
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            count++;
        }
    }
    return count;
}