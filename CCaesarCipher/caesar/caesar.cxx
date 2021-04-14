#include "caesar.hxx"

std::string CaesarCipher::cipher(std::string plaintext,int shift)
{
    if (plaintext.length() == 0)
        return (NULL);
    
    std::string output = plaintext;

    for (int n = 0;output[n] != '\0';n++)
    {
        if (output[n] >='A' && output[n] <= 'Z')
            output[n] = ((output[n] + shift - 'A')%26 + 'A');
        
        else if (output[n] >= 'a' && output[n] <= 'z')
            output[n] = ((output[n] + shift - 'a')%26 + 'a');
    }

    return (output);
}

std::string CaesarCipher::uncipher(std::string ciphertext,int shift)
{
    if (ciphertext.length() == 0)
        return (NULL);

    
    std::string output = ciphertext;

    for (int n = 0;output[n] != '\0';n++)
    {
        if (output[n] >= 'A' && output[n] <= 'Z')
            output[n] = ((output[n] - shift - 'Z')%26 + 'Z');
        
        else if (output[n] >= 'a' && output[n] <= 'z')
            output[n] = ((output[n] - shift - 'z')%26 + 'z');
    }

    return (output);
}