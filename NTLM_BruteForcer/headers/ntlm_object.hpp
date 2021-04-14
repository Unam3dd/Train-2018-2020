#include <iostream>
#include "NTLM.hpp"


using namespace std;

class NTLM_Hash
{
    public:
        NTLM_Hash(string str);
        string hash_r;
        string get_hash();
};