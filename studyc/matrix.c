#include <stdio.h>
#include <string.h>
#include <math.h>

int main()
{
	char input[100];
	char *a=input;
	printf("enter the words:");
	scanf("%s",input);

	int size = sqrt(strlen(input));
	
	for(int i=0;i<size;i++)
	{
		for(int j=0;j<size;j++)
		{
			printf("%c ",*a);
			a++;
		}
		printf("\n");
	}

	return 0;
}
