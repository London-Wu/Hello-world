#include <stdio.h>
#include <string.h>

int main()
{
        char *array[5] = {"Apple", "Boy", "Cat", "Dog", "Good"};
        char *(*p)[5] = &array;

        for (int i = 0; i < 5; i++)
        {
                for (int j = 0; j < 5; j++)
                {
                        if (i > strlen((*p)[j]) - 1)
                        {
                                printf("  ");
                        }
			else
			{
                        	printf("%c ", (*p)[j][i]);
			}
                }
                printf("\n");
        }

        return 0;
}
