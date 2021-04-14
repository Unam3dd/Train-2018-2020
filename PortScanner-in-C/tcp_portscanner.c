// Created By Unamed aka Dxvistxr 0x4eff Dark Pamplemousse- 2019

#include <stdio.h>
#include <sys/socket.h>
#include <errno.h>
#include <netdb.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <arpa/inet.h>

void PortScan(char* target_ip, int max_port){
    struct sockaddr_in so;
    struct hostent *host_ip;
    struct in_addr *address;

    //inet_pton(AF_INET, target_ip, &address);
    printf("\033[1;92m[\033[1;94m*\033[1;92m] IP : %s\n",target_ip);

    int error_socket, x, socks;
    strncpy((char*)&so, "", sizeof so);
    so.sin_family = AF_INET;

    if(isdigit(target_ip[0])){
        so.sin_addr.s_addr = inet_addr(target_ip);
    }
    else if ( (host_ip = gethostbyname(target_ip)) != 0){
        strncpy((char*)&so.sin_addr, (char*) host_ip->h_addr, sizeof so.sin_addr);
    }
    else {
        herror(host_ip);
        printf("\033[1;91m[!] Error : %s Please Enter IP no Domain Name !\033[00m\n", target_ip);
        exit(2);
    }

    for(x=1; x <=max_port; x++){
        so.sin_port = htons(x);
        socks = socket(AF_INET, SOCK_STREAM, 0);

        if(socks < 0){
            exit(1);
        }

        error_socket = connect(socks, (struct sockaddr*)&so, sizeof so);

        if(error_socket < 0){
            fflush(stdout);
        }
        else{
            struct servent *service_variable_struct;
            int buffer_size = sizeof(struct servent);
            service_variable_struct = (struct servent *)malloc(buffer_size);
            bzero(service_variable_struct, buffer_size);
            service_variable_struct = getservbyport(htons(x),NULL);
            if (service_variable_struct == NULL)
            {
                perror("getservbyport()");
            }
            printf("\033[1;96m[\033[1;94m*\033[1;96m] Port \033[1;92m%d/tcp\033[00m open \033[1;96m| Service Name : \033[00m%s\n", x, service_variable_struct->s_name);
            
            if(x==21){
                int data_recv;
                char buffer[10000];
                char dt_recv[10000];
                data_recv = recv(socks, buffer, sizeof buffer - 1, 0);
                if(data_recv < 0)
                {
                    perror("[*] Error Recv Data !\n");
                }
                buffer[data_recv] = 0;
                char *p = strstr (buffer, "\r\n");
                if (p != NULL){
                    *p = 0;
                    printf("\033[1;96m[\033[1;94m*\033[1;96m] Version FTP : \033[1;92m%s\033[00m\n", buffer);
                }
                else{
                    printf("[*] Error Recv Data\n");
                }
            }

            else if(x==22){
                int data_recv;
                char buffer[10000];
                char dt_recv[10000];
                data_recv = recv(socks, buffer, sizeof buffer - 1, 0);
                if(data_recv < 0)
                {
                    perror("[*] Error Recv Data !\n");
                }
                buffer[data_recv] = 0;
                char *p = strstr (buffer, "\r\n");
                if (p != NULL){
                    *p = 0;
                    printf("\033[1;96m[\033[1;94m*\033[1;96m] Version SSH : \033[1;92m%s\033[00m\n", buffer);
                }
                else{
                    printf("[*] Error Recv Data\n");
                }
            }
        }
        close(socks);
    }
    fflush(stdout);
    exit(0);
}

void check_bin_path_cow(char* bin_path){
    if(access( bin_path, F_OK) != -1){
        printf("\033[1;92m[\033[1;94m*\033[1;92m] Cowsay Found !\033[00m\n");
    
    }else{
        printf("\033[1;91m[!] Cowsay Not Found !\033[00m\n");
        system("apt update && apt install cowsay -y");
    }
}

void check_lolcat(char* bin_path){
    if(access( bin_path, F_OK) != -1){
        printf("\033[1;92m[\033[1;94m*\033[1;92m] Lolcat Found !\033[00m\n");
    }else{
        printf("\033[1;91m[!] Lolcat Not Found !\033[00m\n");
        system("apt update && apt install lolcat -y");
    }
}

int main(){
    check_bin_path_cow("/usr/share/cowsay/cows/eyes.cow");
    check_lolcat("/usr/games/lolcat");
    system("clear");
    system("cowsay -f eyes Simple PortScanner By Unamed | lolcat");
    printf("\033[1;96m         ==================================      \033[00m\n");
    printf("\033[1;96m         =    Instagram : \033[1;91m0x4eff\033[1;96m          =      \033[00m\n");
    printf("\033[1;96m         =    Github : \033[1;91mDxvistxr\033[1;96m           =      \033[00m\n");
    printf("\033[1;96m         ==================================      \033[00m\n");
    char target_ip[1000];
    printf("\033[1;92m[\033[1;94m*\033[1;92m] Enter Target IP ~> \033[1;96m");
    fgets(target_ip,1000,stdin);
    int max_port;
    printf("\033[1;92m[\033[1;94m*\033[1;92m] Enter Max Port ~> \033[1;96m ");
    scanf("%d",&max_port);
    printf("\033[1;92m[\033[1;94m*\033[1;92m] Starting Scanner !\n");
    printf("\n");
    PortScan(target_ip,max_port);
}
