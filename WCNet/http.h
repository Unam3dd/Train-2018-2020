#pragma once
#define CURL_STATICLIB
#include "http_response_parser.h"
#include "curl/curl.h"

#pragma comment (lib, "Normaliz.lib")
#pragma comment (lib, "Wldap32.lib")
#pragma comment (lib,"Crypt32.lib")
#pragma comment (lib, "advapi32.lib")

struct Headers {
    char* memory;
    size_t size;
};

struct Body {
    char* memory;
    size_t size;
};

static size_t header_callback(char* buffer, size_t size, size_t nitems, void* userdata);
static size_t WriteMemoryCallback(void* contents, size_t size, size_t nmemb, void* userp);
char* http_get(char* url,char *user_agent,BOOL follow_redirect);
char* http_post(char* url, char* postfields,char *user_agent,BOOL follow_redirect);
HttpResponse_t *requests_get(char* url,char *user_agent,BOOL follow_redirect);
HttpResponse_t* request_post(char* url, char* data, char* user_agent,BOOL follow_redirect);