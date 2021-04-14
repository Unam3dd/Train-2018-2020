#include "wcnet.h"

///////////////////////////////////////////////////////
//               SOCKET FUNCTION                     //
///////////////////////////////////////////////////////

SOCKET Socket(int family,int type,int protocol)
{
    WSADATA wsa;
    SOCKET fd;
    
    if (WSAStartup(MAKEWORD(2,2),&wsa) != 0)
        return ((SOCKET)WSAGetLastError());
    
    return (WSASocketA(family,type,protocol,0,0,0));
}


int Connect(SOCKET fd,const char *host,int port)
{
    struct sockaddr_in s = session(host,port);

    return (WSAConnect(fd,(struct sockaddr *)&s,sizeof(s),0,0,0,0));
}

int ConnectTimeout(SOCKET fd,const char *host,int port,int ms)
{
    struct sockaddr_in s = session(host,port);
    unsigned long mode = SOCKET_NONBLOCKMODE;
    fd_set Write = {0};
    fd_set Err = {0};
    struct timeval time = {0};
    
    time.tv_sec = ms / 1000;
    time.tv_usec = (ms %1000) * 1000;

    FD_ZERO(&Write);
    FD_ZERO(&Err);
    FD_SET(fd,&Write);
    FD_SET(fd,&Err);

    ioctlsocket(fd,FIONBIO,&mode);
    WSAConnect(fd,(SOCKADDR *)&s,sizeof(s),0,0,0,0);

    select(0,NULL,&Write,&Err,&time);

    if (FD_ISSET(fd,&Write)){
        mode = SOCKET_BLOCKMODE;
        ioctlsocket(fd,FIONBIO,&mode);
        return (0);
    }

    return (SOCKET_ERROR);
}


int Bind(SOCKET fd,int port)
{
    struct sockaddr_in s = sessionbind(port);
    return (bind(fd,(SOCKADDR *)&s,sizeof(s)));
}


int Listen(SOCKET fd,int maxcon)
{
    return (listen(fd,maxcon));
}

int Send(SOCKET fd,char *buffer,int flags)
{
    return (send(fd,buffer,strlen(buffer),flags));
}

int SendEx(SOCKET fd,char *buffer,int nbytes,int flags)
{
    return (send(fd,buffer,nbytes,flags));
}

int SendTimeout(SOCKET fd,const char *data,unsigned long ms,int flags)
{
    Sleep(ms);
    return (send(fd,data,strlen(data),flags));
}

int SendTimeoutEx(SOCKET fd,const char *data,unsigned long ms,int nbytes,int flags)
{
    Sleep(ms);
    return (send(fd,data,nbytes,flags));
}

int Recv(SOCKET fd,char *buffer,int nbytes,int flags)
{
    return (recv(fd,buffer,nbytes,flags));
}

int RecvMemset(SOCKET fd,char *buffer,int nbytes,int flags)
{
    memset(buffer,0,sizeof(buffer));
    return (recv(fd,buffer,nbytes,flags));
}

char *RecvEx(SOCKET fd,int nbytes,int *bytes_recv,int flags)
{
    char *output = malloc(sizeof(char) * nbytes+1);

    if (output == NULL)
        return (NULL);
    
    memset(output,0,sizeof(output));
    
    *bytes_recv = recv(fd,output,nbytes,flags);

    if (bytes_recv <= 0){
        return (NULL);
    }
    
    return (output);
}


int RecvTimeout(SOCKET fd,char *buffer,int nbytes,int flags,int ms)
{
    memset(buffer,0,sizeof(buffer));
    Sleep(ms);
    return (Recv(fd,buffer,nbytes,flags));
}


int RecvFrom(SOCKET fd,char *data,int nbytes,int flags,UDPPacket_t *info)
{
    struct sockaddr_in client = {0};
    int client_size = sizeof(client);
    int i = 0;

    i = recvfrom(fd,data,nbytes,flags,(struct sockaddr *)&client,&client_size);

    if (i < 0){
        info->err = i;
        return (SOCKET_ERROR);
    }
    
    info->address = inet_ntoa(client.sin_addr);
    info->port = ntohs(client.sin_port);

    return (i);
}


SOCKET Accept(SOCKET fd)
{
    struct sockaddr_in s = {0};
    int size = sizeof(s);
    return (accept(fd,(SOCKADDR *)&s,&size));
}

SOCKET AcceptClient(SOCKET fd,struct sockaddr_in *clientinfo,int *size_client)
{
    return (accept(fd,(struct sockaddr *)clientinfo,size_client));
}

struct sockaddr_in session(const char *host,int port)
{
    struct sockaddr_in socks = {0};

    socks.sin_addr.s_addr = inet_addr(host);
    socks.sin_port = htons(port);
    socks.sin_family = AF_INET;

    return (socks);
}

struct sockaddr_in sessionbind(int port)
{
    struct sockaddr_in socks = {0};
    socks.sin_addr.s_addr = htonl(INADDR_ANY);
    socks.sin_port = htons(port);
    socks.sin_family = AF_INET;

    return (socks);
}

void RecvEx_free(char *buffer)
{
    free(buffer);
}


int SendTo(SOCKET fd,char *data,int len_data,const char *host,int port,int flags)
{
    struct sockaddr_in s = session(host,port);
    return (sendto(fd,data,len_data,flags,(const struct sockaddr *)&s,sizeof(s)));
}


peer_t GetPeerName(SOCKET fd)
{
    SOCKADDR_IN peer = {0};
    peer_t p;
    socklen_t sizepeer = sizeof(peer);
    
    if (getpeername(fd,(SOCKADDR *)&peer,&sizepeer) < 0){
        p.err_code = WSAGetLastError();
        return (p);
    }

    p.addr = inet_ntoa(peer.sin_addr);
    p.port = ntohs(peer.sin_port);

    return (p);
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

void WSAstrerror(int errorcode)
{
    char buffer[WSA_ERROR_MESSAGE_SIZE] = {0};
    FormatMessageA(FORMAT_MESSAGE_FROM_SYSTEM | FORMAT_MESSAGE_IGNORE_INSERTS,NULL,errorcode,MAKELANGID(LANG_NEUTRAL,SUBLANG_DEFAULT),buffer,WSA_ERROR_MESSAGE_SIZE,NULL);
    fprintf(stderr,"[-] Error %d : %s\n",errorcode,buffer);
}


int Getservicebyport(int port,char *buffer)
{
    struct servent *s = getservbyport(ntohs(port),NULL);

    if (s == NULL)
        return (SOCKET_ERROR);

    strncpy(buffer,s->s_name,SERVICE_MAX_CHAR_SIZE);

    return (0);
}

int Getservicebyname(char *name,char *proto)
{
    struct servent *s = getservbyname(name,proto);

    if (!s)
        return (SOCKET_ERROR);

    return (ntohs(s->s_port));
}

int WINSOCK_INITIALIZE(void)
{
    WSADATA wsa;
    
    if (WSAStartup(MAKEWORD(2,2),&wsa) != 0)
        return (INVALID_SOCKET);
    
    return (0);
}

int WINSOCK_CLEANUP(void)
{
    return (WSACleanup());
}

char **Gethostbyname(char *name,int *len_address)
{
    int i = 0, naddress = 0,shift = 0;
    struct in_addr addr = {0};
    struct hostent *h = gethostbyname(name);
    const int size_addr = h->h_length;

    while ((size_addr>>shift) >= 4){
        naddress++;
        shift++;
    }

    *len_address = naddress;

    char **addr_list = malloc(sizeof(char *) * naddress+1);

    if (addr_list == NULL)
        return (ERROR_ALLOCATE_MEMORY);

    while (h->h_addr_list[i] != 0){
        addr.s_addr = *(u_long *) h->h_addr_list[i];
        addr_list[i] = malloc(sizeof(char) * 16);
        
        if (!addr_list[i])
            return (ERROR_ALLOCATE_MEMORY);

        strncpy(addr_list[i],inet_ntoa(addr),16);
        
        i++;
    }

    addr_list[i] = malloc(1);

    if (!addr_list[i])
        return (ERROR_ALLOCATE_MEMORY);
    
    addr_list[i] = NULL;

    return (addr_list);
}


void free_addr_list(char **addr_list)
{
    int i = 0;
    
    for (i;addr_list[i] != NULL;i++)
    {
        free(addr_list[i]);
    }

    free(addr_list[i]);
    free(addr_list);
}


int setblocking(SOCKET fd,BOOL value)
{
    if (value == TRUE){
        unsigned long mode = SOCKET_NONBLOCKMODE;
        return (ioctlsocket(fd,FIONBIO,&mode));
    } else {
        unsigned long mode = SOCKET_BLOCKMODE;
        return (ioctlsocket(fd,FIONBIO,&mode));
    }
}


int Getsockname(SOCKET fd,sockname_t *sockname)
{
    struct sockaddr_in client = {0};
    int client_size = sizeof(client);

    if (getsockname(fd,(struct sockaddr *)&client,&client_size) == SOCKET_ERROR)
        return (SOCKET_ERROR);    

    sockname->address = inet_ntoa(client.sin_addr);
    sockname->port = ntohs(client.sin_port);

    return (0);
}


int Getnameinfo(const char *addr,int port,char *hostname,char *serviceinfo)
{
    struct sockaddr_in client = {0};
    client.sin_addr.s_addr = inet_addr(addr);
    client.sin_port = htons(port);
    client.sin_family = AF_INET;

    if (getnameinfo((struct sockaddr *)&client,sizeof(struct sockaddr),hostname,NI_MAXHOST,serviceinfo,NI_MAXSERV,NI_NUMERICSERV) != 0)
        return (SOCKET_ERROR);
    
    return (0);
}


int Gethostbyaddr(const char *host,hostinfo_t *hi)
{
    struct in_addr s = {0};
    struct in_addr addr = {0};
    struct hostent *h = {0};
    int shift = 0, total_address = 0,i = 0;

    s.s_addr = inet_addr(host);
    h = gethostbyaddr((char *)&s,16,AF_INET);

    int naddress = h->h_length;

    while ((naddress>>shift) >= 4)
    {
        shift++;
        total_address++;
    }

    hi->addr_list = malloc(sizeof(char *) * total_address);

    if (!hi->addr_list)
        return (-1);

    while (h->h_addr_list[i] != 0)
    {
        addr.s_addr = *(u_long *) h->h_addr_list[i];
        
        hi->addr_list[i] = (char *)malloc(sizeof(char) * 16);
        
        if (!hi->addr_list[i])
            return (-1);
        
        strncpy(hi->addr_list[i],inet_ntoa(addr),16);

        i++;
    }

    hi->addr_list[i] = malloc(1);

    if (!hi->addr_list[i])
        return (-1);
    
    hi->addr_list[i] = NULL;

    hi->name = malloc(strlen(h->h_name)+1);

    if (!hi->name)
        return (-1);
    
    strncpy(hi->name,h->h_name,strlen(h->h_name));
    
    return (0);
}

void GethostbyaddrFree(hostinfo_t *hi)
{
    int i = 0;
    for (i;hi->addr_list[i] != NULL;i++)
    {
        free(hi->addr_list[i]);
    }

    free(hi->addr_list[i]);
    free(hi->name);
}


void PortScan(PortScan_t *target)
{
    WSADATA wsa;
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

    printf("[+] Target IP     : %s\n",target->ip);
    printf("[+] RangePort     : %d-%d\n",target->startport,target->maxport);
    printf("[+] Timeout (ms)  : %d\n",target->timeoutms);
    printf("[+] Verbosity     : %d\n",target->verbosity);
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

void to_network_little_endian(const char *addr,char *output)
{
    snprintf(output,MAX_SIZE_ADDRESS,"%#x",inet_addr(addr));
}

int Ping(char *addr,char *buffer,ICMPResponse_t *icmp)
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

    dwReturnValue = IcmpSendEcho(hIcmp,ip,data,sizeof(data),NULL,ReplyBuffer,dwReplySize,1000);

    if (dwReturnValue == 0)
        return (GetLastError());
    
    PICMP_ECHO_REPLY IcmpReply = (PICMP_ECHO_REPLY)ReplyBuffer;
    raddr.S_un.S_addr = IcmpReply->Address;
    strncpy(icmp->addr,inet_ntoa(raddr),sizeof(icmp->addr));
    icmp->status = IcmpReply->Status;
    
    icmp->data = IcmpReply->Data;

    if (icmp->data == NULL)
        return (-1);

    icmp->data_size = IcmpReply->DataSize;
    
    icmp->reserved = IcmpReply->Reserved;
    icmp->round_trip_time = IcmpReply->RoundTripTime;
    

    IcmpCloseHandle(hIcmp);
    return (0);
}


int SendFile(SOCKET fd,const char *filename)
{
    HANDLE file = CreateFileA(filename,GENERIC_READ,0,NULL,OPEN_EXISTING,FILE_ATTRIBUTE_NORMAL | FILE_FLAG_SEQUENTIAL_SCAN,NULL);

    if (file == INVALID_HANDLE_VALUE)
        return (GetLastError());
    
    if (TransmitFile(fd,file,0,0,NULL,NULL,TF_DISCONNECT | TF_REUSE_SOCKET) != TRUE)
        return (WSAGetLastError());
    
    CloseHandle(file);
    
    return (0);
}


int SendFileBinary(SOCKET fd,const char *filename)
{
    FILE *fp = NULL;
    int i;
    char *buffer = NULL;
    char size[100] = {0};
    char base64_size[100] = {0};

    fp = fopen(filename,"rb");

    if (!fp)
        return (3);
    
    fseek(fp,0,SEEK_END);
    size_t size_bytes = ftell(fp);
    fseek(fp,0,SEEK_SET);

    buffer = (char *)malloc(sizeof(char) * size_bytes+1);

    if (!buffer)
        return (-1);
    
    fread(buffer,sizeof(char),size_bytes,fp);
    
    unsigned char *encoded = base64_encode((unsigned char *)buffer,size_bytes);

    sprintf(size,"%zd",size_bytes);
    sprintf(base64_size,"%zd",strlen(encoded));

    if (send(fd,filename,255,0) < 0)
        return (WSAGetLastError());

    if (send(fd,size,100,0) < 0)
        return (WSAGetLastError());
    
    if (send(fd,base64_size,100,0) < 0)
        return (WSAGetLastError());

    if (send(fd,encoded,strlen(encoded),0) < 0)
        return (WSAGetLastError());

    free(buffer);
    free(encoded);
    fclose(fp);

    return (0);
}

unsigned char *base64_encode(unsigned char *input,int len)
{
    int pad_len = (((len+2) / 3) * 4);
    unsigned char *output = (unsigned char *)calloc(pad_len+1,sizeof(unsigned char));

    if (output == NULL)
        return (NULL);

    int nbytes = EVP_EncodeBlock(output,input,len);

    if (nbytes > pad_len){
        fprintf(stderr,"[-] Error : not enough space in the buffer !\n");
        free(output);
        return (NULL);
    }

    return (output);
}

unsigned char *base64_decode(unsigned char *input,int len)
{
    int pad_len = (len*3)/4;
    unsigned char *output = (unsigned char *)calloc(pad_len,sizeof(unsigned char));

    if (output == NULL)
        return (NULL);
    
    int nbytes = EVP_DecodeBlock(output,input,len);

    if (nbytes > pad_len){
        fprintf(stderr,"[-] Error : not enough space in the buffer !\n");
        free(output);
        return (NULL);
    }

    return (output);
}

long to_long(char* number)
{
    long tolong = 0;

    for (int i = 0; number[i] >= '0' && number[i] <= '9'; i++)
    {
        tolong *= 10;
        tolong += number[i]++ & 0xF;
    }

    return (tolong);
}


void *ThreadStreamInSocket(void *param)
{
    StreamInSocket_t s = *(StreamInSocket_t *)param;
    int bytes = 0;
    char buffer[MAX_BUFFER_SIZE] = {0};

    while ((bytes = read(s.in,buffer,(MAX_BUFFER_SIZE - 1)))){
        if (send(s.out,buffer,bytes,0) < 0){
            fprintf(stderr,"[-] Error send data in socket !\n[-] client probaly closed the connection\n");
            break;
        }
    }

    if (bytes < 0)
        fprintf(stderr,"[-] Error reading STDIN (0)\n");

    return (NULL);
}

int InteractWithFd(SOCKET fd)
{
    pthread_t thread;
    StreamInSocket_t s = {0};
    unsigned long nonblock = -1;
    char buffer[MAX_BUFFER_SIZE] = {0};
    ioctlsocket(fd,FIONBIO,&nonblock);
    int bytes = 0;
    s.in = STDIN_FILENO;
    s.out = fd;

    if (pthread_create(&thread,NULL,ThreadStreamInSocket,(void *)&s) != 0){
        return (-1);
    }

    for (;;){
        while ((bytes = recv(fd,buffer,(MAX_BUFFER_SIZE - 1),0)) > 0)
        {
            if (write(STDOUT_FILENO,buffer,bytes) < 0)
            {
                fprintf(stderr,"[-] Error write stream in output !\n");
                return (-2);
            }
        }
    }

    pthread_cancel(thread);
    pthread_join(thread,NULL);

    return (0);
}