#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// gcc shellcode_exec.c -m32 -z execstack -o shellexec
// shellexec `cat shell.bin`

int main(int argc,char **argv)
{
	if (argc < 2){
		printf("usage : %s <shellcode>",argv[0]);
		exit(EXIT_FAILURE);
	}

	void (*shellcode)() = (void((*)())) (argv[1]);

	shellcode();

	return EXIT_SUCCESS;
}
