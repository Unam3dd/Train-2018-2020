#include "http_server.h"


int http_server_initialize(http_server_info_t *sinfo)
{
    struct sockaddr_in socks = {0};
    WSADATA wsa;

    socks.sin_addr.s_addr = htonl(INADDR_ANY);
    socks.sin_family = AF_INET;

    if (WSAStartup(MAKEWORD(2,2),&wsa) != 0)
        return (WSAGetLastError());
    

    sinfo->fdserver = WSASocketA(AF_INET,SOCK_STREAM,IPPROTO_TCP,0,0,0);

    if (sinfo->fdserver == INVALID_SOCKET)
        return (WSAGetLastError());
    
    if (sinfo->port == 0)
        sinfo->port = HTTP_SERVER_PORT;

    socks.sin_port = htons(sinfo->port);
    
    if (bind(sinfo->fdserver,(struct sockaddr *)&socks,sizeof(socks)) < 0)
        return (WSAGetLastError());

    return (0);
}


int http_get_peer_client(SOCKET fd,http_client_peer_t *peer)
{
    struct sockaddr_in sockspeer = {0};
    int size_sockspeer = sizeof(sockspeer);

    if (getpeername(fd,(struct sockaddr *)&sockspeer,&size_sockspeer) < 0)
        return (WSAGetLastError());
    
    peer->address = inet_ntoa(sockspeer.sin_addr);
    peer->port = ntohs(sockspeer.sin_port);
    
    return (0);
}

int http_server_listen(http_server_info_t *sinfo)
{
    if (listen(sinfo->fdserver,SOMAXCONN) < 0)
        return (WSAGetLastError());
    
    int rp = 0;
    struct sockaddr_in client = {0};
    http_client_peer_t peer = {0};
    int client_size = sizeof(client);

    printf("[+] HTTP Server started listening on %d\n",sinfo->port);
    
    while (1){
        SOCKET cfd = accept(sinfo->fdserver,(struct sockaddr *)&client,&client_size);
        
        if ((rp = http_get_peer_client(cfd,&peer)) != 0)
            http_catch_error(rp);
        
        printf("[+] Client connected -> %s:%d\n",peer.address,peer.port);
        closesocket(cfd);
        printf("[+] Client disconnected -> %s:%d\n",peer.address,peer.port);
        
        memset(&client,0,sizeof(client));
        memset(&peer,0,sizeof(peer));
    }

    return (0);
}

void http_catch_error(int errorcode)
{
    char buffer[255] = {0};
    FormatMessageA(FORMAT_MESSAGE_FROM_SYSTEM | FORMAT_MESSAGE_IGNORE_INSERTS,NULL,errorcode,MAKELANGID(LANG_NEUTRAL,SUBLANG_DEFAULT),buffer,255,NULL);
    fprintf(stderr,"[-] Error %d : %s\n",errorcode,buffer);
}