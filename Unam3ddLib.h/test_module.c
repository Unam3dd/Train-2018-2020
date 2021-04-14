#include "unam3d.h"
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <unistd.h>

int main(){
    clear();
    hello_world();
    char *rinput = raw_input("raw_input >>",4096);
    printf("%s\n",rinput);
    int inp = input("input int >>");
    printf("%d\n",inp);
    char *get_u = get_user();
    printf("User : %s\n",get_u);
    int sub = substring_in_string("Hello","Hello World");
    if (sub ==0){
        print("'Hello' Found in Hello World");
    } else {
        print("'Hello' Not Found in Hello World");
    }
    print("Hello Unam3dd!");
    int path_check = os_path_exists("/home/");
    if (path_check ==0){
        print("/home/ Found !");
    } else {
        print("/home/ Not Found !");
    }
    char *ftp_version = ftp_get_version("127.0.0.1",21);
    print(ftp_version);
    char *ssh_version = ssh_getserver_version("127.0.0.1",22);
    print(ssh_version);
    //linux_reverse_shell("192.168.1.27",444);
    int check_p = check_port_tcp("127.0.0.1",21);
    if (check_p ==0){
        print("[*] Port 21 Open !");
    } else {
        print("[!] Port 21 Closed !");
    }
    char *fp = file_read("requirements.sh",65556,"r");
    printf("%s\n",fp);
    
    file_write("variable_static","Hello World\n","a"); // w,w+,a,a+
    //int dl_file;
    //dl_file = download_file("https://picture.jpg","out.jpg");
    int s = http_requests_status_code("https://www.google.com/",0); // 0 = follow_redirect True, 1 = follow_redirect False
    printf("Status Code : %d\n",s);
    if (s ==200){
        print("Requests SuccessFull !\n");
    } 
    else if (s ==0){
        print("Error Requests !\n");
    } else {
        printf("Requests SuccessFull with %d status code\n",s);
    }

    char *d = http_requests("https://ipinfo.io/json",0);
    printf("%s\n",d);
    int login_ssh = ssh_login("127.0.0.1",22,"dxvistxr","root");
    if (login_ssh ==0){
        printf("[*] Loged On SSH Server !\n");
    } else {
        printf("[!] Not Loged On SSH Server !\n");
    }
}
