#pragma once
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <string.h>
#include <errno.h>
#include <iphlpapi.h>
#include <icmpapi.h>
#include <mswsock.h>
#include "http.h"
#include "http_server.h"
#include "openssl/evp.h"
#include "openssl/err.h"
#include "pthread.h"
#pragma warning(disable: 4700 4477)
#pragma comment(lib,"ws2_32.lib")
#pragma comment(lib,"iphlpapi.lib")
#pragma comment(lib,"mswsock.lib")

typedef int BOOL;
#define TRUE 1
#define FALSE 0
#define STDIN_FILENO _fileno(stdin)
#define STDOUT_FILENO _fileno(stdout)
#define STDERR_FILENO _fileno(stderr)
#define SOCKET_NONBLOCKMODE -1
#define SOCKET_BLOCKMODE 0
#define WSA_ERROR_MESSAGE_SIZE 256
#define MAX_SIZE_ADDRESS 16
#define VERSION_WCNET 1
#define SERVICE_MAX_CHAR_SIZE 10
#define SEND_ENTIRE_FILE 0
#define SEND_DEFAULT_SIZE 0
#define ERROR_ALLOCATE_MEMORY ((void *)-1)
#define MAX_BUFFER_SIZE 65536

//////////////////////////////////////////////////////
//               SOCKET STRUCT                      //
//////////////////////////////////////////////////////

typedef struct peer
{
    char *addr;
    int port;
    int err_code;
} peer_t;


typedef struct UDPPacket
{
    char *address;
    int port;
    int err;
} UDPPacket_t;


typedef struct sockname
{
    char *address;
    int port;
} sockname_t;


typedef struct addressinfo
{
    char *address;
    int port;
    ADDRESS_FAMILY family;
    int err;
} addressinfo_t;

typedef struct hostinfo
{
    char **addr_list;
    char *name;
} hostinfo_t;

typedef struct PortScan {
    char *ip;
    int startport;
    int maxport;
    int verbosity;
    int timeoutms;
} PortScan_t;

typedef struct ICMPResponse {
    char addr[16];
    unsigned long status;
    unsigned long round_trip_time;
    unsigned short data_size;
    unsigned short reserved;
    void *data;
} ICMPResponse_t;

typedef struct StreamInSocket
{
    int in;
    SOCKET out;
} StreamInSocket_t;

typedef struct Client
{
    SOCKET client_fd;
    struct sockaddr_in *client_info;
} Client_t;


///////////////////////////////////////////////////////
//               SOCKET FUNCTION                     //
///////////////////////////////////////////////////////
int WINSOCK_INITIALIZE(void);
int WINSOCK_CLEANUP(void);
SOCKET Socket(int family,int type,int protocol);
int Connect(SOCKET fd,const char *host,int port);
int ConnectTimeout(SOCKET fd,const char *host,int port,int ms);
int Bind(SOCKET fd,int port);
int Listen(SOCKET fd,int maxcon);
int Send(SOCKET fd,char *buffer,int flags);
int SendEx(SOCKET fd,char *buffer,int nbytes,int flags);
int SendTimeout(SOCKET fd,const char *data,unsigned long ms,int flags);
int SendTimeoutEx(SOCKET fd,const char *data,unsigned long ms,int nbytes,int flags);
int SendTo(SOCKET fd,char *data,int len_data,const char *host,int port,int flags);
int Recv(SOCKET fd,char *buffer,int nbytes,int flags);
char *RecvEx(SOCKET fd,int nbytes,int *bytes_recv,int flags);
int RecvMemset(SOCKET fd,char *buffer,int nbytes,int flags);
int RecvTimeout(SOCKET fd,char *buffer,int nbytes,int flags,int ms);
void RecvEx_free(char *buffer);
int RecvFrom(SOCKET fd,char *data,int nbytes,int flags,UDPPacket_t *info);
void ExecuteAndStreamProcess(SOCKET fd,char *process);
void WSAstrerror(int err);
SOCKET Accept(SOCKET fd);
SOCKET AcceptClient(SOCKET fd,struct sockaddr_in *clientinfo,int *size_client);
peer_t GetPeerName(SOCKET fd);
SOCKADDR_IN session(const char *host,int port);
SOCKADDR_IN sessionbind(int port);
int Getservicebyport(int port,char *buffer);
int Getservicebyname(char *name,char *protocol);
char **Gethostbyname(char *name,int *address_len);
void free_addr_list(char **addr_list);
int setblocking(SOCKET fd,BOOL value);
int Getsockname(SOCKET fd,sockname_t *sockname);
int Getnameinfo(const char *addr,int port,char *hostname,char *serviceinfo);
int Gethostbyaddr(const char *addr,hostinfo_t *hi);
void GethostbyaddrFree(hostinfo_t *hi);
void PortScan(PortScan_t *target);
void to_network_little_endian(const char *addr,char *output);
int Ping(char *addr,char *buffer,ICMPResponse_t *icmp);
int SendFile(SOCKET fd,const char *filename);
int SendFileBinary(SOCKET fd,const char *filename);
long to_long(char* number);
unsigned char *base64_encode(unsigned char *input,int len);
unsigned char *base64_decode(unsigned char *input,int len);
void *ThreadStreamInSocket(void *param);
int InteractWithFd(SOCKET fd);