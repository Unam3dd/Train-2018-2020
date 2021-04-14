#include <stdio.h>
#include <WinSock2.h>
#include <string.h>
#include <WS2tcpip.h>
#include <windows.h>

#define AUTHOR "\033[1;96munam3dd\033[00m"
#define VERSION "\033[1;96m0.1\033[00m"
#define GITHUB "\033[1;96mhttps://github.com/Unam3dd/\033[00m"
#define BANNER "\033[38;5;82m\t ______ _______                   \n\t|   __ \\     __|.----.---.-.-----.\n\t|    __/__     ||  __|  _  |     |\n\t|___|  |_______||____|___._|__|__|\n\033[00m"
#define TOOLS_BANNER "\t   \033[38;5;82mThis tools made with C programming language !\n\033[00m"

typedef struct Target {
    char ip[16];
    int startport;
    int maxport;
    int verbosity;
    int timeoutms;
} Target;

void PortScan(struct Target *target);
void show_banner();
char *get_ip(char *domain,char *buffer);