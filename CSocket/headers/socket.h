#pragma once

typedef struct{
    char *address;
    int port;
} peer_t;

#ifdef _WIN32
    #pragma comment (lib,"Ws2_32.lib")
    #include <winsock2.h>
    #include <ws2tcpip.h>
    #include <stdio.h>
    #include <windows.h>

    
    fd_set Write,Err;
    struct timeval t;

    SOCKET Socket(short family,int type,int protocol);
    int Connect(SOCKET fd,const char *host,int port);
    int ConnectTimeout(SOCKET fd,const char *host, int port, int ms);
    int Bind(SOCKET fd,int port);
    int Listen(SOCKET fd,int maxcon);
    SOCKET Accept(SOCKET fd);
    int Send(SOCKET fd,const char *data,int flags);
    int SendTimeout(SOCKET fd,const char *data,unsigned long ms,int flags);
    int RecvData(SOCKET fd,char *buffer,int bytes,int flags);
    int RecvDataTimeout(SOCKET fd,char *buffer,int bytes,int flags,unsigned long ms);
    peer_t GetPeerName(SOCKET fd);
    SOCKADDR_IN session(const char *host,int port);
    SOCKADDR_IN sessionbind(short family,int port);
    void ExecuteAndStreamProcess(SOCKET fd,const char *process);
    int rdata(SOCKET s, char* buffer, int len,int flags);

#elif __unix__
    #include <sys/types.h>
    #include <sys/socket.h>
    #include <netinet/in.h>
    #include <arpa/inet.h>
    #include <netdb.h>
    #include <unistd.h>
    #include <string.h>
    
    struct timeval t;
    #define INVALID_SOCKET -1
    #define SOCKET_ERROR -1
    #define closesocket(s) close(s)

    typedef int SOCKET;
    typedef struct sockaddr_in SOCKADDR_IN;

    SOCKET Socket(short family,int type,int protocol);
    int Connect(SOCKET fd,const char *host,int port);
    int ConnectTimeout(SOCKET fd,const char *host, int port, int ms);
    int Bind(SOCKET fd,int port);
    int Listen(SOCKET fd,int maxcon);
    SOCKET Accept(SOCKET fd);
    int Send(SOCKET fd,const char *data,int flags);
    int SendTimeout(SOCKET fd,const char *data,unsigned long ms,int flags);
    int RecvData(SOCKET fd,char *buffer,int bytes,int flags);
    int RecvDataTimeout(SOCKET fd,char *buffer,int bytes,int flags,unsigned long ms);
    peer_t GetPeerName(SOCKET fd);
    SOCKADDR_IN session(const char *host,int port);
    SOCKADDR_IN sessionbind(short family,int port);
    void ExecuteAndStreamProcess(SOCKET fd,const char *process);

    

#endif
