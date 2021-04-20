#include "winbd_utils.h"
#include <iostream>

//compile : g++ winbd_utils.cpp test_winbd_utils.cpp -o ww.exe -s -ffunction-sections -fdata-sections -Wno-write-strings -fno-exceptions -fmerge-all-constants -static-libstdc++ -static-libgcc -std=c++11

using namespace std;

int main()
{
	cout << user_admin << endl;
	char path[4096];
	char dir[] = "C:\\Users\\SAM";

	if (cd(dir) == 1)
	{
		int pd = pwd(path);
		cout << path << endl;
		cout << pd << endl;
		string hl = "hello/world";
		vector<string> sl = split(hl,'/');
		for (int i = 0; i < sl.size(); i++)
		{
			cout << sl[i] << endl;
		}

		bool d = startswith(hl, "h");
		cout << d << endl;

		int mk = makedir("lol2");
		if (mk == 1)
		{
			cout << "Lol Created !" << endl;
		}
		else {
			cout << "Lol Not Created  " << endl;
		}

		LPCSTR f = "mdr.txt";
		
		if (remove_file(f) == 1)
		{
			cout << "File Deleted !" << endl;
		}
		else
		{
			cout << "File Not Deleted !" << endl;
		}

		/*SYSTEM_INFO sysinfo;
		MEMORYSTATUS mi;
		memset(&mi, 0, sizeof(MEMORYSTATUS));
		mi.dwLength = sizeof(MEMORYSTATUS);
		GlobalMemoryStatus(&mi);
		GetNativeSystemInfo(&sysinfo);
		cout << sysinfo.dwProcessorType << endl;
		cout << mi.dwTotalPhys / (1024 * 1024) << endl;*/
		winbdinfo l;
		GetSystemInformation(&l);
		cout << l.total_memory_mb << endl;
		cout << l.total_memory << endl;
		cout << l.total_memory_virtual << endl;
		cout << l.username << endl;
		cout << l.computer_name << endl;
		cout << l.oem_id << endl;
		cout << l.minimum_application_address << endl;
		cout << l.maximum_application_address << endl;
		cout << l.major_version << endl;
		cout << l.minor_version << endl;
		cout << l.build_version << endl;
		char buffer[4096];
		cmd_popen_char("dir", "rb", buffer);
		cout << buffer << endl;

	}
	else {
		cout << "Path Not Found !" << endl;
	}
	return 0;
}