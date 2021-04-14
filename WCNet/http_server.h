#pragma once
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <winsock2.h>
#include <ws2tcpip.h>

#define HTTP_SERVER_PORT 80
#define HTTP_VERSION "HTTP/1.1"

#define HTTP_STATUS_CODE_CONTINUE "100"
#define HTTP_STATUS_CODE_CONTINUE_REASON "Continue"




////////////////////////////
// Structure HTTP SERVER  //
////////////////////////////

typedef struct http_server_info {
    int port;
    char path[256];
    SOCKET fdserver;
} http_server_info_t;


typedef struct http_client_peer {
    char *address;
    int port;
} http_client_peer_t;


typedef struct http_server_response_status_line
{
    char *status_code;
    char *reason_phrase;
    char *http_version;
    char *status_line;
} http_server_response_status_line_t;


typedef struct http_server_response_general_headers
{
    char *cache_control;
    char *connection;
    char *date;
    char *pragma;
    char *trailer;
    char *transfer_encoding;
    char *upgrade;
    char *via;
    char *warning;
} http_server_response_general_headers_t;

typedef struct http_server_response_request_headers
{
    char *accept;
    char *accept_charset;
    char *accept_encoding;
    char *accept_language;
    char *authorization;
    char *expect;
    char *from;
    char *host;
    char *if_match;
    char *if_modified_since;
    char *if_none_match;
    char *if_range;
    char *referer;
    char *TE;
    char *user_agent;
} http_server_response_request_headers_t;

typedef struct http_server_response_entity_headers
{
    char *allow;
    char *content_encoding;
    char *content_language;
    char *content_length;
    char *content_location;
    char *content_md5;
    char *content_type;
    char *expires;
    char *last_modified;
    char *extension_header;
} http_server_response_entity_headers_t;

typedef struct http_server_response_headers
{
    http_server_response_general_headers_t *general_header;
    http_server_response_request_headers_t *request_header;
    http_server_response_entity_headers_t *entity_header;
} http_server_response_headers_t;


typedef struct http_server_response
{
    http_server_response_status_line_t *status;
    http_server_response_headers_t *headers;
    char *body;
} http_server_response_t;


////////////////////////////
// Function HTTP SERVER   //
////////////////////////////
int http_server_initialize(http_server_info_t *sinfo);
int http_server_listen(http_server_info_t *sinfo);
int http_get_peer_client(SOCKET fd,http_client_peer_t *peer);
char *http_craft_response(http_server_response_t *ptr);
void http_free_craft_response(http_server_response_t *ptr);
void http_catch_error(int errorcode);