#include <stdio.h>
#include <string.h>

int main(){
	char *programme[2];
	programme[0] = "/bin/sh";
	programme[1] = NULL;
	execve(programme[0],programme,0);
	return 0;
}
