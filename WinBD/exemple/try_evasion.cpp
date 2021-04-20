#include "evasion.h"

// Compile : g++ evasion.cpp try_evasion.cpp -o try_evasion.exe -s -ffunction-sections -fdata-sections -Wno-write-strings -fno-exceptions -fmerge-all-constants -static-libstdc++ -static-libgcc -std=c++11 -lshlwapi

int main()
{
	Evasion ev;
	cout << ev.cf_exists((LPCSTR)"lololol.h") << endl;
	vector<LPCSTR> v;
	ev.check_sndbox_filesystem(&v);
	for (int i = 0; i < v.size(); i++)
	{
		cout << "Path Found : " << v[i] << endl;
	}
	string p = "firefox.exe";
	cout << ev.check_path_env_virtualbox() << endl;
	cout << ev.check_regkey_exists(HKEY_LOCAL_MACHINE, "SOFTWARE\\Python\\PythonCore\\2.7\\PythonPath") << endl;
	cout << ev.check_process(p) << endl;
	return 0;
}