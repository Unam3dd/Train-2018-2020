#include "winbd_getinformation.h"

using namespace std;

char *GetInfo::GetUsername()
{
	TCHAR Username[1024];
	char* u = Username;
	DWORD bytes = sizeof(Username);

	memset(Username, 0, sizeof(Username));
	GetUserNameA(Username, &bytes);
	return u;
}

char* GetInfo::GetComputername()
{
	TCHAR Computername[1024];
	char* c = Computername;
	DWORD bytes = sizeof(Computername);
	memset(Computername, 0, sizeof(Computername));
	GetComputerNameA(Computername, &bytes);
	return c;
}

char* GetInfo::GetSystemdir()
{
	TCHAR Sysdir[1024];
	char* s = Sysdir;
	memset(Sysdir, 0, sizeof(Sysdir));
	GetSystemDirectoryA(Sysdir, 1024);
	return s;
}

char* GetInfo::GetWindowsdir()
{
	TCHAR Windir[1024];
	char* w = Windir;
	memset(Windir, 0, sizeof(Windir));
	GetWindowsDirectoryA(Windir, 1024);
	return w;
}

char* GetInfo::GetOs()
{
	char Getos[1024];
	char* g = Getos;
	memset(Getos, 0, sizeof(Getos));
	ExpandEnvironmentStrings((LPCSTR)"%OS%", (LPSTR)Getos, (DWORD)1024);
	return g;
}

char* GetInfo::GetTemp()
{
	char GetT[1024];
	char* t = GetT;
	memset(GetT, 0, sizeof(GetT));
	ExpandEnvironmentStrings((LPCSTR)"%TEMP%", (LPSTR)GetT, (DWORD)1024);
	return t;
}

char* GetInfo::GetHomePath()
{
	char GetP[1024];
	char* p = GetP;
	memset(GetP, 0, sizeof(GetP));
	ExpandEnvironmentStrings((LPCSTR)"%HOMEPATH%", (LPSTR)p, (DWORD)1024);
	return p;
}

char* GetInfo::GetVersion()
{
	OSVERSIONINFOEX i;
	char buffer[4096];
	char* ret = buffer;
	ZeroMemory(&i, sizeof(OSVERSIONINFOEX));
	i.dwOSVersionInfoSize = sizeof(OSVERSIONINFOEX);
	GetVersionEx((LPOSVERSIONINFO)&i);
	snprintf(buffer, 4096, "[+] Windows Version : %u.%u\n[+] Build Number : %u\n[+] Windows Detected : \n", i.dwMajorVersion, i.dwMinorVersion,i.dwBuildNumber, i.dw);
	return ret;
}