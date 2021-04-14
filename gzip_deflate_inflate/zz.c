#include <stdio.h>
#include <string.h>
#include <zlib.h>

// gcc zz.c -o zz.exe -I "C:\Users\unamed\Documents\C_C++\HttpParser\zlib" zlib\libz.a


char *compress_data(char *buffer,char *output)
{
    uLong ucompSize = strlen(buffer)+1;
    uLong compSize = compressBound(ucompSize);
    compress((Bytef *)output,&compSize,(Bytef *)buffer,ucompSize);

    return (output);
}

char *decompress_data(char *buffer,char *output)
{
    uLong ucompSize = strlen(buffer)+1;
    uLong compSize = compressBound(ucompSize);

    uncompress((Bytef *)output,&ucompSize,(Bytef *)buffer,compSize);

    return (output);
}


int gzip_compress_data(char *buffer,char *output,unsigned long size_in)
{
    z_stream compress;
    compress.zalloc = Z_NULL;
    compress.zfree = Z_NULL;
    compress.opaque = Z_NULL;
    compress.avail_in = (uInt)strlen(buffer)+1;
    compress.next_in = (Bytef *)buffer;
    compress.avail_out = (uInt)size_in;
    compress.next_out = (Bytef *)output;
    
    deflateInit2(&compress,Z_DEFAULT_COMPRESSION,Z_DEFLATED, 15 | 16,8,Z_DEFAULT_STRATEGY);
    deflate(&compress,Z_FINISH);
    deflateEnd(&compress);

    return (compress.total_out);
}


int gzip_decompress_data(char *buffer,unsigned long size_in, char *output)
{
    z_stream decompress;
    decompress.zalloc = Z_NULL;
    decompress.zfree = Z_NULL;
    decompress.opaque = Z_NULL;
    decompress.avail_in = (uInt)(size_in); // size of input
    decompress.next_in = (Bytef *)buffer; // input char array
    decompress.avail_out = (uInt)(size_in); // size of output
    decompress.next_out = (Bytef *)output; // output char array

    inflateInit2(&decompress,16+MAX_WBITS);
    inflate(&decompress, Z_NO_FLUSH);
    inflateEnd(&decompress);

    return (decompress.total_out);
}

int main()
{
    char test[50] = "Hello World";
    unsigned char test2[50] = {0};
    char test3[50] = {0};
    int size = 0;

    size = gzip_compress_data(test,test2,50);
    printf("Size : %d\n",size);
    int i = 0;

    while (i<=size)
    {
        printf("\\x%02x",test2[i]);
        i++;
    }

    printf("\n");

    size = gzip_decompress_data("\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\x0b\xf3\x48\xcd\xc9\xc9\x57\x08\xcf\x2f\xca\x49\x61\x00\x00\xfd\x0c\x40\x50\x0c\x00\x00\x00\x00",50,test3);
    printf("%s\n",test3);

    return (0);
}