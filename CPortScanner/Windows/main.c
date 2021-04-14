#include "winpscan.h"
//compile : gcc .\winpscan.c .\main.c -o main.exe -lws2_32
// compile Optimized : gcc .\winpscan.c .\main.c -o main.exe -lws2_32 -s -w -O1 -O2

int main(int argc, char * argv[])
{
    show_banner();

    if (argc < 5){
        printf("usage : %s <host> <startport> <maxport> <timeoutms> -v (-v optional)\n",argv[0]);
        exit(-1);
    }

    Target t;
    strcpy(t.ip,argv[1]);
    t.startport = atoi(argv[2]);
    t.maxport = atoi(argv[3]);
    t.timeoutms = atoi(argv[4]);

    if (argc == 6){
        if (strcmp(argv[5],"-v") ==0)
            t.verbosity = 1;
        else
            t.verbosity = 0;
    } else
        t.verbosity = 0;

    PortScan(&t);

    return (0);
}