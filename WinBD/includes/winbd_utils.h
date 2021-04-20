#pragma once

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
#include <Shlwapi.h>
#include <lmcons.h>
#include <wtypes.h>
#include <fstream>
#include <sstream>
#include <windows.h>

using namespace std;
#define BUFFER_SIZE_DEFAULT 4096
#define READ_ONLY _S_IREAD
#define WRITE_READ_ONLY _S_IWRITE
#define READ_WRITE_ONLY _S_IREAD | _S_IWRITE

struct winbdinfo{
    SIZE_T total_memory;
    SIZE_T total_memory_virtual;
    SIZE_T total_memory_mb;
    SIZE_T total_memory_available;
    SIZE_T total_memory_available_mb;
    string username;
    string computer_name;
    DWORD oem_id;
    DWORD number_processor;
    DWORD page_size;
    DWORD processor_type;
    LPVOID minimum_application_address;
    LPVOID maximum_application_address;
    DWORD active_processor_mask;
    DWORD major_version;
    DWORD minor_version;
    DWORD build_version;
};

int pwd(char* buffer); // return 1 if true and print the buffer variable if you want show path else return 0 on error
int cd(char* path); // return 1 if true else return 0 if false
vector<string> split(const string& s,char delim); //return vector split string
bool endswith(const std::string& str, const std::string& suffix); // if return code is 1 its True else if is 0 its False
bool startswith(const std::string& str, const std::string& prefix); // if return code is 1 its True else if is 0 its False
int makedir(const char* path); // if return code is 1 dir is created else if return code is -1 dir failed !
int removedir(const char* path); // if return code is 1 dir is created else if return code is -1 dir failed !
int changemod(const char* filename, int m); // mode changed if code return is 1 else return code is 0
string read_file(string filename, string buffer_return);
string read_file_binary(string filename, string buffer_return);
int user_admin(void); // return 1 if user is admin else return 0 if user is not admin
int shell_exec_user(LPCSTR process, LPCSTR args, LPCSTR dir,INT SHWD); // if return 1 command executed else if return -1 command not executed
int remove_file(LPCSTR filename); // if return code is 1 file is removed else is return code is -1
void GetSystemInformation(struct winbdinfo* info);
char* cmd_popen_char(const char* command, const char* mode, char* buffer);
void hide_console(void);
string tohex(string buffer);
string xor_string_enc_dec(string data, char key[]);
char* raw_input(char* input_string);
int int_input(char* input_string);
int StartsWith(const char* a, const char* b);
int check_file_exists(LPCSTR filename);