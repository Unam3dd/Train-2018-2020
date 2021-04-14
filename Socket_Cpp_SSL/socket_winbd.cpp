#include "socket_winbd.h"

#pragma comment (lib, "Ws2_32.lib")
#define BUFFER_SIZE_DEFAULT 4096

int connect(SOCKET socks_instance, struct sockaddr_in session)
{
    int c = WSAConnect(socks_instance, (struct sockaddr*) & session, sizeof(session), 0, 0, 0, 0);
    if (c != 0) {
        closesocket(socks_instance);
        WSACleanup();
        return -1;
    }
    return 0;
}
