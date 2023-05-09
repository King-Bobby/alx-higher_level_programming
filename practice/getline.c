#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*getline(char *buffer, size_t *num, file *stream);
*/

int main(void)
{
	size_t num = 10;
	char *buffer = malloc(sizeof(char));

	printf("Enter Club ");

	getline(&buffer, &num, stdin);

	printf("Club name is %s Buffer size is %ld\n", buffer, num);

	free(buffer);
	return (0);
}
