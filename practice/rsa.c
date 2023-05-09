#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
	unsigned long long int i, j, f_num;

	(void)argc;

	FILE *fp = fopen(argv[1], "r");

	if (fp == NULL)
		printf("Unable to open file for reading");

	while (fscanf(fp, "%lld", &f_num) == 1)
	{
		for(i = 2; i <= f_num; i++)
		{
			for(j = f_num; j >= 1; j--)
			{
				if((j * i) == f_num)
				{
					break;
					printf("n = %lld * %lld\n", j, i);
				}
			}
		}
	}
	fclose(fp);
	return (0);
}
