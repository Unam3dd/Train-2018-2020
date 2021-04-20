#pragma once
#include <stdio.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <windows.h>
#include <string.h>

#pragma comment (lib, "Ws2_32.lib")
#define BUFFER_SIZE_DEFAULT 4096


int connect(SOCKET socks_instance, struct sockaddr_in session); // 0 = sucess | -1 = error
int send_data(SOCKET socks_instance, char* buffer);
int recv_data(SOCKET socks_instance, char* buffer, int len);
void execute_process(SOCKET socks_instance, char* process);
char* ghostbyaddr_ipv4(struct hostent* remote_host, const char* buffer_addr);
servent* gservbyport(struct servent* get_service_name, int port);
servent* gservbyname(struct servent* get_service_port, const char* name);