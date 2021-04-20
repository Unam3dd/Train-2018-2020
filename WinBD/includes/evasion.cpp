#include "evasion.h"

using namespace std;

//Public

int Evasion::cf_exists(LPCSTR filename)
{
	return (check_file_exists(filename)); // return 1 or 0 for PathFileExists
}


int Evasion::check_regkey_exists(HKEY key, char* regkeys)
{
	HKEY regkey;
	LONG ret;
	ret = RegOpenKeyEx(key, regkeys, 0, KEY_READ, &regkey);
	if (ret == ERROR_SUCCESS)
	{
		RegCloseKey(regkey);
		return 1; // Exists
	}
	else
	{
		return 0; // Not Exists
	}
}

int Evasion::check_path_env_vmware(void)
{
	char ProgramFile[1024];
	char Path[1024];
	ExpandEnvironmentStrings((LPCSTR)"%PROGRAMFILES%",(LPSTR)ProgramFile,(DWORD)1024);
	PathCombine((LPSTR)Path, (LPSTR)ProgramFile, LPCSTR("VMWare\\"));
	return cf_exists((LPCSTR)Path);
}

int Evasion::check_path_env_virtualbox(void)
{
	char ProgramFile[1024];
	char Path[1024];
	ExpandEnvironmentStrings((LPCSTR)"%PROGRAMFILES%", (LPSTR)ProgramFile, (DWORD)1024);
	PathCombine((LPSTR)Path, (LPSTR)ProgramFile, LPCSTR("Oracle\\VirtualBox\\"));
	return cf_exists((LPCSTR)Path);
}

int Evasion::check_process(string& process)
{
	HANDLE snap;
	PROCESSENTRY32 pr = {};
	pr.dwSize = sizeof(pr);
	int p = 0;
	int ret = 0;
	snap = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);

	if (snap == INVALID_HANDLE_VALUE)
	{
		return 0;
	}

	if (Process32First(snap, &pr))
	{
		do {
			if (!StrCmpI(pr.szExeFile, process.c_str()))
			{
				ret = 1;
				break;
			}
		} while (Process32Next(snap, &pr));
	}
	CloseHandle(snap);

	return ret;
}

int Evasion::check_sndbox_filesystem(vector<LPCSTR> *v)
{
	LPCSTR file_sys[33];
	vector<char> l;
	int kk = -6;

	file_sys[0] = "=4VQch^iqmVQch^iqmOj^[n_(fia";

	file_sys[1] = "=4VQch^iqmVMsmn_g-,V^lcp_lmVjlf_nb(msm";
	file_sys[2] = "=4VQch^iqmVMsmn_g-,V^lcp_lmVjlf`m(msm";
	file_sys[3] = "=4VQch^iqmVMsmn_g-,V^lcp_lmVjlfgiom_(msm";
	file_sys[4] = "=4VQch^iqmVMsmn_g-,V^lcp_lmVjlfpc^_i(msm";
	file_sys[5] = "=4VQch^iqmVMsmn_g-,V^lcp_lmVjlfncg_(msm";
	file_sys[6] = "=4VQch^iqmVMsmn_g-,V^lcp_lmVjlfYjp-,(msm";
	file_sys[7] = "=4VQch^iqmVMsmn_g-,V^lcp_lmVjlfYj[l[pclnY-,(msm";
	
	file_sys[8] = "=4VQch^iqmVMsmn_g-,V^lcp_lmVP<irGiom_(msm";
	file_sys[9] = "=4VQch^iqmVMsmn_g-,V^lcp_lmVP<irAo_mn(msm";
	file_sys[10] = "=4VQch^iqmVMsmn_g-,V^lcp_lmVP<irM@(msm";
	file_sys[11] = "=4VQch^iqmVMsmn_g-,V^lcp_lmVP<irPc^_i(msm";
	file_sys[12] = "=4VQch^iqmVMsmn_g-,Vp\\ir^cmj(^ff";
	file_sys[13] = "=4VQch^iqmVMsmn_g-,Vp\\irbiie(^ff";
	file_sys[14] = "=4VQch^iqmVMsmn_g-,Vp\\irglrhj(^ff";
	file_sys[15] = "=4VQch^iqmVMsmn_g-,Vp\\iriaf(^ff";
	file_sys[16] = "=4VQch^iqmVMsmn_g-,Vp\\iriaf[ll[smjo(^ff";
	file_sys[17] = "=4VQch^iqmVMsmn_g-,Vp\\iriaf]loncf(^ff";
	file_sys[18] = "=4VQch^iqmVMsmn_g-,Vp\\iriaf_llilmjo(^ff";
	file_sys[19] = "=4VQch^iqmVMsmn_g-,Vp\\iriaf`__^\\[]emjo(^ff";
	file_sys[20] = "=4VQch^iqmVMsmn_g-,Vp\\iriafj[]emjo(^ff";
	file_sys[21] = "=4VQch^iqmVMsmn_g-,Vp\\iriafj[mmnblioabmjo(^ff";
	file_sys[22] = "=4VQch^iqmVMsmn_g-,Vp\\irm_lpc]_(_r_";
	file_sys[23] = "=4VQch^iqmVMsmn_g-,Vp\\irnl[s(_r_";
	file_sys[24] = "=4VQch^iqmVMsmn_g-,VP<ir=ihnlif(_r_";
	
	file_sys[25] = "=4VQch^iqmVMsmn_g-,V^lcp_lmVpgmlp](msm";
	file_sys[26] = "=4VQch^iqmVMsmn_g-,V^lcp_lmVpj]'m-(msm";

	file_sys[27] = "=4VQch^iqmVMsmn_g-,V^lcp_lmVpggiom_(msm";
	file_sys[28] = "=4VQch^iqmVMsmn_g-,V^lcp_lmVpgh_n(msm";
	file_sys[29] = "=4VQch^iqmVMsmn_g-,V^lcp_lmVpgrh_n(msm";
	file_sys[30] = "=4VQch^iqmVMsmn_g-,V^lcp_lmVpgba`m(msm";
	file_sys[31] = "=4Vqch^iqmVMsmn_g-,V^lcp_lmVpgr20(msm";
	file_sys[32] = "=4VQch^iqmVMsmn_g-,V^lcp_lmVba`m(msm";

	for (int xx = 0; xx < 33; xx++)
	{
		LPCSTR f = file_sys[xx];
		
		for (int ii = 0; ii < strlen(f); ii++)
		{
			l.push_back(f[ii]);
		}
		string d = evasion_decrypt_string(l, kk);
		int ret = check_file_exists((const char *)d.c_str());
		if (ret == 1)
		{
			v->push_back(d.c_str());
		}
		l.clear();
	}
}


int Evasion::check_anti_debug(void)
{
	if (IsDebuggerPresent() == 0)
	{
		return 0; // not present
	}
	else
	{
		return 1; // present
	}
}

// Private
int Evasion::check_file_exists(LPCSTR filename)
{
	return (PathFileExistsA(filename)); // 1 if exists // 0 if None
}

string Evasion::evasion_encrypt_string(vector<char> vt, int key)
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

string Evasion::evasion_decrypt_string(vector<char> dec, int key)
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