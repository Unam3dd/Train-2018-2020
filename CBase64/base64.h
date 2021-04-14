#include <stdio.h>
#include <stdlib.h>
#include "openssl/evp.h"
#include "openssl/err.h"

//https://www.openssl.org/docs/man1.0.2/man3/EVP_EncodeBlock.html

unsigned char *base64_encode(unsigned char *input,int len)
{
    int pad_len = (((len+2) / 3) * 4);
    unsigned char *output = (unsigned char *)calloc(pad_len+1,sizeof(unsigned char));

    if (output == NULL)
        return (NULL);

    int nbytes = EVP_EncodeBlock(output,input,len);

    if (nbytes > pad_len){
        fprintf(stderr,"[-] Error : not enough space in the buffer !\n");
        free(output);
        return (NULL);
    }

    return (output);
}

unsigned char *base64_decode(unsigned char *input,int len)
{
    int pad_len = (len*3)/4;
    unsigned char *output = (unsigned char *)calloc(pad_len,sizeof(unsigned char));

    if (output == NULL)
        return (NULL);
    
    int nbytes = EVP_DecodeBlock(output,input,len);

    if (nbytes > pad_len){
        fprintf(stderr,"[-] Error : not enough space in the buffer !\n");
        free(output);
        return (NULL);
    }

    return (output);
}