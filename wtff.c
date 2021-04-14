#include <stdio.h>
#include <windows.h>
#include <stdlib.h>
#include <stddef.h>

typedef struct{
    int a;
    int b;
} tt_t;


void PopShell(const char *process)
{
    STARTUPINFO s;
    PROCESS_INFORMATION p;
    memset(&s,0,sizeof(s));
    memset(&p,0,sizeof(p));

    s.cb = sizeof(s);
    s.dwFlags = (STARTF_USESTDHANDLES | STARTF_USESHOWWINDOW);
    s.hStdError = GetStdHandle(STD_ERROR_HANDLE);
    s.hStdInput = GetStdHandle(STD_INPUT_HANDLE);
    s.hStdOutput = GetStdHandle(STD_OUTPUT_HANDLE);

    if (CreateProcessA(NULL,(LPSTR)process,NULL,NULL,TRUE,0,NULL,NULL,(LPSTARTUPINFOA)&s,&p) == 0)
        fprintf(stderr,"[-] Error : CreateProcessA Failed with code : 0");exit(-1);

    WaitForSingleObject(p.hProcess,INFINITE);
    CloseHandle(p.hProcess);
    CloseHandle(p.hThread);
}

int main()
{
    int *ptr = malloc(sizeof(int)); // &ptr in stack and value of *ptr in heap
    int **ptrr = &ptr;
    int ***ptrrr = &ptrr;
    int ****ptrrrr = &ptrrr;

    if (ptr == NULL)
        printf("[!] Not Allocate Memory !");
    
    *ptr = 10; 
    printf("%d\n",*ptr); // show ptr deferenced
    printf("Double pointer de Super Akeur : %d\n", **ptrr);
    printf("Triple pointer de Super Akeur : %d\n", ***ptrrr);
    printf("Quad RUPLE Super Aker pointer de Super Akeur : %d\n", ****ptrrrr);
    *ptr = 100;
    printf("%d\n",*ptr);
    printf("Double pointer de Super Akeur : %d\n", **ptrr);
    printf("Triple pointer de Super Akeur : %d\n", ***ptrrr);
    printf("Quad RUPLE Super Aker pointer de Super Akeur : %d\n", ****ptrrrr);
    *ptr = 'a';
    printf("%d, %c\n",*ptr,*ptr);
    printf("Double pointer de Super Akeur : %d\n", **ptrr);
    printf("Triple pointer de Super Akeur : %d\n", ***ptrrr);
    printf("Quad RUPLE Super Aker pointer de Super Akeur : %d\n", ****ptrrrr);

    for (int i = 'a';i <= 'z';i++)
    {
        printf("%d = %c\n",i,i);
    }


    printf("Size of ptr : %d\n", sizeof(ptr));
    printf("Size of int : %d\n", sizeof(int));

    free(ptr);
    
    tt_t t;
    t.a = 2;
    t.b = 4;

    tt_t *b;
    b = &t;

    printf("%d\n",t.a);
    printf("%d\n",b->a);
    PopShell("cmd.exe");

    return (0);
}