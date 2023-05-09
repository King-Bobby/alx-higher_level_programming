#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	int n = atoi(argv[1]);
	int a = atoi(argv[2]);

	if (argc != 3)
		printf("NUmber is not accurate.\n");

	if (argc == 3)
		printf("Answer = %d\n", (n * a));

	/*printf("argc: %d\n", argc);	
	for (n = 0; n < argc; n++)
		printf("argv[%d] = %s\n", n, argv[n]);
*/
	return (0);
}
