#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>

void *myturn(void * args)
{
	int *iptr = (int *)malloc(sizeof(int));
	iptr = args;
	for (int x = 0;x<5;x++)
	{
		sleep(1);
		puts("Try This");
	}

	return iptr;
}

void simple_function_say(const char *say)
{
	puts(say);
}

int main()
{
	int *results;
	printf("test !\n");
	sleep(2);
	printf("Lets go !\n");
	pthread_t pth;
	int value = 6;
	pthread_create(&pth,NULL,myturn,&value); // create thread and start it
	pthread_join(pth,(void *)&results); // join thread (wait thread by thread)
	printf("Return value from thread functions myturn : %d\n",*results);
    return (0);
}
