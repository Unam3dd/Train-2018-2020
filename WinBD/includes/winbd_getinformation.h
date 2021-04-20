#include <iostream>
#include <Windows.h>

using namespace std;

class GetInfo
{
public:
	char* GetUsername(void);
	char* GetComputername(void);
	char* GetSystemdir(void);
	char* GetWindowsdir(void);
	char* GetOs(void);
	char* GetTemp(void);
	char* GetHomePath(void);
	char* GetVersion(void);
};