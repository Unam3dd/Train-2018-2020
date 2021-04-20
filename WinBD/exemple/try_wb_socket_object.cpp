#include "winbd_socket_object.h"

// Author : Unam3dd
// compile : g++ socket_winbd.cpp winbd_socket_object.cpp try_wb_socket_object.cpp -lws2_32 -s -ffunction-sections -fdata-sections -Wno-write-strings -fno-exceptions -fmerge-all-constants -static-libstdc++ -static-libgcc -o try.exe

using namespace std;

int main()
{
	Socket s(AF_INET,SOCK_STREAM,IPPROTO_TCP);
	string host = "192.168.1.27";
	cout << s.GetHostnamebyaddr(host.c_str()) << endl;
	cout << s.Gservbyport(22) << endl;
	cout << s.Gservbyname("ssh") << endl;
	int c = s.Connect("192.168.1.27", 555);
	if (c == 1)
	{
		char lol[4096] = "Hello World";
		int ss = s.SendData(lol);
		cout << ss << endl;
		string r = s.RecvData(4096);
		cout << r << endl;
	}
	return 0;
}