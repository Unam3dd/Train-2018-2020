#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>

struct arg_struct{
    int arg1;
    char *arg2;
};

void *pri(void *arguments)
{
    struct arg_struct *arg_params = (struct arg_struct *)arguments;
    sleep(arg_params->arg1);
    printf("Im First Function And Sleep for %d\n",arg_params -> arg1);
    printf("%s\n",arg_params -> arg2);
    return NULL;
}

void *pri2(void *arguments)
{
    struct arg_struct *arg_params2 = (struct arg_struct *)arguments;
    printf("%s\n",arg_params2 -> arg2);
    return NULL;
}

int main(){
    struct arg_struct params;
    params.arg1 = 5;
    params.arg2 = "Hello WOrld";

    struct arg_struct params2;
    params2.arg2 = "Hello WOrld 2";

    pthread_t thread_id,thread_id2;

    pthread_create(&thread_id, NULL, &pri, (void *)&params);
    pthread_create(&thread_id2, NULL, &pri2, (void *)&params2);
    pthread_join(thread_id,NULL);
    pthread_join(thread_id2,NULL);
    return 0;
}
