#pragma once
#include <iostream>
#include <windows.h>
#include <vector>
#include <stdlib.h>
#include <string>
#include <sstream>
#include <stdio.h>
#include <cstdlib>
#include <wininet.h>
#include <bits/stdc++.h>
#include <string.h>

#pragma comment(lib,"Wininet.lib");
using namespace std;

struct http_struct
{
	char* status_code;
	string content;
	char* status_text;
};

vector<string> split_link(const string& s, char delim);
string path_link(string link);
int download_to_ftp(char* filename, char* ftp_host, int ftp_port, char* ftp_user, char* ftp_pass);
int download_on_ftp(char* filename, char* ftp_host, int ftp_port, char* ftp_user, char* ftp_pass);
void send_http_get(string url,struct http_struct* wbd);
void send_https_get(string url,struct http_struct* wbd);