#include "http.h"

int main()
{
	HttpResponse_t* res = requests_get("https://ifconfig.me/ip","chttp/1.0",FALSE);

	if (res == NULL)
		return (-1);

	if (res->headers->status->status_code == 200)
		printf("%s\n", res->body);

	free(res);
	return (0);
}