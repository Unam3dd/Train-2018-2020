#pragma once
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <windows.h>

using namespace std;

class Wbd_PowerShell
{
public:
	string powershell_popen(string cmd);
	string powershell_command(string command);
};