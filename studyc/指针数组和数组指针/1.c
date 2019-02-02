#include <stdio.h>

int main()
{
	char *array[5] = {"Apple","Boy","Cat","Dog","Egg"};
	char *(*a)[5] = &array;
	
	for(int i = 0;i < 5;i++)
	{
		for(int j = 0;*(*(*a+i)+j) != '\0';j++)
		{
			printf("%c ",*(*(*a+i)+j)); 
		}
		printf("\n");
	}
}
