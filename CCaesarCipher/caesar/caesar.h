#pragma once
#include <stdlib.h>
#include <string.h>


typedef struct CaesarCipher
{
    char *(*cipher)(char *plaintext,int shift);
    char *(*uncipher)(char *ciphertext,int shift);
    char *(*cipher_buffer)(char *plaintext,int shift,char *buffer);
    char *(*uncipher_buffer)(char *ciphertext,int shift,char *buffer);
} CaesarCipher;

void caesar_init_struct(CaesarCipher *c);
char *caesar_cipher(char *plaintext,int shift);
char *caesar_uncipher(char *ciphertext,int shift);
char *caesar_cipher_buffer(char *plaintext,int shift,char *buffer);
char *caesar_uncipher_buffer(char *ciphertext,int shift,char *buffer);
///////////////////////////////////////////
// Caesar Cipher END
///////////////////////////////////////////