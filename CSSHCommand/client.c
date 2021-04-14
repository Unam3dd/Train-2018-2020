#include <stdio.h>
#include <libssh/libssh.h>
#include <stdlib.h>

// compile : cl /EHsc client.c /I"C:\vcpkg\installed\x86-windows\include/" /link C:\vcpkg\installed\x86-windows/lib/ssh.lib  /out:client.exe


int execute_commands(ssh_session s,ssh_channel channel,char *commands)
{
    int rc;
    char buffer[1024];
    int nbytes;

    channel = ssh_channel_new(s);

    if (channel == NULL)
        return (SSH_ERROR);
    
    rc = ssh_channel_open_session(channel);

    if (rc != SSH_OK)
    {
        ssh_channel_free(channel);
        return rc;
    }      
    
    rc = ssh_channel_request_exec(channel,commands);

    if (rc != SSH_OK)
    {
        ssh_channel_close(channel);
        ssh_channel_free(channel);
        return rc;
    }

    nbytes = ssh_channel_read(channel, buffer, sizeof(buffer),0);

    while (nbytes > 0)
    {
        if (write(1,buffer,nbytes) != (unsigned int) nbytes){
            ssh_channel_close(channel);
            ssh_channel_free(channel);
            return (SSH_ERROR);
        }
        nbytes = ssh_channel_read(channel,buffer,sizeof(buffer),0);
    }

    if (nbytes < 0)
    {
        ssh_channel_close(channel);
        ssh_channel_free(channel);
        return SSH_ERROR;
    }



    ssh_channel_send_eof(channel);
    ssh_channel_close(channel);
    ssh_channel_free(channel);
    return SSH_OK;
}


int main(int argc, char * argv[])
{
    if (argc < 6){
        printf("usage : %s <host> <port> <username> <password> <command>",argv[0]);
        exit(-1);
    }

    ssh_session session = ssh_new();
    int port = atoi(argv[2]);
    int rc;
    char buffer[1024];
    ssh_channel channel;

    if (session == NULL){
        fprintf(stderr,"[!] Error : %s\n",ssh_get_error(session));
        exit(-1);
    }
    
    ssh_options_set(session,SSH_OPTIONS_HOST,argv[1]);
    ssh_options_set(session,SSH_OPTIONS_PORT,&port);
    ssh_options_set(session,SSH_OPTIONS_USER,argv[3]);

    rc = ssh_connect(session);

    if (rc != SSH_OK){
        fprintf(stderr,"[!] Error : %s\n",ssh_get_error(session));
        exit(-1);
    }

    rc = ssh_userauth_password(session,NULL,argv[4]);

    if (rc != SSH_AUTH_SUCCESS)
    {
        fprintf(stderr,"[!] Error : %s\n",ssh_get_error(session));
        ssh_disconnect(session);
        ssh_free(session);
        exit(-1);
    }

    execute_commands(session,channel,argv[5]);

    ssh_disconnect(session);
    ssh_free(session);

    return (0);
}