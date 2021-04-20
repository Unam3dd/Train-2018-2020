#include "winbd_socket_object_ssl.h"

using namespace std;

// public

Socket_SSL::Socket_SSL(short family, int type, int protocol)
{
	this->Socket_SSL::family = family;
	this->Socket_SSL::type = type;
	this->Socket_SSL::protocol = protocol;
	SOCKET socks = Socket_SSL::init_socket(); // socket init
	this->Socket_SSL::sobject = socks;
}


int Socket_SSL::Connect(string host, int port)
{
	this->Socket_SSL::host = host;
	this->Socket_SSL::port = port;
	sockaddr_in config = s_setting();
	if (connect(Socket_SSL::sobject, config) != -1)
	{
		Socket_SSL::Attach_Socket_SSL();
		return 1; // Connected !
	}
	else
	{
		return 0; // Fail Connect
	}
}


int Socket_SSL::SendData(char* data)
{
	Sleep(100);
	int s = SSL_write(Socket_SSL::cssl_object, data, strlen(data));
	if (s > 0) {
		return 1; // success !
	}
	else {
		return 0; // failed !
	}
}

string Socket_SSL::RecvData(int bytes)
{
	Sleep(100);
	char buffer[bytes];
	string output;
	memset(buffer, 0, sizeof(buffer));
	int r = SSL_read(Socket_SSL::cssl_object, (char*)buffer,(bytes-1));

	if (r > 0)
	{
		output = buffer;
		return output; // Success !
	}
	else
	{
		output = "NULL";
		return output; // Failed !
	}
}

// private
SOCKET Socket_SSL::init_socket()
{
	SOCKET s;
	WSADATA wsa;

	WSAStartup(MAKEWORD(2, 2), &wsa);
	s = WSASocket(Socket_SSL::family, Socket_SSL::type, Socket_SSL::protocol, 0, 0, 0);
	return s;
}

sockaddr_in Socket_SSL::s_setting()
{
	struct sockaddr_in s;
	s.sin_family = Socket_SSL::family;
	s.sin_addr.s_addr = inet_addr(Socket_SSL::host.c_str());
	s.sin_port = htons(Socket_SSL::port);
	return s;
}

void Socket_SSL::Attach_Socket_SSL()
{
	SSL_CTX* sslctx;
	SSL* cssl;

	SSL_load_error_strings();
	SSL_library_init();
	sslctx = SSL_CTX_new(SSLv23_method());
	cssl = SSL_new(sslctx);
	SSL_set_fd(cssl, (int)Socket_SSL::sobject);
	SSL_connect(cssl);
	this->Socket_SSL::cssl_object = cssl;
}