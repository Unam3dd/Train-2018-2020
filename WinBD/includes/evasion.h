#pragma once
#include <iostream>
#include <Windows.h>
#include <Shlwapi.h>
#include <TlHelp32.h>
#include <vector>

using namespace std;

class Evasion
{
public:
	int check_sndbox_filesystem(vector<LPCSTR> *v); // true = 1 | false = 0
	int cf_exists(LPCSTR filename); // true = 1 | false = 0
	int check_path_env_vmware(void); // true = 1 | false = 0;
	int check_path_env_virtualbox(void); // true = 1 | false = 0:
	int check_process(string& process); // true = 1 | false = 0;
	int check_regkey_exists(HKEY key, char* regkey); // true = 1 | false = 0;
	string evasion_encrypt_string(vector<char> vt, int key);
	string evasion_decrypt_string(vector<char> dec, int key);
	int check_anti_debug(void); // true = 1 | false = 0
private:
	int check_file_exists(LPCSTR filename); // true = 1 | false = 0;
};