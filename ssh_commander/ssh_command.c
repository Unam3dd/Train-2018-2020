#include <libssh/libssh.h>
#include <stdlib.h>
#include <stdio.h>
#include <netdb.h>
#include <string.h>
#include <sys/types.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <sys/socket.h>

#define BUFFER_SIZE 4096

void free_channel(ssh_channel channel)
{
    ssh_channel_send_eof(channel);
    ssh_channel_close(channel);
    ssh_channel_free(channel);
}

void free_session(ssh_session session)
{
    ssh_disconnect(session);
    ssh_free(session);
}

void get_version(char *target_ip){
    struct sockaddr_in so_variable;
    struct hostent *host_variable;
    struct in_addr *addr_variable;
    int error_socket, socks;
    strncpy((char*)&so_variable, "", sizeof(so_variable));
    so_variable.sin_family = AF_INET;

    so_variable.sin_addr.s_addr = inet_addr(target_ip);
    so_variable.sin_port = htons(22);
    socks = socket(AF_INET, SOCK_STREAM, 0);

    if(socks < 0){
        exit(-1);
    }

    error_socket = connect(socks, (struct sockaddr*)&so_variable, sizeof(so_variable));

    if(error_socket < 0){
        fflush(stdout);
    }

    int data_recv;
    char buffer[BUFFER_SIZE];
    data_recv = recv(socks,buffer,sizeof buffer - 1, 0);
    if(data_recv < 0){
        perror("[*] Error Recv Data !\n");
    }
    buffer[data_recv] = 0;
    char *p = strstr(buffer,"\r\n");
    if (p != NULL){
        *p = 0;
        printf("\033[32m[\033[34m+\033[32m] Version SSH : %s\n", buffer);
    }
}

void error(ssh_session session)
{
    fprintf(stderr, "\033[31m[!] Error: %s\n\033[00m", ssh_get_error(session));
    free_session(session);
    exit(-1);
}

void ssh_connect_main(char *ip,char *username,char *password,char *command){
    ssh_session session;
    ssh_channel channel;
    int ssh_s, port = 22;
    char buffer[BUFFER_SIZE];
    unsigned int bytes;

    session = ssh_new();
    if (session == NULL) exit(-1);

    ssh_options_set(session, SSH_OPTIONS_HOST, ip);
    ssh_options_set(session, SSH_OPTIONS_PORT, &port);
    ssh_options_set(session, SSH_OPTIONS_USER, username);

    printf("\033[32m[\033[34m+\033[32m] Connecting... to %s:22\n",ip);
    ssh_s = ssh_connect(session);
    if (ssh_s != SSH_OK) error(session);

    printf("\033[32m[\033[34m+\033[32m] Try Password...\n");
    ssh_s = ssh_userauth_password(session, NULL, password);
    if (ssh_s != SSH_AUTH_SUCCESS) error(session);

    printf("\033[32m[\033[34m+\033[32m] Connected To %s:22\n",ip);
    channel = ssh_channel_new(session);
    if (channel == NULL) exit(-1);

    ssh_s = ssh_channel_open_session(channel);
    if (ssh_s != SSH_OK) error(session);

    printf("\033[32m[\033[34m+\033[32m] Executing remote command...\n");
    ssh_s = ssh_channel_request_exec(channel, command);
    if (ssh_s != SSH_OK) error(session);

    printf("\033[32m[\033[34m+\033[32m] Received Output :\n\n");
    bytes = ssh_channel_read(channel, buffer, sizeof(buffer), 0);
    fwrite(buffer, 1, bytes, stdout);
    bytes = ssh_channel_read(channel, buffer, sizeof(buffer), 0);

    free_channel(channel);
    free_session(session);
}

int main(int argc,char *argv[]){
    if(argc<5){
        printf("    Created By \033[31mUnam3dd\033[00m\nusage : %s <hostname> <username> <password> <command>\n",argv[0]);
    } else {
        get_version(argv[1]);
        ssh_connect_main(argv[1],argv[2],argv[3],argv[4]);
        return 0;
    }
}