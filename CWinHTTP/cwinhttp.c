/*MIT License

Copyright (c) 2020 Unam3dd

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/
#include "cwinhttp.h"

void CreateRequests(HttpSession *s)
{
    char link[100][100];
    char url[1024];
    strcpy(url,s->url);
    int c = 0;
    int cc = 2;
    char * token = strtok(url,":/");

    while (token != NULL)
    {
        //printf("%s\n",token);
        strcpy(link[c],token);
        token = strtok(NULL,":/");
        c++;
    }

    strcpy(s->protocol,link[0]);
    strcpy(s->domain,link[1]);

    while (cc != c)
    {
        strcat(s->path,link[cc]);
        cc++;

        if (cc == c)
            break;
        
        strcat(s->path,"/");
    }

    if (strcmp(s->protocol,"http") == 0){
        s->port = INTERNET_DEFAULT_HTTP_PORT;
        s->flag_secure = FALSE;
    } else {
        s->port = INTERNET_DEFAULT_HTTPS_PORT;
        s->flag_secure = TRUE;
    }
}

/////////////////////////////////////////
// Check Internet Functions
/////////////////////////////////////////

void CheckInternetStatus(HttpSession *s)
{
    DWORD check = InternetAttemptConnect(0);
    s->error_code_status = check;
    if (check != ERROR_SUCCESS)
        s->internet_status = FALSE;
    else
        s->internet_status = TRUE;
}

void CheckUrlConnection(HttpSession *s)
{
    if (InternetCheckConnectionA(s->url,FLAG_ICC_FORCE_CONNECTION,0) != TRUE)
        s->check_connection_url = (int)GetLastError();
    else
        s->check_connection_url = TRUE;
}


int CheckInternetStatusAndPingUrl(HttpSession *s){
    CheckInternetStatus(s);

    if (s->internet_status == FALSE)
        return (-2);
    
    CheckUrlConnection(s);

    if (s->check_connection_url != TRUE)
        return (-1);
    
    return (0);
}

/////////////////////////////////////////
// Http Send Functions 
/////////////////////////////////////////
int HttpReq(HttpSession *s,HttpResponse *r)
{    
    HINTERNET hInternet,hConnect,hRequest;
    char buffer[BUFFER_SIZE];
    char lensize[BUFFER_SIZE];
    BOOL KeepReading = TRUE;
    DWORD SizeHeaders = 4096;
    DWORD ContentLength;
    DWORD BytesRead = -1;
    char hdrs[] = "Content-Type: application/x-www-form-urlencoded";

    CheckInternetStatus(s);

    CreateRequests(s);

    if (s->async_request != INTERNET_FLAG_ASYNC)
        s->async_request = 0;

    if (strlen(s->ua) == 1)
        hInternet = InternetOpenA(NULL,INTERNET_OPEN_TYPE_DIRECT,NULL,NULL,s->async_request);
    else
        hInternet = InternetOpenA(s->ua,INTERNET_OPEN_TYPE_DIRECT,NULL,NULL,s->async_request);

    if (hInternet == NULL)
        return ((int)GetLastError());
    
    
    hConnect = InternetConnectA(hInternet,s->domain,s->port,NULL,NULL,INTERNET_SERVICE_HTTP,s->async_request,0);

    if (hConnect == NULL)
        return ((int)GetLastError());
    
    if (strlen(s->accesstypes) == 0)
        strcpy(s->accesstypes,"*/*");
    
    LPCSTR parrAcceptTypes[] = { s->accesstypes,NULL};

    if (s->flag_secure == 1)
        hRequest = HttpOpenRequestA(hConnect,s->methods,s->path,"HTTP/1.1",NULL,parrAcceptTypes,INTERNET_FLAG_SECURE,0);
    else
        hRequest = HttpOpenRequestA(hConnect,s->methods,s->path,"HTTP/1.1",NULL,parrAcceptTypes,0,0);
    
    if (hRequest == NULL)
        return ((int)GetLastError());
    
    if (strcmp(s->methods,"GET") == 0)
        HttpSendRequestA(hRequest,NULL,0,NULL,0);
    else
        HttpSendRequestA(hRequest,hdrs,strlen(hdrs),s->postvalue,strlen(s->postvalue));
    
 
    memset(buffer,0,sizeof(buffer));

    HttpQueryInfoA(hRequest,HTTP_QUERY_RAW_HEADERS_CRLF,r->headers,&SizeHeaders,NULL);
    HttpQueryInfoA(hRequest,HTTP_QUERY_STATUS_CODE,r->status_code_str,&SizeHeaders,NULL);
    HttpQueryInfoA(hRequest,HTTP_QUERY_STATUS_TEXT,r->status,&SizeHeaders,NULL);
    HttpQueryInfo(hRequest,HTTP_QUERY_USER_AGENT,r->ua,&SizeHeaders,NULL);
    r->status_code = atoi(r->status_code_str);

    
    while (KeepReading && BytesRead != 0)
    {
        KeepReading = InternetReadFile(hRequest,buffer,BUFFER_SIZE,&BytesRead);
        strcat(lensize,buffer);
        memset(buffer,0,sizeof(buffer));
    }

    r->text = (char *)malloc(strlen(lensize)+1 * sizeof(char));
    printf("%d\n",strlen(lensize)+1 * sizeof(char));

    if (r->text == NULL)
        return (0);
    
    memset(r->text,0,sizeof(r->text));
    strcpy(r->text,lensize);

    InternetCloseHandle(hRequest);
    InternetCloseHandle(hConnect);
    InternetCloseHandle(hInternet);

    return (1);
}

void FreeTextContent(HttpResponse *r)
{
    free(r->text);
    return;
}
