#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>

#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    // Check for correct usage
    if (argc != 2)
    {
        printf("Usage: ./recover card.raw\n");
        return 1;
    }

    // Open forensic image
    FILE *input = fopen(argv[1], "rb");
    if (input == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 1;
    }

    // Buffer to hold 512 bytes
    uint8_t buffer[BLOCK_SIZE];

    // File pointer for output JPEG
    FILE *output = NULL;

    // Counter for filenames
    int file_count = 0;

    // Flag to track if we're writing a JPEG
    bool writing = false;

    // Read blocks until end of file
    while (fread(buffer, BLOCK_SIZE, 1, input) == 1)
    {
        // Check for JPEG signature
        bool is_jpeg = buffer[0] == 0xff &&
                       buffer[1] == 0xd8 &&
                       buffer[2] == 0xff &&
                       (buffer[3] & 0xf0) == 0xe0;

        if (is_jpeg)
        {
            // Close previous file if needed
            if (writing)
            {
                fclose(output);
            }

            // Start new JPEG
            char filename[8];
            sprintf(filename, "%03d.jpg", file_count++);
            output = fopen(filename, "wb");
            writing = true;
        }

        // Write block if we're in a JPEG
        if (writing)
        {
            fwrite(buffer, BLOCK_SIZE, 1, output);
        }
    }

    // Cleanup
    if (output != NULL)
    {
        fclose(output);
    }

    fclose(input);
    return 0;
}