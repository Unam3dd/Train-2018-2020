#include "base64.h"

// cl /c test.c /I .
// link.exe /MACHINE:x64 test.obj  ws2_32.lib lib\libcrypto.lib lib\libssl.lib advapi32.lib crypt32.lib user32.lib

int main(int argc,char **argv)
{
    unsigned char *b64_output = base64_encode("hello",5);

    printf("%s\n",b64_output);

    unsigned char *uncoded = base64_decode(b64_output,strlen(b64_output));

    printf("%s\n",uncoded);
}
