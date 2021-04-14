#pragma once
#include <stdlib.h>

#define true 1
#define false 0
typedef int bool;


char *stringcopy(char *output,char *input)
{
    int i = 0;

    for (i;input[i] != '\0';i++)
    {
        output[i] = input[i];
    }
    
    output[i] = '\0';

    return (output);
}

size_t stringlength(char *buffer)
{
    size_t i = 0;
    
    while (buffer[i] != '\0')
    {
        i++;
    }

    return (i);
}

char *stringconcat(char *src,char *dest)
{
    int i = 0;
    size_t srcsize = stringlength(src);

    for (i;dest[i] != '\0';i++)
    {
        if (stringlength(dest) >= sizeof(src))
            return (NULL);
        
        src[srcsize++] = dest[i];
    }

    src[srcsize++] = '\0';

    return (src);
}

char *stringconcatchar(char *src,char dest)
{
    int i = 0;
    size_t srcsize = stringlength(src);
    src[srcsize++] = dest;
    src[srcsize++] = '\0';
    return (src);
}


bool stringcompare(char *str1,char *str2)
{
    if (stringlength(str1) != stringlength(str2))
        return (false);

    for (int i = 0;str1[i] != '\0';i++)
    {
        if (str1[i] != str2[i])
            return (false);
    }

    return (true);
}

char *stringupper(char *buffer,char *output)
{
    int i = 0;
    for (i;buffer[i] != '\0';i++)
    {
        if (buffer[i] >= 'a' && buffer[i] <= 'z')
            output[i] = (buffer[i] - 32);
    }

    output[i] = '\0';

    return (output);
}

char *stringlower(char *buffer,char *output)
{
    int i = 0;
    for (i;buffer[i] != '\0';i++)
    {
        if (buffer[i] >= 'A' && buffer[i] <= 'z')
            output[i] = (buffer[i] + 32);
    }

    output[i] = '\0';
    return (output);
}

char *stringcharreplace(char *buffer,char asciicode,char replaceasciicode,char *output)
{
    int i = 0;
    
    for (i;buffer[i] != '\0';i++)
    {
        if (buffer[i] == asciicode)
            output[i] = replaceasciicode;
        else
            output[i] = buffer[i];
    }

    output[i] = '\0';

    return (output);
}

char *stringcharreplacepos(char *buffer,char asciicode,char replaceasciicode,int pos,char *output)
{
    int i = 0;

    for (i;buffer[i] != '\0';i++)
    {
        if (i == pos)
        {
            if (buffer[i] == asciicode)
                output[i] = replaceasciicode;
        }

        output[i] = buffer[i];
    }

    output[i] = '\0';
    return (output);
}

bool stringsearchchar(char *buffer,char asciicode)
{
    int i = 0;
    for (i;buffer[i] != '\0';i++){
        if (buffer[i] == asciicode)
            return (true);
    }

    return (false);
}

long stringsearchchargetpos(char *buffer,char asciicode)
{
    int i = 0;
    for (i;buffer[i] != '\0';i++){
        if (buffer[i] == asciicode)
            return (i);
    }

    return (-1);
}

bool stringsubstr(char *buffer,char *substr)
{
    int i = 0;
    int n = 0;
    size_t nsize = stringlength(substr);

    for (i;buffer[i] != '\0';i++)
    {
        if (buffer[i] == substr[n]){
            n++;
        }
    }

    if (nsize == n)
        return (true);
    
    return (false);
}

void *memory_set(void *ptr,int value,size_t nsize)
{
    unsigned char *newv = ptr;
    while (nsize > 0)
    {
        *newv = (unsigned char) value;
        nsize--;
        newv++;
    }

    return (ptr);
}

/////////////////////////////////////
/// to be corrected
////////////////////////////////////

char **splitchar(char *buffer,char delim)
{
    int index = 0,ncount = 0;
    char tmp[sizeof(buffer)*2] = {0};
    char buf[sizeof(buffer)+1] = {0};
    char **out = NULL;
    stringcopy(buf,buffer);
    stringconcatchar(buf,delim);

    for (int i = 0;buf[i] != '\0';i++)
    {
        if (buf[i] == delim)
            ncount++;
    }

    out = malloc(sizeof(char *) * ncount+1);

    if (out == NULL)
        return (NULL);
    
    for (int x = 0;buf[x] != '\0';x++)
    {
        if (buf[x] != delim){
            stringconcatchar(tmp,buf[x]);
        }
        else
        {
            out[index] = malloc(sizeof(char) * stringlength(tmp)+1);
            
            if (out[index] == NULL)
                return (NULL);
            
            stringcopy(out[index],tmp);
            index++;
            memory_set(tmp,0,sizeof(tmp));
        }
    }

    out[index] = NULL;

    return (out);
}


/*int replace_char(char *buffer,char code)
{
    char buf[sizeof(buffer)+1] = {0};
    strcpy(buf,buffer);
    int n = 0;

    for (int i = 0;buf[i] != '\0';i++)
    {
        if (buf[i] != code){
            buffer[n] = buf[i];
            n++;
        }
    }

    buffer[n] = '\0';
}*/