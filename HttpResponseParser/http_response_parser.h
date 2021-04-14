#pragma once
#include <stdlib.h>
#include <string.h>

////////////////////////////////////////////////////////
// Author : Unam3dd, Beginning in C
////////////////////////////////////////////////////////


////////////////////////////////////////////////////////
// List of struct
///////////////////////////////////////////////////////

typedef struct StatusLine
{
    char *status_line;
    long status_code;
    char *http_version;
    char *reason_phrase;
} StatusLine_t;

typedef struct HttpHeaders
{
    struct StatusLine *status;
    char *rawheaders;
} HttpHeaders_t;

typedef struct HttpResponse
{
    struct HttpHeaders *headers;
    char *body;
} HttpResponse_t;

////////////////////////////////////////////////////////
// function for concat char in str
///////////////////////////////////////////////////////

char *strcatchar(char *src,char dest)
{
    int i = 0;
    size_t srcsize = strlen(src);
    
    if (src[srcsize] == '\0'){
        src[srcsize] = dest;
        src[srcsize++] = '\0';
    } else {
        src[srcsize++] = dest;
        src[srcsize++] = '\0';
    }

    return (src);
}

////////////////////////////////////////////////////////
// function like atoi for char to long
///////////////////////////////////////////////////////

long to_integer(char *number)
{
    long todec = 0;

    for (int i = 0;number[i] >= '0' && number[i] <= '9';i++)
    {
        todec *= 10;
        todec += number[i]++ & 0xF;
    }

    return (todec);
}

////////////////////////////////////////////////////////
// function for get position in string
///////////////////////////////////////////////////////

int strpos(char *hay,char *needle,int offset)
{
    char haystack[strlen(hay)];
    
    strncpy(haystack,hay+offset,strlen(hay)-offset); // copy hay+offset in haystack buffer
    
    char *ptr = strstr(haystack,needle); // search needle in haystack with offset
    
    if (ptr)
        return (ptr - haystack+offset); // return position
    
    return (1);
}

////////////////////////////////////////////////////////
// function for allocate memory 
///////////////////////////////////////////////////////

int http_parse_response_allocate_headers(HttpResponse_t *h)
{
    h->headers = malloc(sizeof(HttpHeaders_t));

    if (h->headers == NULL)
        return (0);
    
    h->headers->status = malloc(sizeof(StatusLine_t));

    if (h->headers->status == NULL)
        return (0);
    
    return (1);
}

////////////////////////////////////////////////////////
// function for parse body in HTTP response
///////////////////////////////////////////////////////

int http_parse_response_body(HttpResponse_t *h,char *request)
{
    int maxsize = 4096,in = 0,pos;
    char *buffer = (char*)calloc(maxsize,sizeof(char));

    if (buffer == NULL)
        return (0);

    pos = strpos(request,"\r\n\r\n",0);
    pos += 4;

    while (request[pos] != '\0')
    {
        if (in>=maxsize){
            maxsize += 512;
            buffer = (char*)realloc(buffer,sizeof(char) * maxsize);
            
            if (buffer == NULL)
                return (0);
        }
        
        buffer[in] = request[pos];
        in++;
        pos++;
    }

    h->body = malloc(sizeof(char) * in+1);

    if (h->body == NULL)
        return (0);

    strcpy(h->body,buffer);

    free(buffer);

    return (1);
}

////////////////////////////////////////////////////////
// function for parse http version in status line
///////////////////////////////////////////////////////

static int http_parse_response_status_http_version(HttpResponse_t *h,char *status_line)
{
    int i = 0;
    h->headers->status->http_version = malloc(sizeof(char) * 8);

    if (h->headers->status->http_version == NULL)
        return (0);
    

    for (i;status_line[i] != ' ';i++)
    {
        h->headers->status->http_version[i] = status_line[i];
    }

    h->headers->status->http_version[i] =  '\0';

    return (1);
}

////////////////////////////////////////////////////////
// function for parse status code in status line
///////////////////////////////////////////////////////

static int http_parse_response_status_code(HttpResponse_t *h,char *status_line)
{
    int i = 9, x = 0;
    char statuscode[4] = {0};

    for (i;i<=11;i++)
    {
        statuscode[x] = status_line[i];
        x++;
    }

    h->headers->status->status_code = to_integer(statuscode);
    
    return (1);
}

////////////////////////////////////////////////////////
// function for parse status reason phrase in status line
///////////////////////////////////////////////////////

static int http_parse_response_status_reason_phrase(HttpResponse_t *h,char *request)
{
    int i = 13,x = 0;

    h->headers->status->reason_phrase = malloc(sizeof(char) * 32);

    if (h->headers->status->reason_phrase == NULL)
        return (0);
    
    for (i;request[i] != '\0';i++)
    {
        h->headers->status->reason_phrase[x] = request[i];
        x++;
    }

    h->headers->status->reason_phrase[x] = '\0';

    return (1);
}

////////////////////////////////////////////////////////
// function for parse response status line
///////////////////////////////////////////////////////

int http_parse_response_status_line(HttpResponse_t *h,char *request)
{
    char buffer[50] = {0};
    int pos = 0;

    while (request[pos] != '\r')
    {
        buffer[pos] = request[pos];
        pos++;
    }

    buffer[pos] = '\0';

    h->headers->status->status_line = malloc(sizeof(char) * pos+1);

    if (h->headers->status->status_line == NULL)
        return (0);
    
    strcpy(h->headers->status->status_line,buffer);

    if (http_parse_response_status_http_version(h,buffer) != 1)
        return (0);
    
    http_parse_response_status_code(h,buffer);

    if (http_parse_response_status_reason_phrase(h,buffer) != 1)
        return (0);
    
    return (1);
}

////////////////////////////////////////////////////////
// function for parse generale headers
///////////////////////////////////////////////////////

int http_parse_response_headers(HttpResponse_t *h,char *request)
{
    int i = 0, pos;
    
    pos = strpos(request,"\r\n\r\n",0);

    h->headers->rawheaders = malloc(sizeof(char) * pos+1);

    if (h->headers->rawheaders == NULL)
        return (0);
    
    while (i<=pos)
    {
        h->headers->rawheaders[i] = request[i];
        i++;
    }

    h->headers->rawheaders[i] = '\0';

    return (1);
}

////////////////////////////////////////////////////////
// Free memory of HttpResponse Headers and status
///////////////////////////////////////////////////////

void free_parse_http_response(HttpResponse_t *h)
{
    if (h->body != NULL)
        free(h->body);
    
    free(h->headers->rawheaders);
    free(h->headers->status->reason_phrase);
    h->headers->status->status_code = 0;
    free(h->headers->status->http_version);
    free(h->headers->status->status_line);
    free(h->headers->status);
    free(h->headers);
}

////////////////////////////////////////////////////////
// General function for parse response
///////////////////////////////////////////////////////

int http_parse_response(HttpResponse_t *h,char *request)
{
    if (http_parse_response_allocate_headers(h) != 1)
        return (0);
    
    if (http_parse_response_body(h,request) != 1)
        return (0);
    
    if (http_parse_response_status_line(h,request) != 1)
        return (0);
    
    if (http_parse_response_headers(h,request) != 1)
        return (0);

    return (1);
}

////////////////////////////////////////////////////////
// Get Value of generale headers
// https://tools.ietf.org/html/rfc2616#section-4.5
///////////////////////////////////////////////////////

int http_parse_response_get_headers_value(HttpResponse_t *h,char *value,char *output)
{
    if (h->headers->rawheaders == NULL)
        return (0);
    
    int i = 0;
    int pos = strpos(h->headers->rawheaders,value,0);
    pos += strlen(value)+2;

    while(h->headers->rawheaders[pos] != '\r')
    {
        output[i] = h->headers->rawheaders[pos];
        pos++;
        i++;
    }

    output[i] = '\0';

    return (1);
}