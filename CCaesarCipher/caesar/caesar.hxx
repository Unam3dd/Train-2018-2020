#include <iostream>

class CaesarCipher
{
    public:
        std::string cipher(std::string plaintext,int shift);
        std::string uncipher(std::string ciphertext,int shift);
};