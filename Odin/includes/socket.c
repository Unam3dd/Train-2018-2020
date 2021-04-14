#include "socket.h"


SOCKET listen_on_new_port(int port)
{
    struct sockaddr_in socks = {0};

    int fd = socket(AF_INET,SOCK_STREAM,IPPROTO_TCP);

    if(fd < 0)
        return (errno);
    
    socks.sin_addr.s_addr = htonl(INADDR_ANY);
    socks.sin_port = htons(port);
    socks.sin_family = AF_INET;

    if (bind(fd,(struct sockaddr *)&socks,sizeof(socks)) < 0)
        return (-1);
    
    if (listen(fd,SOMAXCONN) < 0)
        return (-1);
    
    printf("\033[38;5;196m[+] Listening on port %d\033[00m\n",port);

    return (fd);
}

void *handle_new_client(void *param)
{
    ThreadHandle_t t = *(ThreadHandle_t *)param;
    int n = 0;
    struct sockaddr_in client = {0};
    socklen_t client_size = sizeof(client);

    struct sockaddr_in peer = {0};
    socklen_t peer_size = sizeof(peer);

    while (1)
    {
        SOCKET cfd = accept(t.fd,(struct sockaddr *)&client,&client_size);
        t.array[n] = cfd;
        t.n = n+1;
        getpeername(cfd,(struct sockaddr *)&peer,&peer_size);
        printf("[%d] Client : %s:%d\n",n,inet_ntoa(peer.sin_addr),ntohs(peer.sin_port));
        n++;
        t.array = (SOCKET *)realloc(t.array,sizeof(SOCKET) * n+1);

        if (!t.array){
            fprintf(stderr,"[-] Error allocate memory !\n");
            break;
        }

        t.array[n] = 0;
    }

    return (NULL);
}

void list_connections(SOCKET *array)
{
    struct sockaddr_in client = {0};
    socklen_t size_client = sizeof(client);

    for (int i = 0;array[i] != 0;i++)
    {
        getpeername(array[i],(struct sockaddr *)&client,&size_client);
        printf("[%d] Client : %s:%d\n",i,inet_ntoa(client.sin_addr),ntohs(client.sin_port));
    }

    return;
}

void close_all_connections(SOCKET *array,int n)
{
    for (int i = 0;array[i] != 0;i++)
    {
        close(array[i]);
    }

    return;
}

void *std_stream(void *param)
{
    int bytes;
    Stream_t s = *(Stream_t *)param;
    char buffer[MAX_BUFFER] = {0};

    while ((bytes = read(s.in,buffer,(MAX_BUFFER - 1))) > 0)
    {
        if (write(s.out,buffer,bytes) < 0){
            fprintf(stderr,"[-] Error writing in out stream !\n");
            break;
        }
    }

    if (bytes < 0)
        fprintf(stderr,"[-] Error read input stream !\n");
    

    return (NULL);
}

int shell_session(SOCKET fd)
{
    pthread_t thread;
    Stream_t s;
    int bytes;
    s.in = STDIN_FILENO;
    s.out = fd;
    char buffer[MAX_BUFFER] = {0};

    if (pthread_create(&thread,NULL,std_stream,(void *)&s) != 0){
        fprintf(stderr,"[-] Error during creating thread !\n");
    }

    while ((bytes = read(fd,buffer,MAX_BUFFER)) > 0)
    {
        if (write(STDOUT_FILENO,buffer,bytes) < 0){
            fprintf(stderr,"[-] Error write in destination stream !\n");
        }
    }

    if (bytes < 0)
        fprintf(stderr,"[-] Error during read socket !\n");
    
    pthread_cancel(thread);
    pthread_join(thread,NULL); //Make calling thread wait for termination of the thread TH. The exit status of the thread is stored in *THREAD_RETURN, if THREAD_RETURN is not NULL.
    
    return (0);
}

void enter_session(int id,SOCKET *array)
{
    shell_session(array[id]);
}