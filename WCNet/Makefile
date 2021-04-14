all:
	cl /c wcnet.c http.c http_response_parser.c http_server.c /I . /TC
	lib wcnet.obj http.obj http_response_parser.obj http_server.obj /MACHINE:x64 ws2_32.lib libcurl.lib zlib.lib normaliz.lib wldap32.lib crypt32.lib advapi32.lib Iphlpapi.lib Mswsock.lib libcrypto.lib libssl.lib user32.lib /OUT:wcnet.lib