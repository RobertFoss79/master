#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int avg = round((image[i][j].rgbtRed +
                             image[i][j].rgbtGreen +
                             image[i][j].rgbtBlue) /
                            3.0);
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sumRed = 0, sumGreen = 0, sumBlue = 0;
            int count = 0;

            for (int di = -1; di <= 1; di++)
            {
                for (int dj = -1; dj <= 1; dj++)
                {
                    int ni = i + di;
                    int nj = j + dj;

                    if (ni >= 0 && ni < height && nj >= 0 && nj < width)
                    {
                        sumRed += image[ni][nj].rgbtRed;
                        sumGreen += image[ni][nj].rgbtGreen;
                        sumBlue += image[ni][nj].rgbtBlue;
                        count++;
                    }
                }
            }

            temp[i][j].rgbtRed = round(sumRed / (float)count);
            temp[i][j].rgbtGreen = round(sumGreen / (float)count);
            temp[i][j].rgbtBlue = round(sumBlue / (float)count);
        }
    }

    // Copy blurred values back to original image
    for (int i = 0; i < height; i++)
        for (int j = 0; j < width; j++)
            image[i][j] = temp[i][j];
}

// Detect edges using Sobel operator
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    int Gx[3][3] = {
        {-1, 0, 1},
        {-2, 0, 2},
        {-1, 0, 1}};

    int Gy[3][3] = {
        {-1, -2, -1},
        {0, 0, 0},
        {1, 2, 1}};

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sumRx = 0, sumRy = 0;
            int sumGx = 0, sumGy = 0;
            int sumBx = 0, sumBy = 0;

            for (int di = -1; di <= 1; di++)
            {
                for (int dj = -1; dj <= 1; dj++)
                {
                    int ni = i + di;
                    int nj = j + dj;

                    if (ni >= 0 && ni < height && nj >= 0 && nj < width)
                    {
                        int weightX = Gx[di + 1][dj + 1];
                        int weightY = Gy[di + 1][dj + 1];

                        RGBTRIPLE pixel = image[ni][nj];

                        sumRx += pixel.rgbtRed * weightX;
                        sumRy += pixel.rgbtRed * weightY;

                        sumGx += pixel.rgbtGreen * weightX;
                        sumGy += pixel.rgbtGreen * weightY;

                        sumBx += pixel.rgbtBlue * weightX;
                        sumBy += pixel.rgbtBlue * weightY;
                    }
                }
            }

            int red = round(sqrt(sumRx * sumRx + sumRy * sumRy));
            int green = round(sqrt(sumGx * sumGx + sumGy * sumGy));
            int blue = round(sqrt(sumBx * sumBx + sumBy * sumBy));

            temp[i][j].rgbtRed = red > 255 ? 255 : red;
            temp[i][j].rgbtGreen = green > 255 ? 255 : green;
            temp[i][j].rgbtBlue = blue > 255 ? 255 : blue;
        }
    }

    // Copy edge-detected values back to original image
    for (int i = 0; i < height; i++)
        for (int j = 0; j < width; j++)
            image[i][j] = temp[i][j];
}