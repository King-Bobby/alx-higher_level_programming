#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
	printf("This is EXE2\n");
	char *args[] = {"helo", "me", '\0'};
	execv("./exe1", args);
	printf("back to exe2.c\n");
	return (0);
}
