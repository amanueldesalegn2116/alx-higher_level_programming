#include <stdio.h>
/**
* print_triangle - Prints A Left-aligned Triangle, Followed By A New Line
* @siz":"Size Of The Triangle
*/
void print_triangle(int size)
{
    size = 10;
    if(size <= 0)
    {
        printf("\n");
    }
    else
    {
        int i, j;

        for (i = 1; i <= size; i++)
        {
            for (j = 1; j <= size; j++)
            {
                if (j <= size - i)
                {
                    printf(" "); // Print spaces to align the triangle to the left
                }
                else
                {
                    printf("#"); // Print '#' characters for the triangle
                }
            }
            printf("\n"); // Move to the next line after printing each row
        }
    }
}
