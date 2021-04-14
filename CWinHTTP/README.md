# CWinHTTP
Simple Windows Wininet HTTP Wrapper

```cpp
#include "cwinhttp.h"

// Compile : gcc cwinhttp.c get.c -o get.exe -lwininet

int main()
{
    HttpSession s;
    HttpResponse r;
    strcpy(s.url,"http://ifconfig.me/ip");
    strcpy(s.methods,"GET");
    
    if (HttpReq(&s,&r) != TRUE)
        exit(2);

    printf("%s\n",r.headers);
    printf("%s\n",r.text);
    printf("%s\n",r.status);
    printf("%d\n",r.status_code);
    
    memset(&r,0,sizeof(r));
    FreeTextContent(&r);
    return (0);
}

```

```cpp
#include "cwinhttp.h"

// Compile : gcc cwinhttp.c post.c -o post.exe -lwininet

int main()
{
    HttpSession s;
    HttpResponse r;
    strcpy(s.url,"https://postman-echo.com/post");
    strcpy(s.methods,"POST");
    strcpy(s.postvalue,"Hello");
    
    if (HttpReq(&s,&r) != TRUE)
        exit(2);
    
    printf("%s\n",r.headers);
    printf("%s\n",r.text);

    memset(&s,0,sizeof(s));
    memset(&r,0,sizeof(r));
    FreeTextContent(&r);
   
    return (0);
}
```
