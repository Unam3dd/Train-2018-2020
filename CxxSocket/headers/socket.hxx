#pragma once
#include <iostream>
using namespace std;

#ifdef _WIN32
    #pragma comment (lib, "Ws2_32.lib")
    #include <winsock2.h>
    #include <cstdio>
    #include <ws2tcpip.h>
    #include <windows.h>

    typedef struct{
        char *address;
        int port;
    } peer_t;

    fd_set Write,Err;
    struct timeval t;

    class WinSocket
    {
        public:
            WinSocket(short Family,int Type,int Protocol);
            int Connect(string host,int port);
            int ConnectTimeout(string host,int port,int ms);
            int Bind(int port);
            int Listen(int maxcon);
            SOCKET Accept();
            int Send(string data,int flags);
            int SendTimeout(string data,unsigned long ms,int flags);
            int CSend(SOCKET fd,string data,int flags);
            int CSendTimeout(SOCKET fd,string data,unsigned long ms,int flags);
            string RecvData(int bytes,int flags);
            string RecvDataTimeout(int bytes,int flags,unsigned long ms);
            string CRecvData(SOCKET fd,int bytes,int flags);
            string CRecvDataTimeout(SOCKET fd,int bytes,int flags,unsigned long ms);
            void ExecuteAndStreamProcess(string process);
            void CExecuteAndStreamProcess(SOCKET fd,string process);
            peer_t GetPeerName(SOCKET ns);
            int Close();
            int CClose(SOCKET fd);

        private:
            string host;
            int port;
            short Family;
            int Type;
            int Protocol;
            SOCKET sobject;
            SOCKET InitSocket();
            sockaddr_in session();
            sockaddr_in sessionbind();
            int rdata(SOCKET s,char *buffer,int len,int flags);
            int rdatat(SOCKET s,char *buffer, int len,int flags,unsigned long ms);
    };

#elif __unix__
    #include <sys/types.h>
    #include <sys/socket.h>
    #include <netinet/in.h>
    #include <arpa/inet.h>
    #include <stdio.h>
    #include <cstring>
    #include <unistd.h>
    #include <netdb.h>
    typedef int SOCKET;
    typedef struct sockaddr_in SOCKADDR_IN;
    typedef struct sockaddr SOCKADDR;

    #define INVALID_SOCKET -1
    #define SOCKET_ERROR -1
    #define closesocket(s) close(s)

    typedef struct{
        char *address;
        int port;
    } peer_t;
    
    
    struct timeval t;

    class LinSocket{
        public:
            LinSocket(int Family,int Type,int Protocol);
            int Connect(string host,int port);
            int ConnectTimeout(string host,int port,int ms);
            int Bind(int port);
            int Listen(int maxcon);
            SOCKET Accept();
            int Send(string data,int flags);
            int SendTimeout(string data,int seconds,int flags);
            int CSend(SOCKET fd,string data,int flags);
            int CSendTimeout(SOCKET fd,string data,int seconds,int flags);
            string RecvData(int bytes,int flags);
            string RecvDataTimeout(int bytes,int flags,int seconds);
            string CRecvData(SOCKET fd,int bytes,int flags);
            string CRecvDataTimeout(SOCKET fd,int bytes,int flags,int seconds);
            void ExecuteAndStreamProcess(string process);
            void CExecuteAndStreamProcess(SOCKET fd,string process);
            peer_t GetPeerName(SOCKET fd);
            int Close();
            int CClose(SOCKET fd);
        private:
            string host;
            int port;
            int Family;
            int Type;
            int Protocol;
            SOCKET sobject;
            SOCKET InitSocket();
            sockaddr_in session();
            sockaddr_in sessionbind();
            int rdata(SOCKET s,char *buffer,int len,int flags);
            int rdatat(SOCKET s,char *buffer, int len,int flags,int seconds);
    };

#endif
