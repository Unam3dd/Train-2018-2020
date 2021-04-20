#include "winbd_socket_object_ssl.h"

// Documentation OpenSSL : https://www.openssl.org/docs/man1.1.1/man3/SSL_write.html
//compile : g++ socket_winbd.cpp winbd_socket_object_ssl.cpp try_wbd_sock_ssl.cpp -s -ffunction-sections -fdata-sections -Wno-write-strings -fno-exceptions -fmerge-all-constants -static-libstdc++ -static-libgcc -std=c++11 -I"C:\vcpkg\installed\x86-windows\include" -lssl -lcrypto -lws2_32 -lcrypt32 -lgdi32 -lz -m32

using namespace std;

int main()
{
	Socket_SSL s(AF_INET, SOCK_STREAM, IPPROTO_TCP);
	if (s.Connect("192.168.1.27", 555) == 1)
	{
		cout << "Yeah Bro is Connected " << endl;
		int d = s.SendData((char*)"Hello World");
		cout << d << endl;
		string dd = s.RecvData(4096);
		cout << dd << endl;
	}
	return 0;
}