#include "ntlm_object.hpp"

using namespace std;


NTLM_Hash::NTLM_Hash(string str)
{
    NTLM_Hash::hash_r.clear();
    const char* const_str = str.c_str();
    char *get_hash = NTLM((char *)const_str);
    this->NTLM_Hash::hash_r = get_hash;
}

string NTLM_Hash::get_hash()
{
    return NTLM_Hash::hash_r;
}