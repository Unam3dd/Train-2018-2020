#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int age = 5;
    int *ptr = &age;
    int **ptr2 = &ptr;
    printf("%d\n",**ptr2);
    int nplayer = 2;
    int *ptrplayer = NULL;
    ptrplayer = malloc(sizeof(int) * nplayer);
    
    if (ptrplayer == NULL)
        exit(-1);
    
    for (int i = 0;i<nplayer;i++) {
        printf("[%d]\n",ptrplayer[i]);
    }

    nplayer = 10;
    ptrplayer = realloc(ptrplayer,nplayer * sizeof(int));

    if (ptrplayer == NULL)
        exit(-1);
    
    printf("\n");

    

    for (int x = 0;x<nplayer;x++)
    {
        ptrplayer[x] = rand()%10;
        printf("[%p] [%d]\n",&ptrplayer[x],ptrplayer[x]);
    }

    ptrplayer[3] = 12;
    printf("[%p] [%d]\n",&ptrplayer[3],ptrplayer[3]);

    free(ptrplayer);

    return (0);
}