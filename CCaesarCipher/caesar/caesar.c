#include "caesar.h"

///////////////////////////////////////////
// Caesar Cipher BEGIN
///////////////////////////////////////////

void caesar_init_struct(CaesarCipher *c)
{
    c->cipher = caesar_cipher;
    c->cipher_buffer = caesar_cipher_buffer;
    c->uncipher = caesar_uncipher;
    c->uncipher_buffer = caesar_uncipher_buffer;
}

char *caesar_cipher(char *plaintext,int shift)
{   
    if (plaintext == NULL)
        return (NULL);
    
    char *out = malloc(sizeof(plaintext));

    if (out == NULL)
        return (NULL);

    strcpy(out,plaintext);
    
    for (int n = 0;out[n] != '\0';n++)
    {       
        if (out[n] >='A' && out[n] <='Z'){
            out[n] = ((out[n]+shift - 'A')%26 + 'A'); // for ascii operations
        }

        if (out[n] >= 'a' && out[n] <= 'z'){
            out[n] = ((out[n]+shift - 'a')%26 + 'a');
        }
    }

    return (out);
}

char *caesar_uncipher(char *ciphertext,int shift)
{
    if (ciphertext == NULL)
        return (NULL);
    
    char *out = malloc(sizeof(ciphertext));

    if (out == NULL) return (NULL);
    
    strcpy(out,ciphertext);

    for (int n = 0;out[n] != '\0';n++)
    {
        if (out[n] >= 'A' && out[n] <= 'Z'){
            out[n] = ((out[n]-shift - 'Z')%26 + 'Z');
        }

        if (out[n] >= 'a' && out[n] <= 'z'){
            out[n] = ((out[n]-shift - 'z')%26 + 'z');
        }
    }

    return (out);
}


char *caesar_cipher_buffer(char *plaintext,int shift,char *buffer)
{
    if (plaintext == NULL)
        return (NULL);
    
    strcpy(buffer,plaintext);

    //strupr(buffer);

    for (int n = 0;buffer[n] != '\0';n++)
    {
        if (buffer[n] >= 'A' && buffer[n] <= 'Z'){
            buffer[n] = ((buffer[n]+shift - 'A')%26 + 'A');
        }

        if (buffer[n] >= 'a' && buffer[n] <= 'z'){
            buffer[n] = ((buffer[n]+shift - 'a')%26 + 'a');
        }
    }

    return (buffer);
}

char *caesar_uncipher_buffer(char *ciphertext,int shift,char *buffer)
{

    if (ciphertext == NULL)
        return (NULL);
    
    strcpy(buffer,ciphertext);

    for (int n = 0;buffer[n] != '\0';n++)
    {
        if (buffer[n] >= 'A' && buffer[n] <= 'Z'){
            buffer[n] = ((buffer[n]-shift - 'Z')%26 + 'Z');
        }

        if (buffer[n] >= 'a' && buffer[n] <= 'z'){
            buffer[n] = ((buffer[n]-shift - 'z')%26 + 'z');
        }
    }

    return (buffer);
}
///////////////////////////////////////////
// Caesar Cipher END
///////////////////////////////////////////