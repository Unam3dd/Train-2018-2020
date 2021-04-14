#ifndef UNAM3D_H
#define UNAM3D_H

void hello_world(void);
char * raw_input(char *input_string,int buffer);
int input(char *input_string);
char *get_user(void);
void clear(void);
int substring_in_string(char *substring,char *string);
void print(char *string);
int os_path_exists(const char *path);
char *ftp_get_version(char *target_ip,int port);
char *ssh_getserver_version(char *target_ip,int port);
void linux_reverse_shell(char *lhost,int port);
int check_port_tcp(char *ip,int port);
char *file_read(char *filename,int buffer,char *mode);
int file_write(char *filename,char *content,char *mode);
int download_file(char *link,char *output_file);
int http_get_response(char *link,int buffer);
int http_requests_status_code(char *link,int follow_location);
char *file_readlines_n(char *filename,char *mode);
char *file_readlines(char *filename,char *mode);
char *http_requests(char *link,int follow_redirect);
int ssh_login(char *ip,int port,char *username,char *password);

#endif
