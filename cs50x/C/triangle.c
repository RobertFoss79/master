#include <stdio.h>
#include <cs50.h>

bool valid_triangle(float x, float y, float z);

int main(void)
{
    // Example usage
    float a = get_float("Side a: ");
    float b = get_float("Side b: ");
    float c = get_float("Side c: ");

    if (valid_triangle(a, b, c))
    {
        printf("That's a valid triangle!\n");
    }
    else
    {
        printf("That's not a valid triangle.\n");
    }
}

bool valid_triangle(float x, float y, float z)
{
    // Check for all positive sides
    if (x <= 0 || y <= 0 || z <= 0)
    {
        return false;
    }

    // Check that sum of any two sides greater than third
    if ((x + y <= z) || (x + z <= y) || (y + z <= x))
    {
        return false;
    }

    // If we passed both tests, we're good!
    return true;
}
