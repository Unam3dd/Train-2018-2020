#include "console.h"


///////////////////////////////////
//  Console function
///////////////////////////////////
static int command_complete(int count,int key)
{
    printf(" %s",COMMAND_LIST);
    rl_forced_update_display();
}

int to_integer(char *n)
{
    int todec = 0;
    
    for (int i = 0;n[i] >= '0' && n[i] <= '9';i++)
    {
        todec *= 10;
        todec += n[i]++ & 0xF;
    }

    return (todec);
}

void console(const char *prompt)
{
    char *input;
    signal(SIGINT,check_sigint);
    rl_bind_key('\t',command_complete);
    
    pthread_t thread_1;
    int thread_enable = 0;
    int n = 1;

    SOCKET *array = (SOCKET *)malloc(sizeof(SOCKET) * n);

    if (!array){
        fprintf(stderr,"[-] Error allocate memory !\n");
        exit(-1);
    }

    ThreadHandle_t t = {0};
    t.n = 0;
    t.array = array;

    do{
        input = readline(prompt);
        add_history(input);

        if (strcmp(input,"quit") == 0 || strcmp(input,"exit") == 0){
            printf("\033[38;5;196m[+] Thanks for using Odin Tools By Unam3dd\033[00m\n");
            break;
        }

        if (strcmp(input,"banner") == 0)
            if (ReadBanner("banner/viking.txt") != 0)
                fprintf(stderr,"\033[38;5;196m[-] Error print banner !\033[00m\n");

        if (strcmp(input,"cls") == 0 || strcmp(input,"clear") == 0)
            system("clear");

        if (strstr(input,"sh")){
            char *args = get_args(input);
            system(args);
            free(args);
        }

        if (strcmp(input,"session") == 0){
            list_connections(t.array);
        }

        if (strstr(input,"enter")){
            char *args = get_args(input);
            int id = to_integer(args);
            enter_session(id,t.array);
            free(args);
        }

        if (strstr(input,"listen")){
            char *args = get_args(input);
            int port = to_integer(args);
            SOCKET fd = listen_on_new_port(port);

            t.fd = fd;

            if (pthread_create(&thread_1,NULL,handle_new_client,(void *)&t) != 0)
            {
                fprintf(stderr,"[-] Error thread !\n");
            }

            free(args);
        }

        if (strcmp(input,"help") == 0)
            show_help();

    } while (1);

    if (thread_enable == 1){
        pthread_cancel(thread_1);
        pthread_join(thread_1,NULL);
    }

    close_all_connections(t.array,t.n);

    free(array);
}

void check_sigint(int signum)
{
    signal(SIGINT,check_sigint);
    printf("\n\033[38;5;196m[-] CTRL+C for quit type quit or exit\n\033[00m");
    fflush(stdout);
}

int strpos(char *hay,char *needle,int offset)
{
    char haystack[strlen(hay)];
    
    strncpy(haystack,hay+offset,strlen(hay)-offset); // copy hay+offset in haystack buffer
    
    char *ptr = strstr(haystack,needle); // search needle in haystack with offset
    
    if (ptr)
        return (ptr - haystack+offset); // return position
    
    return (1);
}

char *get_args(char *input)
{
    char buffer[BUFFER_CONSOLE_SIZE] = {0};
    int pos = strpos(input," ",0);
    pos += 1;
    int i = 0;

    while (input[pos] != '\0')
    {
        buffer[i] = input[pos];
        pos++;
        i++;
    }
    
    buffer[i] = '\0';

    char *ptr = (char *)calloc(1,strlen(buffer));

    if (!ptr)
        return (NULL);
    
    strncpy(ptr,buffer,strlen(buffer));

    return (ptr);
}

void show_help(void)
{
    printf("\033[38;5;196m[ᛃᛃᛃᛃᛃᛃᛃᛃᛃᛃHELP MAINᛃᛃᛃᛃᛃᛃᛃᛃᛃᛃ]\n");
    printf("\033[38;5;196m   help            show help\n");
    printf("\033[38;5;196m   quit           quit console\n");
    printf("\033[38;5;196m   exit           quit Odin\n");
    printf("\033[38;5;196m   sh <args>     execute local shell command\n");
    printf("\033[38;5;196m   listen <port>  listen on port\n");
    printf("\033[38;5;196m   session        list session received\n");
    printf("\033[38;5;196m   enter         enter in session\n");
    printf("\033[38;5;196m[ᛃᛃᛃᛃᛃᛃᛃᛃᛃᛃHELP MAINᛃᛃᛃᛃᛃᛃᛃᛃᛃᛃ]\033[00m\n");
}