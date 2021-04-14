#include "http.h"

static size_t header_callback(char* buffer, size_t size, size_t nitems, void* userdata)
{
    size_t realsize = size * nitems;
    struct Headers* mem = (struct Headers*)userdata;

    char* ptr = (char *)realloc(mem->memory, mem->size + realsize + 1);

    if (ptr == NULL) {
        printf("not enough memory  (realloc returned NULL)\n");
        return (0);
    }

    mem->memory = ptr;
    memcpy(&(mem->memory[mem->size]), buffer, realsize);
    mem->size += realsize;
    mem->memory[mem->size] = 0;

    return (realsize);
}

static size_t WriteMemoryCallback(void* contents, size_t size, size_t nmemb, void* userp)
{
    size_t realsize = size * nmemb;
    struct Body* mem = (struct Body*)userp;

    char* ptr = (char *)realloc(mem->memory, mem->size + realsize + 1);
    if (ptr == NULL) {
        /* out of memory! */
        fprintf(stderr,"not enough memory (realloc returned NULL)\n");
        return (0);
    }

    mem->memory = ptr;
    memcpy(&(mem->memory[mem->size]), contents, realsize);
    mem->size += realsize;
    mem->memory[mem->size] = 0;

    return (realsize);
}

char* http_get(char* url,char *user_agent,BOOL follow_redirect)
{
    CURL* curl_handle;
    CURLcode res;
    struct Headers headers = { 0 };
    struct Body body = { 0 };

    headers.memory = (char*)malloc(1);

    if (headers.memory == NULL)
        return (NULL);

    body.memory = (char*)malloc(1);

    if (body.memory == NULL)
        return (NULL);

    headers.size = 0;
    body.size = 0;

    curl_global_init(CURL_GLOBAL_ALL);
    curl_handle = curl_easy_init();

    curl_easy_setopt(curl_handle, CURLOPT_URL, url);
    curl_easy_setopt(curl_handle, CURLOPT_WRITEFUNCTION, WriteMemoryCallback);
    curl_easy_setopt(curl_handle, CURLOPT_HEADERFUNCTION, header_callback);
    curl_easy_setopt(curl_handle, CURLOPT_WRITEDATA, (void*)&body);
    curl_easy_setopt(curl_handle, CURLOPT_WRITEHEADER, (void*)&headers);
    
    if (user_agent == NULL)
        curl_easy_setopt(curl_handle, CURLOPT_USERAGENT, "libcurl-agent/1.0");
    else
        curl_easy_setopt(curl_handle, CURLOPT_USERAGENT, user_agent);

    if (follow_redirect == TRUE)
        curl_easy_setopt(curl_handle, CURLOPT_FOLLOWLOCATION, 1L);

    res = curl_easy_perform(curl_handle);

    if (res != CURLE_OK) {
        fprintf(stderr, "[-] error in curl_easy_perform() : %s\n", curl_easy_strerror(res));
        return (NULL);
    }

    char* ptr = (char*)malloc(sizeof(char) * (headers.size + body.size) + 1);

    if (ptr == NULL)
        return (NULL);

    sprintf(ptr, "%s%s", headers.memory, body.memory);
    ptr[headers.size + body.size + 1] = '\0';

    curl_easy_cleanup(curl_handle);
    free(headers.memory);
    free(body.memory);
    curl_global_cleanup();

    return (ptr);
}


char* http_post(char* url, char* postfields,char *user_agent,BOOL follow_redirect)
{

    if (url == NULL || postfields == NULL)
        return (NULL);

    CURL* curl_handle;
    CURLcode res;

    struct Headers headers = { 0 };
    struct Body body = { 0 };

    headers.memory = (char*)malloc(1);

    if (headers.memory == NULL)
        return (NULL);

    body.memory = (char*)malloc(1);

    if (body.memory == NULL)
        return (NULL);

    headers.size = 0;
    body.size = 0;

    curl_global_init(CURL_GLOBAL_ALL);

    curl_handle = curl_easy_init();

    if (curl_handle) {
        curl_easy_setopt(curl_handle, CURLOPT_URL, url);
        curl_easy_setopt(curl_handle, CURLOPT_POSTFIELDS, postfields);
        curl_easy_setopt(curl_handle, CURLOPT_WRITEFUNCTION, WriteMemoryCallback);
        curl_easy_setopt(curl_handle, CURLOPT_HEADERFUNCTION, header_callback);
        curl_easy_setopt(curl_handle, CURLOPT_WRITEDATA, (void*)&body);
        curl_easy_setopt(curl_handle, CURLOPT_WRITEHEADER, (void*)&headers);

        if (user_agent == NULL)
            curl_easy_setopt(curl_handle, CURLOPT_USERAGENT, "libcurl-agent/1.0");
        else
            curl_easy_setopt(curl_handle, CURLOPT_USERAGENT, user_agent);

        if (follow_redirect == TRUE)
            curl_easy_setopt(curl_handle, CURLOPT_FOLLOWLOCATION, 1L);

        res = curl_easy_perform(curl_handle);

        if (res != CURLE_OK) {
            fprintf(stderr, "[-] curl_easy_perform() : %s\n", curl_easy_strerror(res));
            return (NULL);
        }
    }

    char* ptr = (char*)malloc(sizeof(char) * (headers.size + body.size) + 1);

    if (ptr == NULL)
        return (NULL);

    sprintf(ptr, "%s%s", headers.memory, body.memory);
    ptr[headers.size + body.size + 1] = '\0';

    curl_easy_cleanup(curl_handle);
    free(headers.memory);
    free(body.memory);
    curl_global_cleanup();

    return (ptr);
}

HttpResponse_t *requests_get(char* url,char *user_agent,BOOL follow_redirect)
{
    HttpResponse_t* res = malloc(sizeof(HttpResponse_t*));

    if (res == NULL)
        return (NULL);

    char* response = http_get(url,user_agent,follow_redirect);

    if (response == NULL)
        return (NULL);

    http_parse_response(res, response);
    //Sleep(100);
    free(response);
    return (res);
}

HttpResponse_t* request_post(char* url, char* data, char* user_agent,BOOL follow_redirect)
{
    HttpResponse_t* res = malloc(sizeof(HttpResponse_t*));

    if (res == NULL)
        return (NULL);

    char* response = http_post(url, data, user_agent,follow_redirect);

    if (response == NULL)
        return (NULL);

    http_parse_response(res, response);
    free(response);
    return (res);
}