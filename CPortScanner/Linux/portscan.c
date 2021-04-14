#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <unistd.h>
#include <ctype.h>
#include <string.h>

#define AUTHOR "\033[1;96munam3dd\033[00m"
#define VERSION "\033[1;96m0.1\033[00m"
#define GITHUB "\033[1;96mhttps://github.com/Unam3dd/\033[00m"
#define BANNER "\033[38;5;82m\t ______ _______                   \n\t|   __ \\     __|.----.---.-.-----.\n\t|    __/__     ||  __|  _  |     |\n\t|___|  |_______||____|___._|__|__|\n\033[00m"
#define TOOLS_BANNER "\t   \033[38;5;82mThis tools made with C programming langage !\n\033[00m"
#define SOCKET_ERROR -1

///////////////////////////
//  Check is connected 
//////////////////////////

int isConnected(int fd, struct sockaddr_in s)
{
    if (connect(fd,(struct sockaddr *)&s,sizeof(s)) != SOCKET_ERROR)
        return (0);
    else
        return (SOCKET_ERROR);
}

///////////////////////////
//  Show banner function 
//////////////////////////

void show_banner()
{
    puts(BANNER);
    printf("\033[38;5;82m\t   Author : %s\n\t\033[38;5;82m   Version : %s\n\t\033[38;5;82m   Github : %s \n%s\n\n\n\033[00m",AUTHOR,VERSION,GITHUB,TOOLS_BANNER);
}

///////////////////////////////////////////
//  Function for get ip of the domain name
///////////////////////////////////////////

char *get_ip(char *domain,char *buffer)
{
    struct hostent *he;
    he = gethostbyname(domain);
    int i = 0;
    
    while (he->h_addr_list[i] != NULL){
        buffer = inet_ntoa( (struct in_addr) * ((struct in_addr *) he->h_addr_list[i]));
        i++;
    }

    return (buffer);
}

///////////////////////////
//  Main function 
//////////////////////////


int main(int argc, char *argv[])
{
    show_banner();

    if (argc < 4){
        printf("\t\033[38;5;82musage : %s <host> <maxport> <timeout> -v (for verbosity is optional)\n\t        %s 192.168.1.1 1000 10\n\t        %s 192.168.1.1 1000 10 -v\n\n\n\033[00m",argv[0],argv[0],argv[0]);
        exit(-1);
    }
    
    char buffer[32];
    int fd;
    struct sockaddr_in s;
    struct timeval timeout;
    struct servent *sv = {0};

    int verbosity = 0;

    if (argc == 5)
        if (strcmp(argv[4],"-v") == 0)
            verbosity = 1;
        else
            verbosity = 0;
    

    memset(&s,0,sizeof(s));
    memset(&timeout,0,sizeof(timeout));
    memset(buffer,0,sizeof(buffer));
    
    if (isdigit(argv[1][0]) == 0){
        char *b = get_ip(argv[1],buffer);
        s.sin_addr.s_addr = inet_addr(b);
    } else {
        s.sin_addr.s_addr = inet_addr(argv[1]);
    }

    s.sin_family = AF_INET;

    timeout.tv_sec = atoi(argv[3]) / 1000;
    timeout.tv_usec = (atoi(argv[3]) %1000) * 1000;
    
    
    printf("\033[38;5;82m[\033[1;96m+\033[38;5;82m] Target IP     : \033[1;93m%s\n\033[00m",argv[1]);
    printf("\033[38;5;82m[\033[1;96m+\033[38;5;82m] RangePort     : \033[1;93m1-%s\n\033[00m",argv[2]);
    printf("\033[38;5;82m[\033[1;96m+\033[38;5;82m] Timeout (ms)  : \033[1;93m%d\n\033[00m",atoi(argv[3]));
    printf("\033[38;5;82mPORT\tSTATE\tSERVICE\033[00m\n");
    
    for (int i = 1;i<=atoi(argv[2]);i++)
    {
        s.sin_port = htons(i);
        fd = socket(AF_INET,SOCK_STREAM,IPPROTO_TCP);
        setsockopt(fd,SOL_SOCKET,SO_SNDTIMEO,&timeout,sizeof(timeout));
        sv = getservbyport(ntohs(i),NULL);

        if (verbosity){
            if (isConnected(fd,s) != SOCKET_ERROR) {
                printf("\033[1;96m%d\033[38;5;82m \topen \t%s\n\033[00m",i,sv->s_name);
            } else {
                printf("\033[38;5;196m%d\033[38;5;82m \tclosed \n\033[00m",i);
            }

        } else {
            if (isConnected(fd,s) != SOCKET_ERROR){
                printf("\033[1;96m%d\033[38;5;82m \topen \t%s\n\033[00m",i,sv->s_name);
            }
        }
        
        memset(&fd,0,sizeof(fd));
        memset(&s.sin_port,0,sizeof(s.sin_port));
        memset(&sv,0,sizeof(sv));
    }

    close(fd);

    return (0);
}