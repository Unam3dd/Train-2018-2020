# CurlWindowsHttp
Simple project with curl API with static API installed with vcpkg

## install libcurl with static library with vcpkg : 
 vcpkg.exe install libcurl:x64-windows-static
 vcpkg.exe install libcurl:x86-windows-static
 

```c
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
```
