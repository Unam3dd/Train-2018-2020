#pragma once
#include "console.h"
#include <sys/socket.h>
#include <netdb.h>
#include <arpa/inet.h>

typedef int SOCKET;

typedef struct Fdinfo
{
    char *address;
    int port;
} Fdinfo_t;

typedef struct ThreadHandle
{
    SOCKET fd;
    SOCKET *array;
    int n;
} ThreadHandle_t;

typedef struct Stream
{
    int in;
    int out;
} Stream_t;

SOCKET listen_on_new_port(int port);
void *handle_new_client(void *param);
void *std_stream(void *param);
int shell_session(SOCKET fd);
void list_connections(SOCKET *array);
void close_all_connections(SOCKET *array,int n);
void enter_session(int id,SOCKET *array);