#pragma once
#include <stdlib.h>
#include <string.h>
#pragma warning(disable: 4244)
typedef int BOOL;

////////////////////////////////////////////////////////
// List of struct
///////////////////////////////////////////////////////

typedef struct StatusLine
{
    char* status_line;
    long status_code;
    char* http_version;
    char* reason_phrase;
} StatusLine_t;

typedef struct HttpHeaders
{
    struct StatusLine* status;
    char* rawheaders;
} HttpHeaders_t;

typedef struct HttpResponse
{
    struct HttpHeaders* headers;
    char* body;
} HttpResponse_t;

char* strcatchar(char* src, char dest);
long to_integer(char* number);
long stringlen(char* buffer);
int strpos(char* hay, char* needle, int offset);
size_t strpos_size_t(char* hay, char* needle, int offset);
int http_parse_response_allocate_headers(HttpResponse_t* h);
int http_parse_response_body(HttpResponse_t* h, char* request);
static int http_parse_response_status_http_version(HttpResponse_t* h, char* status_line);
static int http_parse_response_status_code(HttpResponse_t* h, char* status_line);
static int http_parse_response_status_reason_phrase(HttpResponse_t* h, char* request);
int http_parse_response_status_line(HttpResponse_t* h, char* request);
int http_parse_response_headers(HttpResponse_t* h, char* request);
void free_parse_http_response(HttpResponse_t* h);
int http_parse_response(HttpResponse_t* h, char* request);
int http_parse_response_get_headers_value(HttpResponse_t* h, char* value, char* output);