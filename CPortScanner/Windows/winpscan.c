#include "winpscan.h"

void PortScan(struct Target *target)
{
    struct WSAData wsa;
    struct sockaddr_in s;
    struct timeval t;
    struct servent *sv = {0};
    int i;
    unsigned long mode = 1;
    fd_set Write, Err;
    SOCKET fd;

    memset(&s,0,sizeof(s));
    memset(&t,0,sizeof(t));
    memset(&Write,0,sizeof(Write));
    memset(&Err,0,sizeof(Err));

    WSAStartup(MAKEWORD(2,2),&wsa);
    
    s.sin_addr.s_addr = inet_addr(target->ip);
    s.sin_family = AF_INET;

    t.tv_sec = target->timeoutms / 1000;
    t.tv_usec = (target->timeoutms %1000) * 1000;

    printf("\033[38;5;82m[\033[1;96m+\033[38;5;82m] Target IP     : \033[1;93m%s\033[00m\n",target->ip);
    printf("\033[38;5;82m[\033[1;96m+\033[38;5;82m] RangePort     : \033[1;93m%d-%d\033[00m\n",target->startport,target->maxport);
    printf("\033[38;5;82m[\033[1;96m+\033[38;5;82m] Timeout (ms)  : \033[1;93m%d\033[00m\n",target->timeoutms);
    printf("\033[38;5;82m[\033[1;96m+\033[38;5;82m] Verbosity     : \033[1;93m%d\033[00m\n",target->verbosity);
    printf("PORT\tSTATE\tSERVICE\n");

    for (i = target->startport;i<=target->maxport;i++){
        s.sin_port = htons(i);
        sv = getservbyport(ntohs(i),NULL);
        fd = WSASocketA(AF_INET,SOCK_STREAM,IPPROTO_TCP,0,0,0);
        ioctlsocket(fd,FIONBIO,&mode);
        WSAConnect(fd,(struct sockaddr *)&s,sizeof(s),0,0,0,0);
        FD_ZERO(&Write);
        FD_ZERO(&Err);
        FD_SET(fd,&Write);
        FD_SET(fd,&Err);
    
        select(0,NULL,&Write,&Err,&t);
        
        if (target->verbosity) {
            if (FD_ISSET(fd,&Write))
                printf("%d\topen\t%s\n",i,sv->s_name);
            else
                printf("%d\tclosed\n",i);
        } else
            if (FD_ISSET(fd,&Write))
                printf("%d\topen\t%s\n",i,sv->s_name);
        

        memset(&s.sin_port,0,sizeof(s.sin_port));
        memset(&Write,0,sizeof(Write));
        memset(&sv,0,sizeof(sv));
        memset(&Err,0,sizeof(Err));
        closesocket(fd);
    }
}

void show_banner()
{
    puts(BANNER);
    printf("\033[38;5;82m\t     Author : %s\n\t\033[38;5;82m   Version : %s\n\t\033[38;5;82m   Github : %s \n%s\n\n\n\033[00m",AUTHOR,VERSION,GITHUB,TOOLS_BANNER);
}