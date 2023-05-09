#include <stdio.h>
#include <string.h>

/*strtok(char *str, char *delim)*/

int main(void)
{
	int i;
	char s[] = "Happy Sunday, to you, all.";
	char d[] = ",";

	char *word = strtok(s, d);
	while (word != NULL)
	{
		printf("%s\n", word);
		word = strtok(NULL, d);
	}

	for (i = 0; i < 25; i++)
	{
		if (s[i] == '\0')
			printf("NULL\n");
		else
			printf("%c", s[i]);
	}

	return (0);
}
