#include <stdio.h>
#include "http_response_parser.h"

int main(void)
{
    char response[] = "HTTP/1.1 404 Not Found\r\nDate: Mon, 12 Oct 2020 20:52:51 GMT\r\nContent-Type: application/json; charset=utf-8\r\nContent-Length: 96\r\nVary: Accept-Encoding\r\nX-Powered-By: Express\r\nAccess-Control-Allow-Origin: *\r\nX-Frame-Options: DENY\r\nX-XSS-Protection: 1; mode=block\r\nX-Content-Type-Options: nosniff\r\nReferrer-Policy: strict-origin-when-cross-origin\r\nSet-Cookie: flash=; Path=/; Expires=Thu, 01 Jan 1970 00:00:00 GMT\r\nVia: 1.1 google\r\n\r\nPlease provide a valid IP address";
    char output[1024] = {0};
    HttpResponse_t h = {0};
    
    http_parse_response(&h,response);
    
    printf("%s\n\n",h.body);
    printf("%s\n\n",h.headers->status->status_line);
    printf("%s\n\n",h.headers->status->http_version);
    printf("%ld\n\n",h.headers->status->status_code);
    printf("%s\n\n",h.headers->status->reason_phrase);
    printf("%s\n\n",h.headers->rawheaders);
    
    http_parse_response_get_headers_value(&h,"Content-Type",output);
    printf("%s\n",output);
    
    free_parse_http_response(&h);
    
    return (EXIT_SUCCESS);
}
