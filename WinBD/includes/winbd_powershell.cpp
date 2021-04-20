#include "winbd_powershell.h"

using namespace std;


string Wbd_PowerShell::powershell_popen(string cmd)
{
	char buffer[4096];
	string out;
	memset(buffer, 0, sizeof(buffer));
	sprintf(buffer, "powershell.exe -C %s", cmd.c_str());
	FILE* fp;

	fp = _popen(buffer, "rb");
	if (fp == NULL)
	{
		out = "[!] Error Popen Command !";
		return out;
	}
	else
	{
		memset(buffer, 0, sizeof(buffer));
		while (fgets(buffer, sizeof(buffer), fp))
		{
			out += buffer;
		}
		return out;
	}
}

string Wbd_PowerShell::powershell_command(string command)
{
	char process[4096];
	char output_char[65000];
	string o;
	STARTUPINFO sinfo;
	PROCESS_INFORMATION pinfo;
	SECURITY_ATTRIBUTES sec;
	HANDLE stdin_read, stdin_write;
	HANDLE stdout_stderr_read, stdout_stderr_write;
	DWORD Read, avail;

	sec.nLength = sizeof(SECURITY_ATTRIBUTES);
	sec.bInheritHandle = TRUE;
	sec.lpSecurityDescriptor = NULL;

	CreatePipe(&stdin_read, &stdin_write, &sec, 0);
	CreatePipe(&stdout_stderr_read, &stdout_stderr_write, &sec, 0);


	memset(&sinfo, 0, sizeof(sinfo));
	sinfo.cb = sizeof(sinfo);
	sinfo.dwFlags = (STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW);
	sinfo.wShowWindow = SW_HIDE;
	sinfo.hStdInput = stdin_read;
	sinfo.hStdOutput = stdout_stderr_write;
	sinfo.hStdError = stdout_stderr_write;

	memset(process, 0, sizeof(process));
	sprintf(process, "powershell.exe -c %s", command.c_str());
	CreateProcessA(NULL, process, &sec, 0, TRUE, 0, 0, 0, &sinfo, &pinfo);
	Sleep(1000);
	memset(output_char, 0, sizeof(output_char));
	while (PeekNamedPipe(stdout_stderr_read, output_char, 1, &Read, &avail, 0))
	{
		if (Read > 0)
		{
			if (ReadFile(stdout_stderr_read, output_char, sizeof(output_char) - 1, &Read, NULL) && Read != 0)
			{
				output_char[Read] = '\0';
				o.append(output_char);
				Sleep(100);
			}
		}
		else
		{
			CloseHandle(stdout_stderr_read);
			CloseHandle(stdin_read);
			CloseHandle(stdin_write);
			break;
		}
	}
	return o;
}