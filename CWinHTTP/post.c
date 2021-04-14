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