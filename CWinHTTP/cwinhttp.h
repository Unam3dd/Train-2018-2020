#include <string.h>
#include <windows.h>
#include <stdio.h>
#include <WinInet.h>

#pragma comment(lib,"Wininet.lib")

#define BUFFER_SIZE 300000

//https://support.microsoft.com/en-us/help/193625/info-wininet-error-codes-12001-through-12156

//////////////////////////
// Structure
///////////////////////////

typedef struct HTTPResponse {
    char *text;
    char headers[1024];
    char ua[1024];
    char status[100];
    char status_code_str[100];
    int status_code;
} HttpResponse;

typedef struct HTTPSession {
    int internet_status;
    int error_code_status;
    int check_connection_url;
    int port;
    int async_request;
    char postvalue[4096];
    int flag_secure;
    char headers[1024];
    char winineterror[1024];
    char methods[10];
    char protocol[6];
    char domain[100];
    char path[1024];
    char accesstypes[100];
    char url[1024];
    char ua[1024];
} HttpSession;

/////////////////////////////////////////
// Create Function Parse URL
/////////////////////////////////////////

void CreateRequests(HttpSession *s);

/////////////////////////////////////////
// Check Internet Functions
/////////////////////////////////////////
void CheckInternetStatus(HttpSession *s);
void CheckUrlConnection(HttpSession *s);
int CheckInternetStatusAndPingUrl(HttpSession *s);

//////////////////////////////////////////
// Parse Functions
/////////////////////////////////////////

void ParseHeadersInformations(HttpResponse *r);

/////////////////////////////////////////
//  Send Functions
/////////////////////////////////////////

int HttpReq(HttpSession *s,HttpResponse *r);
void FreeTextContent(HttpResponse *r);



// Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0