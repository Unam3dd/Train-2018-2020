#include <stdlib.h>
#include <string.h>

char **Split(char *buffer,char *delim)
{
    char *token = strtok(buffer,delim);
    int n = 0;
    int space = 1;
    char **out = malloc(sizeof(char *) * space);
    
    if (out == NULL)
        return (NULL);

    while (token != NULL)
    {
        if (space == 1){
            out[n] = malloc(sizeof(char) * strlen(token));
            out[n] = token;
            token = strtok(NULL,delim);
            n++;
            space++;
        } else {
            out = realloc(out,sizeof(char *) * (space+1));
            out[n] = malloc(sizeof(char) * strlen(token));
            out[n] = token;
            token = strtok(NULL,delim);
            n++;
            space++;
        }
    }

    return (out);
}
