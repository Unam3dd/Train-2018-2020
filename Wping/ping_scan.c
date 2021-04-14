//Compile : cl.exe ping_scan.c /TC /link Ws2_32.lib Iphlpapi.lib
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <iphlpapi.h>
#include <icmpapi.h>
#include <ipexport.h>

#define WSA_ERROR_MESSAGE_SIZE 256

#pragma comment(lib,"Ws2_32.lib")
#pragma comment(lib,"Iphlpapi.lib")


typedef struct ICMPResponse {
    char addr[16];
    unsigned long status;
    unsigned long round_trip_time;
    unsigned short data_size;
    unsigned short reserved;
    void *data;
} ICMPResponse_t;


void Wstrerror(int errorcode)
{
    char buffer[WSA_ERROR_MESSAGE_SIZE] = {0};
    FormatMessageA(FORMAT_MESSAGE_FROM_SYSTEM | FORMAT_MESSAGE_IGNORE_INSERTS,NULL,errorcode,MAKELANGID(LANG_NEUTRAL,SUBLANG_DEFAULT),buffer,WSA_ERROR_MESSAGE_SIZE,NULL);
    fprintf(stderr,"[-] Error %d : %s\n",errorcode,buffer);
}


int Ping(char *addr,char *buffer,ICMPResponse_t *icmp,DWORD ms)
{
    HANDLE hIcmp;
    unsigned long ip = INADDR_NONE;
    DWORD dwReturnValue = 0, dwReplySize = 0;
    void *ReplyBuffer = NULL;
    char data[32] = {0};
    struct in_addr raddr = {0};

    ip = inet_addr(addr);

    if (ip == INADDR_NONE)
        return (GetLastError());
    
    strncpy(data,buffer,31);
    
    hIcmp = IcmpCreateFile();

    if (hIcmp == INVALID_HANDLE_VALUE){
        return (GetLastError());
    }

    dwReplySize = sizeof(ICMP_ECHO_REPLY) + sizeof(data);
    ReplyBuffer = (void *)malloc(dwReplySize);

    if (ReplyBuffer == NULL)
        return (-1);

    dwReturnValue = IcmpSendEcho(hIcmp,ip,data,sizeof(data),NULL,ReplyBuffer,dwReplySize,ms);
    
    PICMP_ECHO_REPLY IcmpReply = (PICMP_ECHO_REPLY)ReplyBuffer;
    raddr.S_un.S_addr = IcmpReply->Address;
    strncpy(icmp->addr,inet_ntoa(raddr),sizeof(icmp->addr));
    icmp->status = IcmpReply->Status;
    
    icmp->data = IcmpReply->Data;

    if (icmp->data == NULL)
        icmp->data = NULL;

    icmp->data_size = IcmpReply->DataSize;
    
    icmp->reserved = IcmpReply->Reserved;
    icmp->round_trip_time = IcmpReply->RoundTripTime;
    

    IcmpCloseHandle(hIcmp);
    return (0);
}

unsigned long to_long(char *number)
{
    unsigned long to_long = 0;

    for (int i = 0;number[i] >= '0' && number[i] <= '9';i++)
    {
        to_long *= 10;
        to_long += number[i]++ & 0xF;
    }

    return (to_long);
}


typedef struct ThreadParam
{
    char address[16];
    char buffer[32];
    int verbose;
    DWORD seconds;
} ThreadParam_t;

DWORD WINAPI Thread(void *lparam)
{
    ThreadParam_t t = *(ThreadParam_t *)lparam;
    ICMPResponse_t icmp;
    WCHAR error[256];
    DWORD length = 256;

    int r = Ping(t.address,t.buffer,&icmp,t.seconds);
    
    if (r != 0)
        Wstrerror(r);
    
    if (t.verbose == 1){
        if (icmp.status != 0){
            DWORD ret = GetIpErrorString(icmp.status,error,&length);

            if (ret != NO_ERROR){
                Wstrerror(ret);
            }

            printf("%s : response from %s  bytes=%d time=%ld ms %ls\n",t.address,icmp.addr,icmp.data_size,icmp.round_trip_time,error);       
        } else {
            printf("%s : response from %s  bytes=%d time=%ld ms Response good.\n",t.address,icmp.addr,icmp.data_size,icmp.round_trip_time);
        }
    } else {
        if (icmp.status == 0){
            printf("%s : response from %s  bytes=%d time=%ld ms Response good.\n",t.address,icmp.addr,icmp.data_size,icmp.round_trip_time);
        }
    }

    return (0);
}

int main(int argc,char **argv)
{
    char address[17];
    char tmp[4] = {0};
    char buffer[32] = {0};
    int i = 0;

    if (argc < 2){
        printf("usage : %s -h",argv[0]);
        printf("        %s -s <address> <buffer> <timeout in seconds> <verbose>\n",argv[0]);
        printf("        %s -s 192.168.1. hello 1000 1\n",argv[0]);
        exit(-1);
    }

    if (strcmp(argv[1],"-s") == 0 && argc == 6){
        
        strncpy(buffer,argv[3],31);
        WCHAR error[WSA_ERROR_MESSAGE_SIZE] = {0};
        DWORD ms = to_long(argv[4]);
        int verbose = to_long(argv[5]);

        do{
            sprintf(tmp,"%ld",i);
            sprintf(address,"%s%s",argv[2],tmp);
            ThreadParam_t t = {0};
            strcpy(t.address,address);
            strcpy(t.buffer,buffer);
            t.seconds = ms;
            t.verbose = verbose;

            HANDLE hThread = CreateThread(NULL,0,Thread,(void *)&t,THREAD_PRIORITY_NORMAL,NULL);
            WaitForSingleObject(hThread,INFINITE);
            CloseHandle(hThread);
            i++;
        } while (i <= 255);
    } else {
        printf("usage : %s -h",argv[0]);
        printf("        %s -s <address> <buffer> <timeout in ms> <verbose/1/0> | address in this format exemple : 192.168.1. leave the last byte empty\n",argv[0]);
        exit(-1);
    }

    return (0);
}
