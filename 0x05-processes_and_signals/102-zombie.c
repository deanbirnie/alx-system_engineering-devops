#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - keeps the zombie process running
 *
 * Return: 0 (success)
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point for the program
 *
 * Return: 0 (success)
 */
int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();

		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
		}
		else if (pid == 0)
		{
			exit(0);
		}
		else
		{
			perror("fork");
			exit(1);
		}
	}

	infinite_while();

	return (0);
}
