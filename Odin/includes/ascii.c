#include "ascii.h"

int ReadBanner(char *filename)
{
    FILE *fp;
    long file_size;

    fp = fopen(filename,"rb");

    if (!fp)
        return (-1);

    fseek(fp,0,SEEK_END);
    file_size = ftell(fp);
    fseek(fp,0,SEEK_SET);

    char *ptr = malloc(sizeof(char) * file_size);

    if (!ptr)
        return (-1);
    
    fread(ptr,sizeof(char),file_size,fp);

    printf("\033[38;5;196m%s\033[00m\n",ptr);

    free(ptr);

    return (0);
}