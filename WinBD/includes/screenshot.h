#pragma once
#include <iostream>
#include <vector>
#include <Ole2.h>
#include <OleCtl.h>
#include <TlHelp32.h>

#pragma comment(lib,"OleAut32.Lib")

using namespace std;
vector<int> GetScreenResolution(int& w, int& h);
bool saveBitmap(LPCSTR filename, HBITMAP bmp, HPALETTE pal);
bool screenshot(int w, int h, LPCSTR fname);