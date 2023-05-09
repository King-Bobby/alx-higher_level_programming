#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
	printf("Exe1 PID : %u\n", getpid());
	char * args[] = {"hello", "Worl", '\0'};
	execv("./exe2", args);
	printf("Back to exe1\n");
	return (0);
}
