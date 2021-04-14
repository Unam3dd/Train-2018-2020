#pragma once
#include <stdio.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <windows.h>
#include <string.h>

#pragma comment (lib, "Ws2_32.lib")
#define BUFFER_SIZE_DEFAULT 4096


int connect(SOCKET socks_instance, struct sockaddr_in session); // 0 = sucess | -1 = error
