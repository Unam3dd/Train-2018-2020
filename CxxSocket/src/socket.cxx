#include "../headers/socket.hxx"

using namespace std;

#ifdef _WIN32
    // Constructor
    WinSocket::WinSocket(short Family, int Type,int Protocol)
    {
        this->WinSocket::Family = Family;
        this->WinSocket::Type = Type;
        this->WinSocket::Protocol = Protocol;
        SOCKET socks = InitSocket();
        this->WinSocket::sobject = socks;
    }

    // Public Methods

    int WinSocket::Connect(string host, int port)
    {
        this->WinSocket::host = host;
        this->WinSocket::port = port;
        sockaddr_in config = session();

        if (WSAConnect(WinSocket::sobject,(struct sockaddr*)&config,sizeof(config),0,0,0,0) != 0){
            closesocket(WinSocket::sobject);
            WSACleanup();
            return (-1);
        }

        return (0);
    }

    int WinSocket::ConnectTimeout(string host,int port,int ms)
    {
        this->WinSocket::host = host;
        this->WinSocket::port = port;
        sockaddr_in ss = session();

        unsigned long mode = -1;

        memset(&Write,0,sizeof(Write));
        memset(&Err,0,sizeof(Err));
        memset(&t,0,sizeof(t));

        t.tv_sec = ms / 1000;
        t.tv_usec = (ms %1000) * 1000;

        ioctlsocket(WinSocket::sobject,FIONBIO,&mode);
        WSAConnect(WinSocket::sobject,(struct sockaddr *)&ss,sizeof(ss),0,0,0,0);
        FD_ZERO(&Write);
        FD_ZERO(&Err);
        FD_SET(WinSocket::sobject,&Write);
        FD_SET(WinSocket::sobject,&Err);

        select(0,NULL,&Write,&Err,&t);

        if (FD_ISSET(WinSocket::sobject,&Write)){
            mode = 0;
            ioctlsocket(WinSocket::sobject,FIONBIO,&mode);
            return (0);
        }
        else
            return (SOCKET_ERROR);
    }

    int WinSocket::Bind(int port){
        this->WinSocket::port = port;
        sockaddr_in config = sessionbind();

        if (bind(WinSocket::sobject,(sockaddr *)&config,sizeof(config)) == SOCKET_ERROR)
        {
            return (-1); // Failed
        }
        return (0); // Success
    }

    int WinSocket::Listen(int maxcon) {
        
        if (listen(WinSocket::sobject,maxcon) == SOCKET_ERROR){
            return (-1);
        }

        return (0);
    }

    SOCKET WinSocket::Accept()
    {
        SOCKET csock;
        SOCKADDR_IN csin = {0};
        int sinsize = sizeof(csin);
        csock = accept(WinSocket::sobject,(sockaddr *)&csin,&sinsize);

        if (csock == INVALID_SOCKET)
        {
            return (-1);
        }

        return (csock);
    }

    int WinSocket::Send(string data,int flags)
    {
        //Sleep(100);
        int s = send(WinSocket::sobject,data.c_str(),strlen(data.c_str()),flags);

        if (s == SOCKET_ERROR)
            fprintf(stderr,"[-] Error : [Error %ld]\n",WSAGetLastError());
            return (SOCKET_ERROR);
        
        return (s);
    }

    int WinSocket::SendTimeout(string data,unsigned long ms,int flags)
    {
        Sleep(ms);
        int s = send(WinSocket::sobject,data.c_str(),strlen(data.c_str()),flags);

        if (s == SOCKET_ERROR)
            fprintf(stderr,"[-] Error : [Error %ld]\n",WSAGetLastError());
            return (SOCKET_ERROR);
        
        return (s);
    }

    int WinSocket::CSend(SOCKET fd,string data,int flags){
        int s = send(fd,data.c_str(),strlen(data.c_str()),flags);

        if (s == SOCKET_ERROR){
            fprintf(stderr,"[-] Error : [Error %ld]\n",WSAGetLastError());
            return (SOCKET_ERROR);
        }

        return (s);
    }

    int WinSocket::CSendTimeout(SOCKET fd,string data,unsigned long ms,int flags){
        Sleep(ms);

        int s = send(fd,data.c_str(),strlen(data.c_str()),flags);

        if (s == SOCKET_ERROR){
            fprintf(stderr,"[-] Error : [Error %ld]\n",WSAGetLastError());
            return (SOCKET_ERROR);
        }

        return (s);
    }

    string WinSocket::RecvData(int bytes,int flags){
        char buffer[bytes];
        string output;
        memset(buffer,0,sizeof(buffer));

        if (this->rdata(WinSocket::sobject,buffer,(bytes-1),flags) == -1)
        {
            output = "[-] Error : recv failed with error %d\n", WSAGetLastError();
        } else {
            output = buffer;
        }

        return (output);
    }

    string WinSocket::RecvDataTimeout(int bytes,int flags,unsigned long ms){
        char buffer[bytes];
        string output;
        memset(buffer,0,sizeof(buffer));

        if (this->rdatat(WinSocket::sobject,buffer,(bytes-1),flags,ms) == SOCKET_ERROR)
        {
            output = "[-] Error : recv failed with error %d\n", WSAGetLastError();
        } else {
            output = buffer;
        }

        return (output);
    }


    string WinSocket::CRecvData(SOCKET fd,int bytes,int flags){
        char buffer[bytes];
        string output;
        memset(buffer,0,sizeof(buffer));

        if (this->rdata(fd,buffer,(bytes-1),flags) == SOCKET_ERROR)
        {
            output = "[-] Error : recv failed with error %d\n", WSAGetLastError();
        } else {
            output = buffer;
        }

        return (output);
    }

    string WinSocket::CRecvDataTimeout(SOCKET fd,int bytes,int flags,unsigned long ms){
        char buffer[bytes];
        string output;
        memset(buffer,0,sizeof(buffer));

        if (this->rdatat(fd,buffer,(bytes-1),flags,ms) == SOCKET_ERROR)
        {
            output = "[-] Error : recv failed with error %d\n",WSAGetLastError();
        } else {
            output = buffer;
        }

        return (output);
    }


    void WinSocket::ExecuteAndStreamProcess(string process){
        STARTUPINFO s;
        memset(&s,0,sizeof(s));
        PROCESS_INFORMATION p;
        memset(&p,0,sizeof(p));
        s.cb = sizeof(s);
        s.dwFlags = (STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW);
        s.hStdError = (HANDLE)WinSocket::sobject;
        s.hStdInput = (HANDLE)WinSocket::sobject;
        s.hStdOutput = (HANDLE)WinSocket::sobject;
        CreateProcessA(NULL,(LPSTR)process.c_str(),NULL,NULL,TRUE,0,NULL,NULL,(LPSTARTUPINFOA)&s,&p);
        WaitForSingleObject(p.hProcess,INFINITE);
        CloseHandle(p.hProcess);
        CloseHandle(p.hThread);
    }

    void WinSocket::CExecuteAndStreamProcess(SOCKET fd,string process){
        STARTUPINFO s;
        PROCESS_INFORMATION p;

        memset(&s,0,sizeof(s));
        memset(&p,0,sizeof(p));

        s.cb = sizeof(s);
        s.dwFlags = (STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW);
        s.hStdError = s.hStdInput = s.hStdOutput = (HANDLE)fd;
        CreateProcessA(NULL,(LPSTR)process.c_str(),NULL,NULL,TRUE,0,NULL,NULL,(LPSTARTUPINFOA)&s,&p);
        WaitForSingleObject(p.hProcess,INFINITE);
        CloseHandle(p.hProcess);
        CloseHandle(p.hThread);
    }

    peer_t WinSocket::GetPeerName(SOCKET ns)
    {
        sockaddr_in peer {};
        socklen_t sizepeer = sizeof(peer);
        getpeername(ns,(sockaddr*)&peer,&sizepeer);
        char *address = inet_ntoa(peer.sin_addr);
        u_short peerport = ntohs(peer.sin_port);
        peer_t p;
        p.address = inet_ntoa(peer.sin_addr);
        p.port = ntohs(peer.sin_port);
        return (p);
    }

    int WinSocket::Close()
    {
        return (closesocket(WinSocket::sobject));
    }

    int WinSocket::CClose(SOCKET fd){
        return (closesocket(fd));
    }

    // Private Methods

    SOCKET WinSocket::InitSocket() {
        WSADATA wsa;
        WSAStartup(MAKEWORD(2,2),&wsa);
        SOCKET s = WSASocketA(WinSocket::Family,WinSocket::Type,WinSocket::Protocol,0,0,0);
        return (s);
    }

    sockaddr_in WinSocket::session() {
        struct sockaddr_in s;
        s.sin_family = WinSocket::Family;
        s.sin_addr.s_addr = inet_addr(WinSocket::host.c_str());
        s.sin_port = htons(WinSocket::port);
        return (s);
    }

    sockaddr_in WinSocket::sessionbind() {
        struct sockaddr_in s;
        s.sin_family = WinSocket::Family;
        s.sin_addr.s_addr = htonl(INADDR_ANY);
        s.sin_port = htons(WinSocket::port);
        return (s);
    }

    int WinSocket::rdata(SOCKET s, char* buffer, int len,int flags)
    {
        int i;
        i = recv(s, buffer, len, flags);
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

    int WinSocket::rdatat(SOCKET s, char* buffer, int len,int flags,unsigned long ms)
    {
        Sleep(ms);
        int i;
        i = recv(s, buffer, len, flags);
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

#elif __unix__
    // Constructor

    LinSocket::LinSocket(int Family,int Type,int Protocol)
    {
        this->LinSocket::Family = Family;
        this->LinSocket::Type = Type;
        this->LinSocket::Protocol = Protocol;
        SOCKET socks = InitSocket();
        this->LinSocket::sobject = socks;
    }

    // Public

    int LinSocket::Connect(string host,int port){
        this->LinSocket::host = host;
        this->LinSocket::port = port;
        sockaddr_in config = LinSocket::session();

        if (connect(LinSocket::sobject,(struct sockaddr*)&config,sizeof(config)) != 0){
            closesocket(LinSocket::sobject);
            return (SOCKET_ERROR);
        }
        return (0);
    }

    int LinSocket::ConnectTimeout(string host,int port,int ms)
    {
        this->LinSocket::host = host;
        this->LinSocket::port = port;
        sockaddr_in ss = LinSocket::session();

        memset(&t,0,sizeof(t));
        t.tv_sec = ms / 1000;
        t.tv_usec = (ms %1000) * 1000;
        setsockopt(this->LinSocket::sobject,SOL_SOCKET,SO_SNDTIMEO,&t,sizeof(t));
        return (connect(this->LinSocket::sobject,(sockaddr *)&ss,sizeof(ss)));
    }

    int LinSocket::Bind(int port){
        this->LinSocket::port = port;
        sockaddr_in config = sessionbind();

        if (bind(LinSocket::sobject,(sockaddr *)&config,sizeof(config)) == SOCKET_ERROR)
        {
            return (-1); // Failed
        }
        return (0); // Success
    }

    int LinSocket::Listen(int maxcon) {
        
        if (listen(LinSocket::sobject,maxcon) == SOCKET_ERROR){
            return (-1);
        }

        return (0);
    }

    SOCKET LinSocket::Accept()
    {
        SOCKET csock;
        SOCKADDR_IN csin = {0};
        socklen_t sinsize = sizeof(csin);
        csock = accept(LinSocket::sobject,(sockaddr *)&csin,&sinsize);

        if (csock == INVALID_SOCKET)
        {
            return (-1);
        }

        return (csock);
    }

    int LinSocket::Send(string data,int flags)
    {
        //Sleep(100);
        int s = send(LinSocket::sobject,data.c_str(),strlen(data.c_str()),flags);

        if (s == SOCKET_ERROR)
            return (SOCKET_ERROR);
        
        return (s);
    }

    int LinSocket::SendTimeout(string data,int seconds,int flags)
    {
        sleep(seconds);
        int s = send(LinSocket::sobject,data.c_str(),strlen(data.c_str()),flags);

        if (s == SOCKET_ERROR)
            return (SOCKET_ERROR);
        
        return (s);
    }

    int LinSocket::CSend(SOCKET fd,string data,int flags)
    {
        //Sleep(100);
        int s = send(fd,data.c_str(),strlen(data.c_str()),flags);

        if (s == SOCKET_ERROR)
            return (SOCKET_ERROR);
        
        return (s);
    }

    int LinSocket::CSendTimeout(SOCKET fd,string data,int seconds,int flags)
    {
        sleep(seconds);
        int s = send(LinSocket::sobject,data.c_str(),strlen(data.c_str()),flags);

        if (s == SOCKET_ERROR)
            return (SOCKET_ERROR);
        
        return (s);
    }

    string LinSocket::RecvData(int bytes,int flags){
        char buffer[bytes];
        string output;
        memset(buffer,0,sizeof(buffer));

        if (this->rdata(LinSocket::sobject,buffer,(bytes-1),flags) == SOCKET_ERROR)
        {
            output = "[-] Error : recv failed\n";
        } else {
            output = buffer;
        }

        return (output);
    }

    string LinSocket::RecvDataTimeout(int bytes,int flags,int seconds){
        char buffer[bytes];
        string output;
        memset(buffer,0,sizeof(buffer));

        if (this->rdatat(LinSocket::sobject,buffer,(bytes-1),flags,seconds) == SOCKET_ERROR)
        {
            output = "[-] Error : recv failed\n";
        } else {
            output = buffer;
        }

        return (output);
    }

    string LinSocket::CRecvData(SOCKET fd,int bytes,int flags){
        char buffer[bytes];
        string output;
        memset(buffer,0,sizeof(buffer));

        if (this->rdata(fd,buffer,(bytes-1),flags) == SOCKET_ERROR)
        {
            output = "[-] Error : recv failed\n";
        } else {
            output = buffer;
        }

        return (output);
    }

    string LinSocket::CRecvDataTimeout(SOCKET fd,int bytes,int flags,int seconds){
        char buffer[bytes];
        string output;
        memset(buffer,0,sizeof(buffer));

        if (this->rdatat(LinSocket::sobject,buffer,(bytes-1),flags,seconds) == SOCKET_ERROR)
        {
            output = "[-] Error : recv failed\n";
        } else {
            output = buffer;
        }

        return (output);
    }

    void LinSocket::ExecuteAndStreamProcess(string process){
        dup2(LinSocket::sobject,0);
        dup2(LinSocket::sobject,1);
        dup2(LinSocket::sobject,2);
        execve(process.c_str(),NULL,NULL);
    }

    void LinSocket::CExecuteAndStreamProcess(SOCKET fd,string process){
        dup2(fd,0);
        dup2(fd,1);
        dup2(fd,2);
        execve(process.c_str(),NULL,NULL);
    }

    int LinSocket::Close()
    {
        return (closesocket(LinSocket::sobject));
    }

    int LinSocket::CClose(SOCKET fd){
        return (closesocket(fd));
    }
    

    // Private
    SOCKET LinSocket::InitSocket(){
        return (socket(LinSocket::Family,LinSocket::Type,LinSocket::Protocol));
    }

    sockaddr_in LinSocket::session() {
        struct sockaddr_in s;
        s.sin_family = LinSocket::Family;
        s.sin_addr.s_addr = inet_addr(LinSocket::host.c_str());
        s.sin_port = htons(LinSocket::port);
        return (s);
    }

    sockaddr_in LinSocket::sessionbind() {
        struct sockaddr_in s;
        s.sin_family = LinSocket::Family;
        s.sin_addr.s_addr = htonl(INADDR_ANY);
        s.sin_port = htons(LinSocket::port);
        return (s);
    }

    int LinSocket::rdata(SOCKET s, char* buffer, int len,int flags)
    {
        int i;
        i = recv(s, buffer, len, flags);
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

    int LinSocket::rdatat(SOCKET s, char* buffer, int len,int flags,int seconds)
    {
        sleep(seconds);
        int i;
        i = recv(s, buffer, len, flags);
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


#endif
