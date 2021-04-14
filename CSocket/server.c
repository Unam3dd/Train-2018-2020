#include "headers/socket.h"

// Compile : gcc .\src\socket.c .\server.c -o server.exe -lws2_32 -s -w -O1 -O2

int main()
{
    SOCKET fd = Socket(AF_INET,SOCK_STREAM,IPPROTO_TCP);
    
    if (Bind(fd,555) == SOCKET_ERROR)
    {
        printf("[-] Error bind Address\n");
    }

    if (Listen(fd,5) == SOCKET_ERROR){
        printf("[-] Error Listen Address\n");
    }

    SOCKET nfd = Accept(fd);
    char *b = "Hello World";
    Send(nfd,b,0);
    closesocket(nfd);

    return (0);
}