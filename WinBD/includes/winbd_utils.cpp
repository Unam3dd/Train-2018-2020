#include "winbd_utils.h"

#include <iostream>
#include <stdio.h>
#include <direct.h>
#include <vector>
#include <stdlib.h>
#include <io.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <errno.h>
#include <ShlObj.h>
#include <shellapi.h>
#include <lmcons.h>
#include <fstream>
#include <sstream>
#include <windows.h>

using namespace std;
#define BUFFER_SIZE_DEFAULT 4096
#define READ_ONLY _S_IREAD
#define WRITE_READ_ONLY _S_IWRITE
#define READ_WRITE_ONLY _S_IREAD | _S_IWRITE

int pwd(char* buffer)
{
    char buffer_pwd[4096];
    if (getcwd(buffer_pwd, sizeof(buffer_pwd)) != NULL)
    {
        strcpy(buffer, buffer_pwd);
        return 1;
    }
    else {
        return 0;
    }
}

int cd(char* path)
{
    if (chdir(path) == 0) {
        return 1;
    }
    else {
        return 0;
    }
}

vector<string> split(const string& s,char delim)
{
    vector<string> result;
    stringstream ss(s);
    string item;

    while (getline(ss, item, delim)) {
        result.push_back(item);
    }

    return result;
}

bool endswith(const std::string& str, const std::string& suffix) // if return code is 1 its True else if is 0 its False
{
    return str.size() >= suffix.size() && 0 == str.compare(str.size() - suffix.size(), suffix.size(), suffix);
}

bool startswith(const std::string& str, const std::string& prefix)
{
    return str.size() >= prefix.size() && 0 == str.compare(0, prefix.size(), prefix);
}

int makedir(const char *path)
{
    if (_mkdir(path) == 0)
    {
        return 1; // dir created !
    }
    else
    {
        return -1; // error dir created !
    }
}

int removedir(const char* path)
{
    if (_rmdir(path) == 0)
    {
        return 1; // dir removed
    }
    else
    {
        return -1; // dir not removed
    }
}

int changemod(const char* filename,int m)
{
    if (_chmod(filename, m) != -1)
    {
        return 1; // mode set !
    }
    else
    {
        return -1; // mode set error !
    }
}

string read_file(string filename, string buffer_return)
{
    string buffer;
    ifstream infile;
    infile.open(filename, ios::app);

    if (infile.is_open())
    {
        while (!infile.eof())
        {
            getline(infile, buffer);
            buffer_return.append(buffer);
            buffer_return.append("\n");
        }
        infile.close();
        return buffer_return;
    }
    else {
        string erf = "Error Read File";
        return erf;
    }
}

string read_file_binary(string filename, string buffer_return)
{
    string buffer;
    ifstream infile;
    infile.open(filename, ios::binary);

    if (infile.is_open())
    {
        while (!infile.eof())
        {
            getline(infile, buffer);
            buffer_return.append(buffer);
            buffer_return.append("\n");
        }
        infile.close();
        return buffer_return;
    }
    else {
        string e = "Error ReadFile";
        return e;
    }
}

int user_admin(void)
{
    if (IsUserAnAdmin() == TRUE)
    {
        return TRUE;
    }
    else
    {
        return FALSE;
    }
}

int shell_exec_user(LPCSTR process, LPCSTR args, LPCSTR dir,INT SHWD)
{
    if (ShellExecuteA(NULL, "open", process, args, dir, SHWD) == 0)
    {
        return 1;
    }
    else
    {
        return -1;
    }
}

int remove_file(LPCSTR filename)
{
    if (DeleteFileA(filename) != 0)
    {
        return 1; // filename is deleted !
    }
    else
    {
        return -1; // error filename not deleted
    }
}

void GetSystemInformation(struct winbdinfo *info)
{
    TCHAR name[256];
    DWORD buffer = 32276;
    DWORD buffer2 = 32276;
    string concat_name;
    string concat_computer_name;
    TCHAR name_comp[256];
    MEMORYSTATUS mi;
    SYSTEM_INFO siSysInfo;
    DWORD dwVersion = 0;
    DWORD dwMajorVersion = 0;
    DWORD dwMinorVersion = 0;
    DWORD dwBuild = 0;


    GetUserNameA(name, &buffer);
    GetComputerNameA(name_comp, &buffer2);
    GetSystemInfo(&siSysInfo);
    dwVersion = GetVersion();

    concat_name = name;
    concat_computer_name = name_comp;

    dwMajorVersion = (DWORD)(LOBYTE(LOWORD(dwVersion)));
    dwMinorVersion = (DWORD)(HIBYTE(LOWORD(dwVersion)));

    if (dwVersion < 0x80000000)
    {
        dwBuild = (DWORD)(HIWORD(dwVersion));
    }

    memset(&mi, 0, sizeof(MEMORYSTATUS));
    mi.dwLength = sizeof(MEMORYSTATUS);
    GlobalMemoryStatus(&mi);
    info->total_memory = mi.dwTotalPhys;
    info->total_memory_virtual = mi.dwTotalVirtual;
    info->total_memory_mb = mi.dwTotalPhys / (1024 * 1024);
    info->total_memory_available = mi.dwAvailPhys;
    info->total_memory_available_mb = mi.dwAvailPhys / (1024 * 1024);
    info->username = concat_name;
    info->computer_name = concat_computer_name;
    info->oem_id = siSysInfo.dwOemId;
    info->number_processor = siSysInfo.dwNumberOfProcessors;
    info->page_size = siSysInfo.dwPageSize;
    info->minimum_application_address = siSysInfo.lpMinimumApplicationAddress;
    info->maximum_application_address = siSysInfo.lpMaximumApplicationAddress;
    info->active_processor_mask = siSysInfo.dwActiveProcessorMask;
    info->major_version = dwMajorVersion;
    info->minor_version = dwMinorVersion;
    info->build_version = dwBuild;
}

char* cmd_popen_char(const char* command, const char* mode, char* buffer)
{
    FILE* fp;
    fp = _popen(command, mode);
    if (fp == NULL) {
        _pclose(fp);
        return "0";
    }
    else {
        int size_of_entry_buffer = sizeof(buffer);
        char buffer_local[size_of_entry_buffer];
        while (fgets(buffer_local, sizeof(buffer_local), fp))
        {
            strcat(buffer, buffer_local);
        }
        return buffer;
        _pclose(fp);
    }
}

void hide_console(void)
{
    FreeConsole();
    HWND hWnd = GetConsoleWindow();
    ShowWindow(hWnd, SW_MINIMIZE);
    ShowWindow(hWnd, SW_HIDE);
}

string tohex(string buffer)
{
    string strconcat2;

    for (unsigned int i = 0; i < buffer.size(); i++)
    {
        stringstream strconcat;
        strconcat << hex << (int)buffer[i];
        strconcat2 += strconcat.str();
    }
    buffer = strconcat2;
    return buffer;
}

string xor_string_enc_dec(string data, char key[])
{
    string xor_enc = data;

    for (int x = 0; x < xor_enc.size(); x++)
    {
        xor_enc[x] = data[x] ^ key[x % (strlen(key) / sizeof(char))];
    }

    return xor_enc;
}

char* raw_input(char* input_string) {
    char input_console[BUFFER_SIZE_DEFAULT];
    printf("%s", input_string);
    return fgets(input_console, BUFFER_SIZE_DEFAULT, stdin);
}

int int_input(char* input_string)
{
    int number;
    printf("%s", input_string);
    scanf("%d", &number);
    return number;
}

int StartsWith(const char* a, const char* b)
{
    if (strncmp(a, b, strlen(b)) == 0) return 1;
    return 0;
}


int check_file_exists(LPCSTR filename)
{
    return PathFileExistsA(filename); // 1 if exists // 0 if None
}