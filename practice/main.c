#include <stdio.h>

int main(void)
{
	char *n = "Holy ALX";
	int i = 0;

	for (; n[i] != '\0'; i++)
		putchar(n[i]);

	putchar('\n');
	return (0);
}
