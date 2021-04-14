#pragma once
#include <iostream>
#include "socket_winbd.h"
#include <openssl/ssl.h>

using namespace std;

class Socket_SSL
{
	public:
		Socket_SSL(short family, int type, int protocol);
		int Connect(string host, int port);
		int SendData(char* data);
		string RecvData(int bytes);
		
	private:
		string host;
		int port;
		short family;
		int type;
		int protocol;
		SOCKET sobject;
		SSL* cssl_object;


		SOCKET init_socket();
		sockaddr_in s_setting();
		void Attach_Socket_SSL();
};