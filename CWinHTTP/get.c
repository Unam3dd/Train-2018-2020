#include "cwinhttp.h"

// Compile : gcc cwinhttp.c post.c -o post.exe -lwininet

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
