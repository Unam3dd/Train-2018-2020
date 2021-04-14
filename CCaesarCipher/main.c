#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "caesar/caesar.h"

int main(int argc,char **argv)
{
	char message[] = "Hello World";
	char output[13] = {0};
	char *out = caesar_cipher(message,2);
	printf("Cipher text : %s\n",output);
	free(out);
	caesar_cipher_buffer(message,3,output);
	printf("Cipher text : %s\n",output);
	caesar_uncipher_buffer(output,3,output);
	printf("Uncipher text : %s\n",output);
	return (0);
}